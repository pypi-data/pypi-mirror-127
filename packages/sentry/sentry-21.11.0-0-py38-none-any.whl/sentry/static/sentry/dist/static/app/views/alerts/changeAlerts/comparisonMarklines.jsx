Object.defineProperty(exports, "__esModule", { value: true });
exports.getComparisonMarkLines = exports.checkChangeStatus = void 0;
const tslib_1 = require("tslib");
const markLine_1 = (0, tslib_1.__importDefault)(require("app/components/charts/components/markLine"));
const locale_1 = require("app/locale");
const formatters_1 = require("app/utils/formatters");
const theme_1 = (0, tslib_1.__importDefault)(require("app/utils/theme"));
const types_1 = require("app/views/alerts/incidentRules/types");
const checkChangeStatus = (value, thresholdType, triggers) => {
    const criticalTrigger = triggers === null || triggers === void 0 ? void 0 : triggers.find(trig => trig.label === 'critical');
    const warningTrigger = triggers === null || triggers === void 0 ? void 0 : triggers.find(trig => trig.label === 'warning');
    const criticalTriggerAlertThreshold = typeof (criticalTrigger === null || criticalTrigger === void 0 ? void 0 : criticalTrigger.alertThreshold) === 'number'
        ? criticalTrigger.alertThreshold
        : undefined;
    const warningTriggerAlertThreshold = typeof (warningTrigger === null || warningTrigger === void 0 ? void 0 : warningTrigger.alertThreshold) === 'number'
        ? warningTrigger.alertThreshold
        : undefined;
    // Need to catch the critical threshold cases before warning threshold cases
    if (thresholdType === types_1.AlertRuleThresholdType.ABOVE &&
        criticalTriggerAlertThreshold &&
        value >= criticalTriggerAlertThreshold) {
        return 'critical';
    }
    if (thresholdType === types_1.AlertRuleThresholdType.ABOVE &&
        warningTriggerAlertThreshold &&
        value >= warningTriggerAlertThreshold) {
        return 'warning';
    }
    // When threshold is below(lower than in comparison alerts) the % diff value is negative
    // It crosses the threshold if its abs value is greater than threshold
    // -80% change crosses below 60% threshold -1 * (-80) > 60
    if (thresholdType === types_1.AlertRuleThresholdType.BELOW &&
        criticalTriggerAlertThreshold &&
        -1 * value >= criticalTriggerAlertThreshold) {
        return 'critical';
    }
    if (thresholdType === types_1.AlertRuleThresholdType.BELOW &&
        warningTriggerAlertThreshold &&
        -1 * value >= warningTriggerAlertThreshold) {
        return 'warning';
    }
    return '';
};
exports.checkChangeStatus = checkChangeStatus;
const getComparisonMarkLines = (timeseriesData = [], comparisonTimeseriesData = [], timeWindow, triggers, thresholdType) => {
    var _a, _b;
    const changeStatuses = [];
    if (((_a = timeseriesData === null || timeseriesData === void 0 ? void 0 : timeseriesData[0]) === null || _a === void 0 ? void 0 : _a.data) !== undefined &&
        timeseriesData[0].data.length > 1 &&
        ((_b = comparisonTimeseriesData === null || comparisonTimeseriesData === void 0 ? void 0 : comparisonTimeseriesData[0]) === null || _b === void 0 ? void 0 : _b.data) !== undefined &&
        comparisonTimeseriesData[0].data.length > 1) {
        const changeData = comparisonTimeseriesData[0].data;
        const baseData = timeseriesData[0].data;
        if (triggers.some(({ alertThreshold }) => typeof alertThreshold === 'number')) {
            const lastPointLimit = baseData[changeData.length - 1].name - timeWindow * formatters_1.MINUTE;
            changeData.forEach(({ name, value: comparisonValue }, idx) => {
                const baseValue = baseData[idx].value;
                const comparisonPercentage = comparisonValue === 0
                    ? baseValue === 0
                        ? 0
                        : Infinity
                    : ((baseValue - comparisonValue) / comparisonValue) * 100;
                const status = (0, exports.checkChangeStatus)(comparisonPercentage, thresholdType, triggers);
                if (idx === 0 ||
                    idx === changeData.length - 1 ||
                    status !== changeStatuses[changeStatuses.length - 1].status) {
                    changeStatuses.push({ name, status });
                }
            });
            return changeStatuses.slice(0, -1).map(({ name, status }, idx) => ({
                seriesName: (0, locale_1.t)('status'),
                type: 'line',
                markLine: (0, markLine_1.default)({
                    silent: true,
                    lineStyle: {
                        color: status === 'critical'
                            ? theme_1.default.red300
                            : status === 'warning'
                                ? theme_1.default.yellow300
                                : theme_1.default.green300,
                        type: 'solid',
                        width: 4,
                    },
                    data: [
                        [
                            { coord: [name, 0] },
                            {
                                coord: [
                                    Math.min(changeStatuses[idx + 1].name, lastPointLimit),
                                    0,
                                ],
                            },
                        ],
                    ],
                }),
                data: [],
            }));
        }
    }
    return [];
};
exports.getComparisonMarkLines = getComparisonMarkLines;
//# sourceMappingURL=comparisonMarklines.jsx.map