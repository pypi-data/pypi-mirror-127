Object.defineProperty(exports, "__esModule", { value: true });
exports.getPerformanceDuration = exports.PerformanceDuration = exports.getTransactionName = exports.addRoutePerformanceContext = exports.getTransactionComparisonUrl = exports.getTransactionDetailsUrl = exports.removeTracingKeysFromSearch = exports.trendsTargetRoute = exports.handleTrendsClick = exports.getTransactionSearchQuery = exports.getPerformanceTrendsUrl = exports.getPerformanceLandingUrl = exports.isSummaryViewFrontend = exports.isSummaryViewFrontendPageLoad = exports.platformAndConditionsToPerformanceType = exports.platformToPerformanceType = exports.PROJECT_PERFORMANCE_TYPE = void 0;
const tslib_1 = require("tslib");
const react_router_1 = require("react-router");
const duration_1 = (0, tslib_1.__importDefault)(require("app/components/duration"));
const globalSelectionHeader_1 = require("app/constants/globalSelectionHeader");
const platformCategories_1 = require("app/data/platformCategories");
const utils_1 = require("app/utils");
const analytics_1 = require("app/utils/analytics");
const dates_1 = require("app/utils/dates");
const fields_1 = require("app/utils/discover/fields");
const formatters_1 = require("app/utils/formatters");
const getCurrentSentryReactTransaction_1 = (0, tslib_1.__importDefault)(require("app/utils/getCurrentSentryReactTransaction"));
const queryString_1 = require("app/utils/queryString");
const tokenizeSearch_1 = require("app/utils/tokenizeSearch");
const utils_2 = require("./trends/utils");
/**
 * Performance type can used to determine a default view or which specific field should be used by default on pages
 * where we don't want to wait for transaction data to return to determine how to display aspects of a page.
 */
var PROJECT_PERFORMANCE_TYPE;
(function (PROJECT_PERFORMANCE_TYPE) {
    PROJECT_PERFORMANCE_TYPE["ANY"] = "any";
    PROJECT_PERFORMANCE_TYPE["FRONTEND"] = "frontend";
    PROJECT_PERFORMANCE_TYPE["BACKEND"] = "backend";
    PROJECT_PERFORMANCE_TYPE["FRONTEND_OTHER"] = "frontend_other";
    PROJECT_PERFORMANCE_TYPE["MOBILE"] = "mobile";
})(PROJECT_PERFORMANCE_TYPE = exports.PROJECT_PERFORMANCE_TYPE || (exports.PROJECT_PERFORMANCE_TYPE = {}));
const FRONTEND_PLATFORMS = [...platformCategories_1.frontend];
const BACKEND_PLATFORMS = [...platformCategories_1.backend];
const MOBILE_PLATFORMS = [...platformCategories_1.mobile];
function platformToPerformanceType(projects, projectIds) {
    if (projectIds.length === 0 || projectIds[0] === globalSelectionHeader_1.ALL_ACCESS_PROJECTS) {
        return PROJECT_PERFORMANCE_TYPE.ANY;
    }
    const selectedProjects = projects.filter(p => projectIds.includes(parseInt(`${p.id}`, 10)));
    if (selectedProjects.length === 0 || selectedProjects.some(p => !p.platform)) {
        return PROJECT_PERFORMANCE_TYPE.ANY;
    }
    if (selectedProjects.every(project => FRONTEND_PLATFORMS.includes(project.platform))) {
        return PROJECT_PERFORMANCE_TYPE.FRONTEND;
    }
    if (selectedProjects.every(project => BACKEND_PLATFORMS.includes(project.platform))) {
        return PROJECT_PERFORMANCE_TYPE.BACKEND;
    }
    if (selectedProjects.every(project => MOBILE_PLATFORMS.includes(project.platform))) {
        return PROJECT_PERFORMANCE_TYPE.MOBILE;
    }
    return PROJECT_PERFORMANCE_TYPE.ANY;
}
exports.platformToPerformanceType = platformToPerformanceType;
/**
 * Used for transaction summary to determine appropriate columns on a page, since there is no display field set for the page.
 */
function platformAndConditionsToPerformanceType(projects, eventView) {
    const performanceType = platformToPerformanceType(projects, eventView.project);
    if (performanceType === PROJECT_PERFORMANCE_TYPE.FRONTEND) {
        const conditions = new tokenizeSearch_1.MutableSearch(eventView.query);
        const ops = conditions.getFilterValues('!transaction.op');
        if (ops.some(op => op === 'pageload')) {
            return PROJECT_PERFORMANCE_TYPE.FRONTEND_OTHER;
        }
    }
    return performanceType;
}
exports.platformAndConditionsToPerformanceType = platformAndConditionsToPerformanceType;
/**
 * Used for transaction summary to check the view itself, since it can have conditions which would exclude it from having vitals aside from platform.
 */
function isSummaryViewFrontendPageLoad(eventView, projects) {
    return (platformAndConditionsToPerformanceType(projects, eventView) ===
        PROJECT_PERFORMANCE_TYPE.FRONTEND);
}
exports.isSummaryViewFrontendPageLoad = isSummaryViewFrontendPageLoad;
function isSummaryViewFrontend(eventView, projects) {
    return (platformAndConditionsToPerformanceType(projects, eventView) ===
        PROJECT_PERFORMANCE_TYPE.FRONTEND ||
        platformAndConditionsToPerformanceType(projects, eventView) ===
            PROJECT_PERFORMANCE_TYPE.FRONTEND_OTHER);
}
exports.isSummaryViewFrontend = isSummaryViewFrontend;
function getPerformanceLandingUrl(organization) {
    return `/organizations/${organization.slug}/performance/`;
}
exports.getPerformanceLandingUrl = getPerformanceLandingUrl;
function getPerformanceTrendsUrl(organization) {
    return `/organizations/${organization.slug}/performance/trends/`;
}
exports.getPerformanceTrendsUrl = getPerformanceTrendsUrl;
function getTransactionSearchQuery(location, query = '') {
    return (0, queryString_1.decodeScalar)(location.query.query, query).trim();
}
exports.getTransactionSearchQuery = getTransactionSearchQuery;
function handleTrendsClick({ location, organization, }) {
    (0, analytics_1.trackAnalyticsEvent)({
        eventKey: 'performance_views.change_view',
        eventName: 'Performance Views: Change View',
        organization_id: parseInt(organization.id, 10),
        view_name: 'TRENDS',
    });
    const target = trendsTargetRoute({ location, organization });
    react_router_1.browserHistory.push(target);
}
exports.handleTrendsClick = handleTrendsClick;
function trendsTargetRoute({ location, organization, initialConditions, additionalQuery, }) {
    const newQuery = Object.assign(Object.assign({}, location.query), additionalQuery);
    const query = (0, queryString_1.decodeScalar)(location.query.query, '');
    const conditions = new tokenizeSearch_1.MutableSearch(query);
    const modifiedConditions = initialConditions !== null && initialConditions !== void 0 ? initialConditions : new tokenizeSearch_1.MutableSearch([]);
    if (conditions.hasFilter('tpm()')) {
        modifiedConditions.setFilterValues('tpm()', conditions.getFilterValues('tpm()'));
    }
    else {
        modifiedConditions.setFilterValues('tpm()', ['>0.01']);
    }
    if (conditions.hasFilter('transaction.duration')) {
        modifiedConditions.setFilterValues('transaction.duration', conditions.getFilterValues('transaction.duration'));
    }
    else {
        modifiedConditions.setFilterValues('transaction.duration', [
            '>0',
            `<${utils_2.DEFAULT_MAX_DURATION}`,
        ]);
    }
    newQuery.query = modifiedConditions.formatString();
    return { pathname: getPerformanceTrendsUrl(organization), query: Object.assign({}, newQuery) };
}
exports.trendsTargetRoute = trendsTargetRoute;
function removeTracingKeysFromSearch(currentFilter, options = {
    excludeTagKeys: new Set([
        // event type can be "transaction" but we're searching for issues
        'event.type',
        // the project is already determined by the transaction,
        // and issue search does not support the project filter
        'project',
    ]),
}) {
    currentFilter.getFilterKeys().forEach(tagKey => {
        const searchKey = tagKey.startsWith('!') ? tagKey.substr(1) : tagKey;
        // Remove aggregates and transaction event fields
        if (
        // aggregates
        searchKey.match(/\w+\(.*\)/) ||
            // transaction event fields
            fields_1.TRACING_FIELDS.includes(searchKey) ||
            // tags that we don't want to pass to pass to issue search
            options.excludeTagKeys.has(searchKey)) {
            currentFilter.removeFilter(tagKey);
        }
    });
    return currentFilter;
}
exports.removeTracingKeysFromSearch = removeTracingKeysFromSearch;
function getTransactionDetailsUrl(organization, eventSlug, transaction, query, hash) {
    const target = {
        pathname: `/organizations/${organization.slug}/performance/${eventSlug}/`,
        query: Object.assign(Object.assign({}, query), { transaction }),
        hash,
    };
    if (!(0, utils_1.defined)(hash)) {
        delete target.hash;
    }
    return target;
}
exports.getTransactionDetailsUrl = getTransactionDetailsUrl;
function getTransactionComparisonUrl({ organization, baselineEventSlug, regressionEventSlug, transaction, query, }) {
    return {
        pathname: `/organizations/${organization.slug}/performance/compare/${baselineEventSlug}/${regressionEventSlug}/`,
        query: Object.assign(Object.assign({}, query), { transaction }),
    };
}
exports.getTransactionComparisonUrl = getTransactionComparisonUrl;
function addRoutePerformanceContext(selection) {
    const transaction = (0, getCurrentSentryReactTransaction_1.default)();
    const days = (0, dates_1.statsPeriodToDays)(selection.datetime.period, selection.datetime.start, selection.datetime.end);
    const oneDay = 86400;
    const seconds = Math.floor(days * oneDay);
    transaction === null || transaction === void 0 ? void 0 : transaction.setTag('query.period', seconds.toString());
    let groupedPeriod = '>30d';
    if (seconds <= oneDay) {
        groupedPeriod = '<=1d';
    }
    else if (seconds <= oneDay * 7) {
        groupedPeriod = '<=7d';
    }
    else if (seconds <= oneDay * 14) {
        groupedPeriod = '<=14d';
    }
    else if (seconds <= oneDay * 30) {
        groupedPeriod = '<=30d';
    }
    transaction === null || transaction === void 0 ? void 0 : transaction.setTag('query.period.grouped', groupedPeriod);
}
exports.addRoutePerformanceContext = addRoutePerformanceContext;
function getTransactionName(location) {
    const { transaction } = location.query;
    return (0, queryString_1.decodeScalar)(transaction);
}
exports.getTransactionName = getTransactionName;
const hasMilliseconds = (props) => {
    return (0, utils_1.defined)(props.milliseconds);
};
function PerformanceDuration(props) {
    const normalizedSeconds = hasMilliseconds(props)
        ? props.milliseconds / 1000
        : props.seconds;
    return (<duration_1.default abbreviation={props.abbreviation} seconds={normalizedSeconds} fixedDigits={2}/>);
}
exports.PerformanceDuration = PerformanceDuration;
function getPerformanceDuration(milliseconds) {
    return (0, formatters_1.getDuration)(milliseconds / 1000, milliseconds > 1000 ? 2 : 0, true);
}
exports.getPerformanceDuration = getPerformanceDuration;
//# sourceMappingURL=utils.jsx.map