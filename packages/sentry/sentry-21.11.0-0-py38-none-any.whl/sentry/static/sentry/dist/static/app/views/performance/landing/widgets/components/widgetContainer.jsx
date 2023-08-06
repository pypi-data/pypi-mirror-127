Object.defineProperty(exports, "__esModule", { value: true });
exports.WidgetContainerActions = void 0;
const tslib_1 = require("tslib");
const react_1 = require("react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const menuItem_1 = (0, tslib_1.__importDefault)(require("app/components/menuItem"));
const locale_1 = require("app/locale");
const trackAdvancedAnalyticsEvent_1 = (0, tslib_1.__importDefault)(require("app/utils/analytics/trackAdvancedAnalyticsEvent"));
const localStorage_1 = (0, tslib_1.__importDefault)(require("app/utils/localStorage"));
const performanceDisplayContext_1 = require("app/utils/performance/contexts/performanceDisplayContext");
const useOrganization_1 = (0, tslib_1.__importDefault)(require("app/utils/useOrganization"));
const withOrganization_1 = (0, tslib_1.__importDefault)(require("app/utils/withOrganization"));
const contextMenu_1 = (0, tslib_1.__importDefault)(require("app/views/dashboardsV2/contextMenu"));
const metricsSwitch_1 = require("app/views/performance/metricsSwitch");
const types_1 = require("../types");
const widgetDefinitions_1 = require("../widgetDefinitions");
const histogramWidget_1 = require("../widgets/histogramWidget");
const lineChartListWidget_1 = require("../widgets/lineChartListWidget");
const singleFieldAreaWidget_1 = require("../widgets/singleFieldAreaWidget");
const trendsWidget_1 = require("../widgets/trendsWidget");
const vitalWidget_1 = require("../widgets/vitalWidget");
// Use local storage for chart settings for now.
const getContainerLocalStorageObjectKey = 'landing-chart-container';
const getContainerKey = (index, performanceType, height) => `landing-chart-container#${performanceType}#${height}#${index}`;
function getWidgetStorageObject() {
    const localObject = JSON.parse(localStorage_1.default.getItem(getContainerLocalStorageObjectKey) || '{}');
    return localObject;
}
function setWidgetStorageObject(localObject) {
    localStorage_1.default.setItem(getContainerLocalStorageObjectKey, JSON.stringify(localObject));
}
const getChartSetting = (index, height, performanceType, defaultType, forceDefaultChartSetting // Used for testing.
) => {
    if (forceDefaultChartSetting) {
        return defaultType;
    }
    const key = getContainerKey(index, performanceType, height);
    const localObject = getWidgetStorageObject();
    const value = localObject === null || localObject === void 0 ? void 0 : localObject[key];
    if (value &&
        Object.values(widgetDefinitions_1.PerformanceWidgetSetting).includes(value)) {
        const _value = value;
        return _value;
    }
    return defaultType;
};
const _setChartSetting = (index, height, performanceType, setting) => {
    const key = getContainerKey(index, performanceType, height);
    const localObject = getWidgetStorageObject();
    localObject[key] = setting;
    setWidgetStorageObject(localObject);
};
function trackChartSettingChange(previousChartSetting, chartSetting, fromDefault, organization) {
    (0, trackAdvancedAnalyticsEvent_1.default)('performance_views.landingv3.widget.switch', {
        organization,
        from_widget: previousChartSetting,
        to_widget: chartSetting,
        from_default: fromDefault,
    });
}
const _WidgetContainer = (props) => {
    const { organization, index, chartHeight, allowedCharts } = props, rest = (0, tslib_1.__rest)(props, ["organization", "index", "chartHeight", "allowedCharts"]);
    const { isMetricsData } = (0, metricsSwitch_1.useMetricsSwitch)();
    const performanceType = (0, performanceDisplayContext_1.usePerformanceDisplayType)();
    let _chartSetting = getChartSetting(index, chartHeight, performanceType, rest.defaultChartSetting, rest.forceDefaultChartSetting);
    if (!allowedCharts.includes(_chartSetting)) {
        _chartSetting = rest.defaultChartSetting;
    }
    const [chartSetting, setChartSettingState] = (0, react_1.useState)(_chartSetting);
    const setChartSetting = (setting) => {
        if (!props.forceDefaultChartSetting) {
            _setChartSetting(index, chartHeight, performanceType, setting);
        }
        setChartSettingState(setting);
        trackChartSettingChange(chartSetting, setting, rest.defaultChartSetting === chartSetting, organization);
    };
    (0, react_1.useEffect)(() => {
        setChartSettingState(_chartSetting);
    }, [rest.defaultChartSetting]);
    const chartDefinition = (0, widgetDefinitions_1.WIDGET_DEFINITIONS)({ organization })[chartSetting];
    const widgetProps = Object.assign(Object.assign({}, chartDefinition), { chartSetting,
        chartDefinition, ContainerActions: containerProps => (<exports.WidgetContainerActions {...containerProps} allowedCharts={props.allowedCharts} setChartSetting={setChartSetting}/>) });
    if (isMetricsData) {
        return <h1>{(0, locale_1.t)('Using metrics')}</h1>;
    }
    switch (widgetProps.dataType) {
        case types_1.GenericPerformanceWidgetDataType.trends:
            return <trendsWidget_1.TrendsWidget {...props} {...widgetProps}/>;
        case types_1.GenericPerformanceWidgetDataType.area:
            return <singleFieldAreaWidget_1.SingleFieldAreaWidget {...props} {...widgetProps}/>;
        case types_1.GenericPerformanceWidgetDataType.vitals:
            return <vitalWidget_1.VitalWidget {...props} {...widgetProps}/>;
        case types_1.GenericPerformanceWidgetDataType.line_list:
            return <lineChartListWidget_1.LineChartListWidget {...props} {...widgetProps}/>;
        case types_1.GenericPerformanceWidgetDataType.histogram:
            return <histogramWidget_1.HistogramWidget {...props} {...widgetProps}/>;
        default:
            throw new Error(`Widget type "${widgetProps.dataType}" has no implementation.`);
    }
};
const WidgetContainerActions = ({ setChartSetting, allowedCharts, }) => {
    const organization = (0, useOrganization_1.default)();
    const menuOptions = [];
    const settingsMap = (0, widgetDefinitions_1.WIDGET_DEFINITIONS)({ organization });
    for (const setting of allowedCharts) {
        const options = settingsMap[setting];
        menuOptions.push(<menuItem_1.default key={setting} onClick={() => setChartSetting(setting)} data-test-id="performance-widget-menu-item">
        {options.title}
      </menuItem_1.default>);
    }
    return (<ChartActionContainer>
      <contextMenu_1.default>{menuOptions}</contextMenu_1.default>
    </ChartActionContainer>);
};
exports.WidgetContainerActions = WidgetContainerActions;
const ChartActionContainer = (0, styled_1.default)('div') `
  display: flex;
  justify-content: flex-end;
`;
const WidgetContainer = (0, withOrganization_1.default)(_WidgetContainer);
exports.default = WidgetContainer;
//# sourceMappingURL=widgetContainer.jsx.map