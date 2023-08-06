Object.defineProperty(exports, "__esModule", { value: true });
exports.DataDisplay = exports.GenericPerformanceWidget = void 0;
const tslib_1 = require("tslib");
const react_1 = require("react");
const react_router_1 = require("react-router");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const errorPanel_1 = (0, tslib_1.__importDefault)(require("app/components/charts/errorPanel"));
const placeholder_1 = (0, tslib_1.__importDefault)(require("app/components/placeholder"));
const iconWarning_1 = require("app/icons/iconWarning");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const trackAdvancedAnalyticsEvent_1 = (0, tslib_1.__importDefault)(require("app/utils/analytics/trackAdvancedAnalyticsEvent"));
const useApi_1 = (0, tslib_1.__importDefault)(require("app/utils/useApi"));
const performanceWidgetContainer_1 = (0, tslib_1.__importDefault)(require("app/views/performance/landing/widgets/components/performanceWidgetContainer"));
const dataStateSwitch_1 = require("./dataStateSwitch");
const queryHandler_1 = require("./queryHandler");
const widgetHeader_1 = require("./widgetHeader");
// Generic performance widget for type T, where T defines all the data contained in the widget.
function GenericPerformanceWidget(props) {
    var _a;
    // Use object keyed to chart setting so switching between charts of a similar type doesn't retain data with query components still having inflight requests.
    const [allWidgetData, setWidgetData] = (0, react_1.useState)({});
    const widgetData = (_a = allWidgetData[props.chartSetting]) !== null && _a !== void 0 ? _a : {};
    const widgetDataRef = (0, react_1.useRef)(widgetData);
    const setWidgetDataForKey = (0, react_1.useCallback)((dataKey, result) => {
        const _widgetData = widgetDataRef.current;
        const newWidgetData = Object.assign(Object.assign({}, _widgetData), { [dataKey]: result });
        widgetDataRef.current = newWidgetData;
        setWidgetData({ [props.chartSetting]: newWidgetData });
    }, [allWidgetData, setWidgetData]);
    const removeWidgetDataForKey = (0, react_1.useCallback)((dataKey) => {
        const _widgetData = widgetDataRef.current;
        const newWidgetData = Object.assign({}, _widgetData);
        delete newWidgetData[dataKey];
        widgetDataRef.current = newWidgetData;
        setWidgetData({ [props.chartSetting]: newWidgetData });
    }, [allWidgetData, setWidgetData]);
    const widgetProps = { widgetData, setWidgetDataForKey, removeWidgetDataForKey };
    const queries = Object.entries(props.Queries).map(([key, definition]) => (Object.assign(Object.assign({}, definition), { queryKey: key })));
    const api = (0, useApi_1.default)();
    const totalHeight = props.Visualizations.reduce((acc, curr) => acc + curr.height, 0);
    return (<react_1.Fragment>
      <queryHandler_1.QueryHandler widgetData={widgetData} setWidgetDataForKey={setWidgetDataForKey} removeWidgetDataForKey={removeWidgetDataForKey} queryProps={props} queries={queries} api={api}/>
      <_DataDisplay {...props} {...widgetProps} totalHeight={totalHeight}/>
    </react_1.Fragment>);
}
exports.GenericPerformanceWidget = GenericPerformanceWidget;
function trackDataComponentClicks(chartSetting, organization) {
    (0, trackAdvancedAnalyticsEvent_1.default)('performance_views.landingv3.widget.interaction', {
        organization,
        widget_type: chartSetting,
    });
}
function _DataDisplay(props) {
    const { Visualizations, chartHeight, totalHeight, containerType, EmptyComponent } = props;
    const Container = (0, performanceWidgetContainer_1.default)({
        containerType,
    });
    const numberKeys = Object.keys(props.Queries).length;
    const missingDataKeys = Object.values(props.widgetData).length !== numberKeys;
    const hasData = !missingDataKeys && Object.values(props.widgetData).every(d => !d || d.hasData);
    const isLoading = Object.values(props.widgetData).some(d => !d || d.isLoading);
    const isErrored = !missingDataKeys && Object.values(props.widgetData).some(d => d && d.isErrored);
    const paddingOffset = 32; // space(2) * 2;
    return (<Container data-test-id="performance-widget-container">
      <ContentContainer>
        <widgetHeader_1.WidgetHeader {...props}/>
      </ContentContainer>
      <dataStateSwitch_1.DataStateSwitch isLoading={isLoading} isErrored={isErrored} hasData={hasData} errorComponent={<DefaultErrorComponent height={totalHeight - paddingOffset}/>} dataComponents={Visualizations.map((Visualization, index) => (<ContentContainer key={index} noPadding={Visualization.noPadding} bottomPadding={Visualization.bottomPadding} onClick={() => trackDataComponentClicks(props.chartSetting, props.organization)}>
            <Visualization.component grid={defaultGrid} queryFields={Visualization.fields} widgetData={props.widgetData} height={chartHeight}/>
          </ContentContainer>))} loadingComponent={<placeholder_1.default height={`${totalHeight - paddingOffset}px`}/>} emptyComponent={EmptyComponent ? (<EmptyComponent />) : (<placeholder_1.default height={`${totalHeight - paddingOffset}px`}/>)}/>
    </Container>);
}
exports.DataDisplay = (0, react_router_1.withRouter)(_DataDisplay);
const DefaultErrorComponent = (props) => {
    return (<errorPanel_1.default height={`${props.height}px`}>
      <iconWarning_1.IconWarning color="gray300" size="lg"/>
    </errorPanel_1.default>);
};
const defaultGrid = {
    left: (0, space_1.default)(0),
    right: (0, space_1.default)(0),
    top: (0, space_1.default)(2),
    bottom: (0, space_1.default)(0),
};
const ContentContainer = (0, styled_1.default)('div') `
  padding-left: ${p => (p.noPadding ? (0, space_1.default)(0) : (0, space_1.default)(2))};
  padding-right: ${p => (p.noPadding ? (0, space_1.default)(0) : (0, space_1.default)(2))};
  padding-bottom: ${p => (p.bottomPadding ? (0, space_1.default)(1) : (0, space_1.default)(0))};
`;
GenericPerformanceWidget.defaultProps = {
    containerType: 'panel',
    chartHeight: 200,
};
//# sourceMappingURL=performanceWidget.jsx.map