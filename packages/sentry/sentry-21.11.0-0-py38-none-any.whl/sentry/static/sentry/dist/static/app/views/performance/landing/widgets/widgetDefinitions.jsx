Object.defineProperty(exports, "__esModule", { value: true });
exports.WIDGET_DEFINITIONS = exports.PerformanceWidgetSetting = void 0;
const tslib_1 = require("tslib");
const chartPalette_1 = (0, tslib_1.__importDefault)(require("app/constants/chartPalette"));
const locale_1 = require("app/locale");
const data_1 = require("../../data");
const types_1 = require("./types");
var PerformanceWidgetSetting;
(function (PerformanceWidgetSetting) {
    PerformanceWidgetSetting["DURATION_HISTOGRAM"] = "duration_histogram";
    PerformanceWidgetSetting["LCP_HISTOGRAM"] = "lcp_histogram";
    PerformanceWidgetSetting["FCP_HISTOGRAM"] = "fcp_histogram";
    PerformanceWidgetSetting["FID_HISTOGRAM"] = "fid_histogram";
    PerformanceWidgetSetting["APDEX_AREA"] = "apdex_area";
    PerformanceWidgetSetting["P50_DURATION_AREA"] = "p50_duration_area";
    PerformanceWidgetSetting["P75_DURATION_AREA"] = "p75_duration_area";
    PerformanceWidgetSetting["P95_DURATION_AREA"] = "p95_duration_area";
    PerformanceWidgetSetting["P99_DURATION_AREA"] = "p99_duration_area";
    PerformanceWidgetSetting["P75_LCP_AREA"] = "p75_lcp_area";
    PerformanceWidgetSetting["TPM_AREA"] = "tpm_area";
    PerformanceWidgetSetting["FAILURE_RATE_AREA"] = "failure_rate_area";
    PerformanceWidgetSetting["USER_MISERY_AREA"] = "user_misery_area";
    PerformanceWidgetSetting["WORST_LCP_VITALS"] = "worst_lcp_vitals";
    PerformanceWidgetSetting["WORST_FCP_VITALS"] = "worst_fcp_vitals";
    PerformanceWidgetSetting["WORST_CLS_VITALS"] = "worst_cls_vitals";
    PerformanceWidgetSetting["WORST_FID_VITALS"] = "worst_fid_vitals";
    PerformanceWidgetSetting["MOST_IMPROVED"] = "most_improved";
    PerformanceWidgetSetting["MOST_REGRESSED"] = "most_regressed";
    PerformanceWidgetSetting["MOST_RELATED_ERRORS"] = "most_related_errors";
    PerformanceWidgetSetting["MOST_RELATED_ISSUES"] = "most_related_issues";
    PerformanceWidgetSetting["SLOW_HTTP_OPS"] = "slow_http_ops";
    PerformanceWidgetSetting["SLOW_DB_OPS"] = "slow_db_ops";
    PerformanceWidgetSetting["SLOW_RESOURCE_OPS"] = "slow_resource_ops";
    PerformanceWidgetSetting["SLOW_BROWSER_OPS"] = "slow_browser_ops";
    PerformanceWidgetSetting["COLD_STARTUP_AREA"] = "cold_startup_area";
    PerformanceWidgetSetting["WARM_STARTUP_AREA"] = "warm_startup_area";
    PerformanceWidgetSetting["SLOW_FRAMES_AREA"] = "slow_frames_area";
    PerformanceWidgetSetting["FROZEN_FRAMES_AREA"] = "frozen_frames_area";
    PerformanceWidgetSetting["MOST_SLOW_FRAMES"] = "most_slow_frames";
    PerformanceWidgetSetting["MOST_FROZEN_FRAMES"] = "most_frozen_frames";
})(PerformanceWidgetSetting = exports.PerformanceWidgetSetting || (exports.PerformanceWidgetSetting = {}));
const WIDGET_PALETTE = chartPalette_1.default[5];
const WIDGET_DEFINITIONS = ({ organization, }) => {
    var _a;
    return ({
        [PerformanceWidgetSetting.DURATION_HISTOGRAM]: {
            title: (0, locale_1.t)('Duration Distribution'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.DURATION_DISTRIBUTION),
            fields: ['transaction.duration'],
            dataType: types_1.GenericPerformanceWidgetDataType.histogram,
            chartColor: WIDGET_PALETTE[5],
        },
        [PerformanceWidgetSetting.LCP_HISTOGRAM]: {
            title: (0, locale_1.t)('LCP Distribution'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.DURATION_DISTRIBUTION),
            fields: ['measurements.lcp'],
            dataType: types_1.GenericPerformanceWidgetDataType.histogram,
            chartColor: WIDGET_PALETTE[5],
        },
        [PerformanceWidgetSetting.FCP_HISTOGRAM]: {
            title: (0, locale_1.t)('FCP Distribution'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.DURATION_DISTRIBUTION),
            fields: ['measurements.fcp'],
            dataType: types_1.GenericPerformanceWidgetDataType.histogram,
            chartColor: WIDGET_PALETTE[5],
        },
        [PerformanceWidgetSetting.FID_HISTOGRAM]: {
            title: (0, locale_1.t)('FID Distribution'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.DURATION_DISTRIBUTION),
            fields: ['measurements.fid'],
            dataType: types_1.GenericPerformanceWidgetDataType.histogram,
            chartColor: WIDGET_PALETTE[5],
        },
        [PerformanceWidgetSetting.WORST_LCP_VITALS]: {
            title: (0, locale_1.t)('Worst LCP Web Vitals'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.LCP),
            fields: ['measurements.lcp'],
            vitalStops: {
                poor: 4000,
                meh: 2500,
            },
            dataType: types_1.GenericPerformanceWidgetDataType.vitals,
        },
        [PerformanceWidgetSetting.WORST_FCP_VITALS]: {
            title: (0, locale_1.t)('Worst FCP Web Vitals'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.FCP),
            fields: ['measurements.fcp'],
            vitalStops: {
                poor: 3000,
                meh: 1000,
            },
            dataType: types_1.GenericPerformanceWidgetDataType.vitals,
        },
        [PerformanceWidgetSetting.WORST_FID_VITALS]: {
            title: (0, locale_1.t)('Worst FID Web Vitals'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.FID),
            fields: ['measurements.fid'],
            vitalStops: {
                poor: 300,
                meh: 100,
            },
            dataType: types_1.GenericPerformanceWidgetDataType.vitals,
        },
        [PerformanceWidgetSetting.WORST_CLS_VITALS]: {
            title: (0, locale_1.t)('Worst CLS Web Vitals'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.CLS),
            fields: ['measurements.cls'],
            vitalStops: {
                poor: 0.25,
                meh: 0.1,
            },
            dataType: types_1.GenericPerformanceWidgetDataType.vitals,
        },
        [PerformanceWidgetSetting.TPM_AREA]: {
            title: (0, locale_1.t)('Transactions Per Minute'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.TPM),
            fields: ['tpm()'],
            dataType: types_1.GenericPerformanceWidgetDataType.area,
            chartColor: WIDGET_PALETTE[1],
        },
        [PerformanceWidgetSetting.APDEX_AREA]: {
            title: (0, locale_1.t)('Apdex'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.APDEX_NEW),
            fields: ['apdex()'],
            dataType: types_1.GenericPerformanceWidgetDataType.area,
            chartColor: WIDGET_PALETTE[4],
        },
        [PerformanceWidgetSetting.P50_DURATION_AREA]: {
            title: (0, locale_1.t)('p50 Duration'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.P50),
            fields: ['p50(transaction.duration)'],
            dataType: types_1.GenericPerformanceWidgetDataType.area,
            chartColor: WIDGET_PALETTE[3],
        },
        [PerformanceWidgetSetting.P75_DURATION_AREA]: {
            title: (0, locale_1.t)('p75 Duration'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.P75),
            fields: ['p75(transaction.duration)'],
            dataType: types_1.GenericPerformanceWidgetDataType.area,
            chartColor: WIDGET_PALETTE[3],
        },
        [PerformanceWidgetSetting.P95_DURATION_AREA]: {
            title: (0, locale_1.t)('p95 Duration'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.P95),
            fields: ['p95(transaction.duration)'],
            dataType: types_1.GenericPerformanceWidgetDataType.area,
            chartColor: WIDGET_PALETTE[3],
        },
        [PerformanceWidgetSetting.P99_DURATION_AREA]: {
            title: (0, locale_1.t)('p99 Duration'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.P99),
            fields: ['p99(transaction.duration)'],
            dataType: types_1.GenericPerformanceWidgetDataType.area,
            chartColor: WIDGET_PALETTE[3],
        },
        [PerformanceWidgetSetting.P75_LCP_AREA]: {
            title: (0, locale_1.t)('p75 LCP'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.P75),
            fields: ['p75(measurements.lcp)'],
            dataType: types_1.GenericPerformanceWidgetDataType.area,
            chartColor: WIDGET_PALETTE[1],
        },
        [PerformanceWidgetSetting.FAILURE_RATE_AREA]: {
            title: (0, locale_1.t)('Failure Rate'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.FAILURE_RATE),
            fields: ['failure_rate()'],
            dataType: types_1.GenericPerformanceWidgetDataType.area,
            chartColor: WIDGET_PALETTE[2],
        },
        [PerformanceWidgetSetting.USER_MISERY_AREA]: {
            title: (0, locale_1.t)('User Misery'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.USER_MISERY),
            fields: [`user_misery(${(_a = organization.apdexThreshold) !== null && _a !== void 0 ? _a : ''})`],
            dataType: types_1.GenericPerformanceWidgetDataType.area,
            chartColor: WIDGET_PALETTE[0],
        },
        [PerformanceWidgetSetting.COLD_STARTUP_AREA]: {
            title: (0, locale_1.t)('Cold Startup Time'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.APP_START_COLD),
            fields: ['p75(measurements.app_start_cold)'],
            dataType: types_1.GenericPerformanceWidgetDataType.area,
            chartColor: WIDGET_PALETTE[4],
        },
        [PerformanceWidgetSetting.WARM_STARTUP_AREA]: {
            title: (0, locale_1.t)('Warm Startup Time'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.APP_START_WARM),
            fields: ['p75(measurements.app_start_warm)'],
            dataType: types_1.GenericPerformanceWidgetDataType.area,
            chartColor: WIDGET_PALETTE[3],
        },
        [PerformanceWidgetSetting.SLOW_FRAMES_AREA]: {
            title: (0, locale_1.t)('Slow Frames'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.SLOW_FRAMES),
            fields: ['p75(measurements.frames_slow_rate)'],
            dataType: types_1.GenericPerformanceWidgetDataType.area,
            chartColor: WIDGET_PALETTE[0],
        },
        [PerformanceWidgetSetting.FROZEN_FRAMES_AREA]: {
            title: (0, locale_1.t)('Frozen Frames'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.FROZEN_FRAMES),
            fields: ['p75(measurements.frames_frozen_rate)'],
            dataType: types_1.GenericPerformanceWidgetDataType.area,
            chartColor: WIDGET_PALETTE[5],
        },
        [PerformanceWidgetSetting.MOST_RELATED_ERRORS]: {
            title: (0, locale_1.t)('Most Related Errors'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.MOST_ERRORS),
            fields: [`failure_count()`],
            dataType: types_1.GenericPerformanceWidgetDataType.line_list,
            chartColor: WIDGET_PALETTE[0],
        },
        [PerformanceWidgetSetting.MOST_RELATED_ISSUES]: {
            title: (0, locale_1.t)('Most Related Issues'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.MOST_ISSUES),
            fields: [`count()`],
            dataType: types_1.GenericPerformanceWidgetDataType.line_list,
            chartColor: WIDGET_PALETTE[0],
        },
        [PerformanceWidgetSetting.SLOW_HTTP_OPS]: {
            title: (0, locale_1.t)('Slow HTTP Ops'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.SLOW_HTTP_SPANS),
            fields: [`p75(spans.http)`],
            dataType: types_1.GenericPerformanceWidgetDataType.line_list,
            chartColor: WIDGET_PALETTE[0],
        },
        [PerformanceWidgetSetting.SLOW_BROWSER_OPS]: {
            title: (0, locale_1.t)('Slow Browser Ops'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.SLOW_HTTP_SPANS),
            fields: [`p75(spans.browser)`],
            dataType: types_1.GenericPerformanceWidgetDataType.line_list,
            chartColor: WIDGET_PALETTE[0],
        },
        [PerformanceWidgetSetting.SLOW_RESOURCE_OPS]: {
            title: (0, locale_1.t)('Slow Resource Ops'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.SLOW_HTTP_SPANS),
            fields: [`p75(spans.resource)`],
            dataType: types_1.GenericPerformanceWidgetDataType.line_list,
            chartColor: WIDGET_PALETTE[0],
        },
        [PerformanceWidgetSetting.SLOW_DB_OPS]: {
            title: (0, locale_1.t)('Slow DB Ops'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.SLOW_HTTP_SPANS),
            fields: [`p75(spans.db)`],
            dataType: types_1.GenericPerformanceWidgetDataType.line_list,
            chartColor: WIDGET_PALETTE[0],
        },
        [PerformanceWidgetSetting.MOST_SLOW_FRAMES]: {
            title: (0, locale_1.t)('Most Slow Frames'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.SLOW_FRAMES),
            fields: ['p75(measurements.frames_slow_rate)'],
            dataType: types_1.GenericPerformanceWidgetDataType.line_list,
            chartColor: WIDGET_PALETTE[0],
        },
        [PerformanceWidgetSetting.MOST_FROZEN_FRAMES]: {
            title: (0, locale_1.t)('Most Frozen Frames'),
            titleTooltip: (0, data_1.getTermHelp)(organization, data_1.PERFORMANCE_TERM.FROZEN_FRAMES),
            fields: ['p75(measurements.frames_frozen_rate)'],
            dataType: types_1.GenericPerformanceWidgetDataType.line_list,
            chartColor: WIDGET_PALETTE[0],
        },
        [PerformanceWidgetSetting.MOST_IMPROVED]: {
            title: (0, locale_1.t)('Most Improved'),
            titleTooltip: (0, locale_1.t)('This compares the baseline (%s) of the past with the present.', 'improved'),
            fields: [],
            dataType: types_1.GenericPerformanceWidgetDataType.trends,
        },
        [PerformanceWidgetSetting.MOST_REGRESSED]: {
            title: (0, locale_1.t)('Most Regressed'),
            titleTooltip: (0, locale_1.t)('This compares the baseline (%s) of the past with the present.', 'regressed'),
            fields: [],
            dataType: types_1.GenericPerformanceWidgetDataType.trends,
        },
    });
};
exports.WIDGET_DEFINITIONS = WIDGET_DEFINITIONS;
//# sourceMappingURL=widgetDefinitions.jsx.map