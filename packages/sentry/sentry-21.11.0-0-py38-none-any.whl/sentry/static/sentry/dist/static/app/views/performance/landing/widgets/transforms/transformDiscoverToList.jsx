Object.defineProperty(exports, "__esModule", { value: true });
exports.transformDiscoverToList = void 0;
const getParams_1 = require("app/components/organizations/globalSelectionHeader/getParams");
const utils_1 = require("app/utils");
const data_1 = require("app/views/performance/data");
function transformDiscoverToList(widgetProps, results, _) {
    var _a, _b;
    const { start, end, utc, interval, statsPeriod } = (0, getParams_1.getParams)(widgetProps.location.query, {
        defaultStatsPeriod: data_1.DEFAULT_STATS_PERIOD,
    });
    const data = (_b = (_a = results.tableData) === null || _a === void 0 ? void 0 : _a.data) !== null && _b !== void 0 ? _b : [];
    const childData = Object.assign(Object.assign({}, results), { isErrored: !!results.error, hasData: (0, utils_1.defined)(data) && !!data.length, data, utc: utc === 'true', interval, statsPeriod: statsPeriod !== null && statsPeriod !== void 0 ? statsPeriod : undefined, start: start !== null && start !== void 0 ? start : '', end: end !== null && end !== void 0 ? end : '' });
    return childData;
}
exports.transformDiscoverToList = transformDiscoverToList;
//# sourceMappingURL=transformDiscoverToList.jsx.map