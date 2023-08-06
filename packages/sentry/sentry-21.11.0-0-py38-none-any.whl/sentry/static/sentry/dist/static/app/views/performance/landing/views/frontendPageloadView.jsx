Object.defineProperty(exports, "__esModule", { value: true });
exports.FrontendPageloadView = void 0;
const tslib_1 = require("tslib");
const pageError_1 = require("app/utils/performance/contexts/pageError");
const performanceDisplayContext_1 = require("app/utils/performance/contexts/performanceDisplayContext");
const table_1 = (0, tslib_1.__importDefault)(require("../../table"));
const utils_1 = require("../../utils");
const data_1 = require("../data");
const widgetChartRow_1 = require("../widgets/components/widgetChartRow");
const widgetDefinitions_1 = require("../widgets/widgetDefinitions");
function FrontendPageloadView(props) {
    return (<performanceDisplayContext_1.PerformanceDisplayProvider value={{ performanceType: utils_1.PROJECT_PERFORMANCE_TYPE.FRONTEND }}>
      <div data-test-id="frontend-pageload-view">
        <widgetChartRow_1.TripleChartRow {...props} allowedCharts={[
            widgetDefinitions_1.PerformanceWidgetSetting.P75_LCP_AREA,
            widgetDefinitions_1.PerformanceWidgetSetting.LCP_HISTOGRAM,
            widgetDefinitions_1.PerformanceWidgetSetting.FCP_HISTOGRAM,
            widgetDefinitions_1.PerformanceWidgetSetting.USER_MISERY_AREA,
            widgetDefinitions_1.PerformanceWidgetSetting.TPM_AREA,
        ]}/>
        <widgetChartRow_1.DoubleChartRow {...props} allowedCharts={[
            widgetDefinitions_1.PerformanceWidgetSetting.WORST_LCP_VITALS,
            widgetDefinitions_1.PerformanceWidgetSetting.WORST_FCP_VITALS,
            widgetDefinitions_1.PerformanceWidgetSetting.WORST_FID_VITALS,
            widgetDefinitions_1.PerformanceWidgetSetting.MOST_RELATED_ERRORS,
            widgetDefinitions_1.PerformanceWidgetSetting.MOST_RELATED_ISSUES,
            widgetDefinitions_1.PerformanceWidgetSetting.SLOW_HTTP_OPS,
            widgetDefinitions_1.PerformanceWidgetSetting.SLOW_BROWSER_OPS,
            widgetDefinitions_1.PerformanceWidgetSetting.SLOW_RESOURCE_OPS,
        ]}/>
        <table_1.default {...props} columnTitles={data_1.FRONTEND_PAGELOAD_COLUMN_TITLES} setError={(0, pageError_1.usePageError)().setPageError}/>
      </div>
    </performanceDisplayContext_1.PerformanceDisplayProvider>);
}
exports.FrontendPageloadView = FrontendPageloadView;
//# sourceMappingURL=frontendPageloadView.jsx.map