Object.defineProperty(exports, "__esModule", { value: true });
exports.HistogramWidget = void 0;
const tslib_1 = require("tslib");
const react_1 = require("react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const locale_1 = require("app/locale");
const histogramQuery_1 = (0, tslib_1.__importDefault)(require("app/utils/performance/histogram/histogramQuery"));
const histogramChart_1 = require("app/views/performance/landing/chart/histogramChart");
const performanceWidget_1 = require("../components/performanceWidget");
const transformHistogramQuery_1 = require("../transforms/transformHistogramQuery");
function HistogramWidget(props) {
    const { ContainerActions, location } = props;
    const globalSelection = props.eventView.getGlobalSelection();
    const Queries = (0, react_1.useMemo)(() => {
        return {
            chart: {
                fields: props.fields,
                component: provided => (<histogramQuery_1.default {...provided} eventView={props.eventView} location={props.location} numBuckets={20} dataFilter="exclude_outliers"/>),
                transform: transformHistogramQuery_1.transformHistogramQuery,
            },
        };
    }, [props.eventView, props.fields[0], props.organization.slug]);
    const onFilterChange = () => { };
    return (<performanceWidget_1.GenericPerformanceWidget {...props} Subtitle={() => (<Subtitle>{(0, locale_1.t)('Compared to last %s ', globalSelection.datetime.period)}</Subtitle>)} HeaderActions={provided => (<react_1.Fragment>
          <ContainerActions {...provided.widgetData.chart}/>
        </react_1.Fragment>)} Queries={Queries} Visualizations={[
            {
                component: provided => {
                    var _a, _b;
                    return (<histogramChart_1.Chart {...provided} colors={props.chartColor ? [props.chartColor] : undefined} height={100} location={location} isLoading={false} isErrored={false} onFilterChange={onFilterChange} field={props.fields[0]} chartData={(_b = (_a = provided.widgetData.chart) === null || _a === void 0 ? void 0 : _a.data) === null || _b === void 0 ? void 0 : _b[props.fields[0]]} disableXAxis disableZoom/>);
                },
                height: 160,
            },
        ]}/>);
}
exports.HistogramWidget = HistogramWidget;
const Subtitle = (0, styled_1.default)('span') `
  color: ${p => p.theme.gray300};
  font-size: ${p => p.theme.fontSizeMedium};
`;
//# sourceMappingURL=histogramWidget.jsx.map