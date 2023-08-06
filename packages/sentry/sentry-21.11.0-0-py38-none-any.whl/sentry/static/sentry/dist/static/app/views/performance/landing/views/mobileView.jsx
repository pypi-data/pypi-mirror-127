Object.defineProperty(exports, "__esModule", { value: true });
exports.MobileView = void 0;
const tslib_1 = require("tslib");
const pageError_1 = require("app/utils/performance/contexts/pageError");
const performanceDisplayContext_1 = require("app/utils/performance/contexts/performanceDisplayContext");
const table_1 = (0, tslib_1.__importDefault)(require("../../table"));
const utils_1 = require("../../utils");
const data_1 = require("../data");
const widgetChartRow_1 = require("../widgets/components/widgetChartRow");
const widgetDefinitions_1 = require("../widgets/widgetDefinitions");
function MobileView(props) {
    return (<performanceDisplayContext_1.PerformanceDisplayProvider value={{ performanceType: utils_1.PROJECT_PERFORMANCE_TYPE.ANY }}>
      <div>
        <widgetChartRow_1.TripleChartRow {...props} allowedCharts={[
            widgetDefinitions_1.PerformanceWidgetSetting.TPM_AREA,
            widgetDefinitions_1.PerformanceWidgetSetting.COLD_STARTUP_AREA,
            widgetDefinitions_1.PerformanceWidgetSetting.WARM_STARTUP_AREA,
            widgetDefinitions_1.PerformanceWidgetSetting.SLOW_FRAMES_AREA,
            widgetDefinitions_1.PerformanceWidgetSetting.FROZEN_FRAMES_AREA,
        ]}/>
        <widgetChartRow_1.DoubleChartRow {...props} allowedCharts={[
            widgetDefinitions_1.PerformanceWidgetSetting.MOST_SLOW_FRAMES,
            widgetDefinitions_1.PerformanceWidgetSetting.MOST_FROZEN_FRAMES,
            widgetDefinitions_1.PerformanceWidgetSetting.MOST_IMPROVED,
            widgetDefinitions_1.PerformanceWidgetSetting.MOST_REGRESSED,
        ]}/>
        <table_1.default {...props} columnTitles={data_1.MOBILE_COLUMN_TITLES} // TODO(k-fish): Add react native column titles
     setError={(0, pageError_1.usePageError)().setPageError}/>
      </div>
    </performanceDisplayContext_1.PerformanceDisplayProvider>);
}
exports.MobileView = MobileView;
//# sourceMappingURL=mobileView.jsx.map