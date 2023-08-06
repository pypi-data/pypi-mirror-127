Object.defineProperty(exports, "__esModule", { value: true });
exports.transformEventsRequestToVitals = void 0;
const getParams_1 = require("app/components/organizations/globalSelectionHeader/getParams");
const utils_1 = require("app/utils");
function transformEventsRequestToVitals(widgetProps, results, _) {
    var _a;
    const { start, end, utc, interval, statsPeriod } = (0, getParams_1.getParams)(widgetProps.location.query);
    const data = (_a = results.results) !== null && _a !== void 0 ? _a : [];
    const childData = Object.assign(Object.assign({}, results), { isLoading: results.loading, isErrored: results.errored, hasData: (0, utils_1.defined)(data) && !!data.length && !!data[0].data.length, data, utc: utc === 'true', interval, statsPeriod: statsPeriod !== null && statsPeriod !== void 0 ? statsPeriod : undefined, start: start !== null && start !== void 0 ? start : '', end: end !== null && end !== void 0 ? end : '' });
    return childData;
}
exports.transformEventsRequestToVitals = transformEventsRequestToVitals;
//# sourceMappingURL=transformEventsToVitals.jsx.map