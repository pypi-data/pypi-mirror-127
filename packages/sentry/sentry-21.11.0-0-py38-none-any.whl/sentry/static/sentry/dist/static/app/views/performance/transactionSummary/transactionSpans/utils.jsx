Object.defineProperty(exports, "__esModule", { value: true });
exports.getSuspectSpanSortFromEventView = exports.getSuspectSpanSortFromLocation = exports.SPAN_SORT_OPTIONS = exports.spansRouteWithQuery = exports.generateSpansRoute = void 0;
const locale_1 = require("app/locale");
const queryString_1 = require("app/utils/queryString");
const types_1 = require("./types");
function generateSpansRoute({ orgSlug }) {
    return `/organizations/${orgSlug}/performance/summary/spans/`;
}
exports.generateSpansRoute = generateSpansRoute;
function spansRouteWithQuery({ orgSlug, transaction, projectID, query, }) {
    const pathname = generateSpansRoute({
        orgSlug,
    });
    return {
        pathname,
        query: {
            transaction,
            project: projectID,
            environment: query.environment,
            statsPeriod: query.statsPeriod,
            start: query.start,
            end: query.end,
            query: query.query,
        },
    };
}
exports.spansRouteWithQuery = spansRouteWithQuery;
exports.SPAN_SORT_OPTIONS = [
    {
        prefix: (0, locale_1.t)('Percentile'),
        label: (0, locale_1.t)('p50 Duration'),
        field: types_1.SpanSortPercentiles.P50_EXCLUSIVE_TIME,
    },
    {
        prefix: (0, locale_1.t)('Percentile'),
        label: (0, locale_1.t)('p75 Duration'),
        field: types_1.SpanSortPercentiles.P75_EXCLUSIVE_TIME,
    },
    {
        prefix: (0, locale_1.t)('Percentile'),
        label: (0, locale_1.t)('p95 Duration'),
        field: types_1.SpanSortPercentiles.P95_EXCLUSIVE_TIME,
    },
    {
        prefix: (0, locale_1.t)('Percentile'),
        label: (0, locale_1.t)('p99 Duration'),
        field: types_1.SpanSortPercentiles.P99_EXCLUSIVE_TIME,
    },
    {
        prefix: (0, locale_1.t)('Total'),
        label: (0, locale_1.t)('Cumulative Duration'),
        field: types_1.SpanSortOthers.SUM_EXCLUSIVE_TIME,
    },
    {
        prefix: (0, locale_1.t)('Total'),
        label: (0, locale_1.t)('Occurrences'),
        field: types_1.SpanSortOthers.COUNT,
    },
];
const DEFAULT_SORT = types_1.SpanSortOthers.SUM_EXCLUSIVE_TIME;
function getSuspectSpanSort(sort) {
    const selected = exports.SPAN_SORT_OPTIONS.find(option => option.field === sort);
    if (selected) {
        return selected;
    }
    return exports.SPAN_SORT_OPTIONS.find(option => option.field === DEFAULT_SORT);
}
function getSuspectSpanSortFromLocation(location) {
    var _a, _b;
    const sort = (_b = (0, queryString_1.decodeScalar)((_a = location === null || location === void 0 ? void 0 : location.query) === null || _a === void 0 ? void 0 : _a.sort)) !== null && _b !== void 0 ? _b : DEFAULT_SORT;
    return getSuspectSpanSort(sort);
}
exports.getSuspectSpanSortFromLocation = getSuspectSpanSortFromLocation;
function getSuspectSpanSortFromEventView(eventView) {
    const sort = eventView.sorts.length ? eventView.sorts[0].field : DEFAULT_SORT;
    return getSuspectSpanSort(sort);
}
exports.getSuspectSpanSortFromEventView = getSuspectSpanSortFromEventView;
//# sourceMappingURL=utils.jsx.map