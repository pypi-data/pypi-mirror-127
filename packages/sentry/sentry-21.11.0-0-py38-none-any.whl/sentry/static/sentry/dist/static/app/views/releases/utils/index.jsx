Object.defineProperty(exports, "__esModule", { value: true });
exports.isMobileRelease = exports.ADOPTION_STAGE_LABELS = exports.getReleaseParams = exports.getReleaseBounds = exports.isReleaseArchived = exports.getReleaseHandledIssuesUrl = exports.getReleaseUnhandledIssuesUrl = exports.getReleaseNewIssuesUrl = exports.displaySessionStatusPercent = exports.getSessionStatusPercent = exports.displayCrashFreePercent = exports.getCrashFreePercent = exports.roundDuration = exports.CRASH_FREE_DECIMAL_THRESHOLD = void 0;
const tslib_1 = require("tslib");
const pick_1 = (0, tslib_1.__importDefault)(require("lodash/pick"));
const round_1 = (0, tslib_1.__importDefault)(require("lodash/round"));
const moment_1 = (0, tslib_1.__importDefault)(require("moment"));
const externalLink_1 = (0, tslib_1.__importDefault)(require("app/components/links/externalLink"));
const getParams_1 = require("app/components/organizations/globalSelectionHeader/getParams");
const globalSelectionHeader_1 = require("app/constants/globalSelectionHeader");
const platformCategories_1 = require("app/data/platformCategories");
const locale_1 = require("app/locale");
const types_1 = require("app/types");
const tokenizeSearch_1 = require("app/utils/tokenizeSearch");
const utils_1 = require("app/views/issueList/utils");
exports.CRASH_FREE_DECIMAL_THRESHOLD = 95;
const roundDuration = (seconds) => {
    return (0, round_1.default)(seconds, seconds > 60 ? 0 : 3);
};
exports.roundDuration = roundDuration;
const getCrashFreePercent = (percent, decimalThreshold = exports.CRASH_FREE_DECIMAL_THRESHOLD, decimalPlaces = 3) => {
    const roundedValue = (0, round_1.default)(percent, percent > decimalThreshold ? decimalPlaces : 0);
    if (roundedValue === 100 && percent < 100) {
        return (Math.floor(percent * Math.pow(10, decimalPlaces)) / Math.pow(10, decimalPlaces));
    }
    return roundedValue;
};
exports.getCrashFreePercent = getCrashFreePercent;
const displayCrashFreePercent = (percent, decimalThreshold = exports.CRASH_FREE_DECIMAL_THRESHOLD, decimalPlaces = 3) => {
    if (isNaN(percent)) {
        return '\u2015';
    }
    if (percent < 1 && percent > 0) {
        return `<1\u0025`;
    }
    const rounded = (0, exports.getCrashFreePercent)(percent, decimalThreshold, decimalPlaces).toLocaleString();
    return `${rounded}\u0025`;
};
exports.displayCrashFreePercent = displayCrashFreePercent;
const getSessionStatusPercent = (percent, absolute = true) => {
    return (0, round_1.default)(absolute ? Math.abs(percent) : percent, 3);
};
exports.getSessionStatusPercent = getSessionStatusPercent;
const displaySessionStatusPercent = (percent, absolute = true) => {
    return `${(0, exports.getSessionStatusPercent)(percent, absolute).toLocaleString()}\u0025`;
};
exports.displaySessionStatusPercent = displaySessionStatusPercent;
const getReleaseNewIssuesUrl = (orgSlug, projectId, version) => {
    return {
        pathname: `/organizations/${orgSlug}/issues/`,
        query: {
            project: projectId,
            // we are resetting time selector because releases' new issues count doesn't take time selector into account
            statsPeriod: undefined,
            start: undefined,
            end: undefined,
            query: new tokenizeSearch_1.MutableSearch([`firstRelease:${version}`]).formatString(),
            sort: utils_1.IssueSortOptions.FREQ,
        },
    };
};
exports.getReleaseNewIssuesUrl = getReleaseNewIssuesUrl;
const getReleaseUnhandledIssuesUrl = (orgSlug, projectId, version, dateTime = {}) => {
    return {
        pathname: `/organizations/${orgSlug}/issues/`,
        query: Object.assign(Object.assign({}, dateTime), { project: projectId, query: new tokenizeSearch_1.MutableSearch([
                `release:${version}`,
                'error.unhandled:true',
            ]).formatString(), sort: utils_1.IssueSortOptions.FREQ }),
    };
};
exports.getReleaseUnhandledIssuesUrl = getReleaseUnhandledIssuesUrl;
const getReleaseHandledIssuesUrl = (orgSlug, projectId, version, dateTime = {}) => {
    return {
        pathname: `/organizations/${orgSlug}/issues/`,
        query: Object.assign(Object.assign({}, dateTime), { project: projectId, query: new tokenizeSearch_1.MutableSearch([
                `release:${version}`,
                'error.handled:true',
            ]).formatString(), sort: utils_1.IssueSortOptions.FREQ }),
    };
};
exports.getReleaseHandledIssuesUrl = getReleaseHandledIssuesUrl;
const isReleaseArchived = (release) => release.status === types_1.ReleaseStatus.Archived;
exports.isReleaseArchived = isReleaseArchived;
function getReleaseBounds(release) {
    var _a;
    const { lastEvent, currentProjectMeta, dateCreated } = release || {};
    const { sessionsUpperBound } = currentProjectMeta || {};
    const releaseStart = (0, moment_1.default)(dateCreated).startOf('minute').utc().format();
    const releaseEnd = (0, moment_1.default)((_a = ((0, moment_1.default)(sessionsUpperBound).isAfter(lastEvent) ? sessionsUpperBound : lastEvent)) !== null && _a !== void 0 ? _a : undefined)
        .endOf('minute')
        .utc()
        .format();
    if ((0, moment_1.default)(releaseStart).isSame(releaseEnd, 'minute')) {
        return {
            releaseStart,
            releaseEnd: (0, moment_1.default)(releaseEnd).add(1, 'minutes').utc().format(),
        };
    }
    const thousandDaysAfterReleaseStart = (0, moment_1.default)(releaseStart).add('999', 'days');
    if (thousandDaysAfterReleaseStart.isBefore(releaseEnd)) {
        // if the release spans for more than thousand days, we need to clamp it
        // (otherwise we would hit the backend limit for the amount of data buckets)
        return {
            releaseStart,
            releaseEnd: thousandDaysAfterReleaseStart.utc().format(),
        };
    }
    return {
        releaseStart,
        releaseEnd,
    };
}
exports.getReleaseBounds = getReleaseBounds;
function getReleaseParams({ location, releaseBounds }) {
    const params = (0, getParams_1.getParams)((0, pick_1.default)(location.query, [
        ...Object.values(globalSelectionHeader_1.URL_PARAM),
        ...Object.values(globalSelectionHeader_1.PAGE_URL_PARAM),
        'cursor',
    ]), {
        allowAbsolutePageDatetime: true,
        allowEmptyPeriod: true,
    });
    if (!Object.keys(params).some(param => [globalSelectionHeader_1.URL_PARAM.START, globalSelectionHeader_1.URL_PARAM.END, globalSelectionHeader_1.URL_PARAM.UTC, globalSelectionHeader_1.URL_PARAM.PERIOD].includes(param))) {
        params[globalSelectionHeader_1.URL_PARAM.START] = releaseBounds.releaseStart;
        params[globalSelectionHeader_1.URL_PARAM.END] = releaseBounds.releaseEnd;
    }
    return params;
}
exports.getReleaseParams = getReleaseParams;
const adoptionStagesLink = (<externalLink_1.default href="https://docs.sentry.io/product/releases/health/#adoption-stages"/>);
exports.ADOPTION_STAGE_LABELS = {
    low_adoption: {
        name: (0, locale_1.t)('Low Adoption'),
        tooltipTitle: (0, locale_1.tct)('This release has a low percentage of sessions compared to other releases in this project. [link:Learn more]', { link: adoptionStagesLink }),
        type: 'warning',
    },
    adopted: {
        name: (0, locale_1.t)('Adopted'),
        tooltipTitle: (0, locale_1.tct)('This release has a high percentage of sessions compared to other releases in this project. [link:Learn more]', { link: adoptionStagesLink }),
        type: 'success',
    },
    replaced: {
        name: (0, locale_1.t)('Replaced'),
        tooltipTitle: (0, locale_1.tct)('This release was previously Adopted, but now has a lower level of sessions compared to other releases in this project. [link:Learn more]', { link: adoptionStagesLink }),
        type: 'default',
    },
};
const isMobileRelease = (releaseProjectPlatform) => [...platformCategories_1.mobile, ...platformCategories_1.desktop].includes(releaseProjectPlatform);
exports.isMobileRelease = isMobileRelease;
//# sourceMappingURL=index.jsx.map