Object.defineProperty(exports, "__esModule", { value: true });
exports.SidebarSpacer = exports.generateTransactionLink = exports.generateTraceLink = exports.transactionSummaryRouteWithQuery = exports.generateTransactionSummaryRoute = exports.TransactionFilterOptions = void 0;
const tslib_1 = require("tslib");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const urls_1 = require("app/utils/discover/urls");
const tokenizeSearch_1 = require("app/utils/tokenizeSearch");
const utils_1 = require("app/views/performance/traceDetails/utils");
const utils_2 = require("../utils");
var TransactionFilterOptions;
(function (TransactionFilterOptions) {
    TransactionFilterOptions["FASTEST"] = "fastest";
    TransactionFilterOptions["SLOW"] = "slow";
    TransactionFilterOptions["OUTLIER"] = "outlier";
    TransactionFilterOptions["RECENT"] = "recent";
})(TransactionFilterOptions = exports.TransactionFilterOptions || (exports.TransactionFilterOptions = {}));
function generateTransactionSummaryRoute({ orgSlug }) {
    return `/organizations/${orgSlug}/performance/summary/`;
}
exports.generateTransactionSummaryRoute = generateTransactionSummaryRoute;
function cleanTransactionSummaryFilter(query) {
    const filterParams = new tokenizeSearch_1.MutableSearch(query);
    filterParams.removeFilter('transaction');
    return filterParams.formatString();
}
function transactionSummaryRouteWithQuery({ orgSlug, transaction, projectID, query, unselectedSeries = 'p100()', display, trendFunction, trendColumn, showTransactions, additionalQuery, }) {
    const pathname = generateTransactionSummaryRoute({
        orgSlug,
    });
    let searchFilter;
    if (typeof query.query === 'string') {
        searchFilter = cleanTransactionSummaryFilter(query.query);
    }
    else {
        searchFilter = query.query;
    }
    return {
        pathname,
        query: Object.assign({ transaction, project: projectID, environment: query.environment, statsPeriod: query.statsPeriod, start: query.start, end: query.end, query: searchFilter, unselectedSeries,
            showTransactions,
            display,
            trendFunction,
            trendColumn }, additionalQuery),
    };
}
exports.transactionSummaryRouteWithQuery = transactionSummaryRouteWithQuery;
function generateTraceLink(dateSelection) {
    return (organization, tableRow, _query) => {
        const traceId = `${tableRow.trace}`;
        if (!traceId) {
            return {};
        }
        return (0, utils_1.getTraceDetailsUrl)(organization, traceId, dateSelection, {});
    };
}
exports.generateTraceLink = generateTraceLink;
function generateTransactionLink(transactionName) {
    return (organization, tableRow, query, hash) => {
        const eventSlug = (0, urls_1.generateEventSlug)(tableRow);
        return (0, utils_2.getTransactionDetailsUrl)(organization, eventSlug, transactionName, query, hash);
    };
}
exports.generateTransactionLink = generateTransactionLink;
exports.SidebarSpacer = (0, styled_1.default)('div') `
  margin-top: ${(0, space_1.default)(3)};
`;
//# sourceMappingURL=utils.jsx.map