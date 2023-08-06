Object.defineProperty(exports, "__esModule", { value: true });
exports.Chart = exports.HistogramChart = void 0;
const tslib_1 = require("tslib");
const react_1 = require("react");
const react_2 = require("@emotion/react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const barChart_1 = (0, tslib_1.__importDefault)(require("app/components/charts/barChart"));
const barChartZoom_1 = (0, tslib_1.__importDefault)(require("app/components/charts/barChartZoom"));
const errorPanel_1 = (0, tslib_1.__importDefault)(require("app/components/charts/errorPanel"));
const styles_1 = require("app/components/charts/styles");
const transparentLoadingMask_1 = (0, tslib_1.__importDefault)(require("app/components/charts/transparentLoadingMask"));
const placeholder_1 = (0, tslib_1.__importDefault)(require("app/components/placeholder"));
const questionTooltip_1 = (0, tslib_1.__importDefault)(require("app/components/questionTooltip"));
const iconWarning_1 = require("app/icons/iconWarning");
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const getDynamicText_1 = (0, tslib_1.__importDefault)(require("app/utils/getDynamicText"));
const histogramQuery_1 = (0, tslib_1.__importDefault)(require("app/utils/performance/histogram/histogramQuery"));
const utils_1 = require("app/utils/performance/histogram/utils");
const styles_2 = require("../../styles");
const utils_2 = require("../display/utils");
const NUM_BUCKETS = 50;
const PRECISION = 0;
function HistogramChart(props) {
    const { location, onFilterChange, organization, eventView, field, title, titleTooltip, didReceiveMultiAxis, backupField, usingBackupAxis, } = props;
    const _backupField = backupField ? [backupField] : [];
    return (<div>
      <styles_2.DoubleHeaderContainer>
        <styles_1.HeaderTitleLegend>
          {title}
          <questionTooltip_1.default position="top" size="sm" title={titleTooltip}/>
        </styles_1.HeaderTitleLegend>
      </styles_2.DoubleHeaderContainer>
      <histogramQuery_1.default location={location} orgSlug={organization.slug} eventView={eventView} numBuckets={NUM_BUCKETS} precision={PRECISION} fields={[field, ..._backupField]} dataFilter="exclude_outliers" didReceiveMultiAxis={didReceiveMultiAxis}>
        {results => {
            var _a;
            const _field = usingBackupAxis ? (0, utils_2.getFieldOrBackup)(field, backupField) : field;
            const isLoading = results.isLoading;
            const isErrored = results.error !== null;
            const chartData = (_a = results.histograms) === null || _a === void 0 ? void 0 : _a[_field];
            if (isErrored) {
                return (<errorPanel_1.default height="250px">
                <iconWarning_1.IconWarning color="gray300" size="lg"/>
              </errorPanel_1.default>);
            }
            if (!chartData) {
                return null;
            }
            return (<Chart isLoading={isLoading} isErrored={isErrored} chartData={chartData} location={location} onFilterChange={onFilterChange} field={_field}/>);
        }}
      </histogramQuery_1.default>
    </div>);
}
exports.HistogramChart = HistogramChart;
function Chart(props) {
    const { isLoading, isErrored, chartData, location, field, onFilterChange, height, grid, disableXAxis, disableZoom, colors, } = props;
    if (!chartData) {
        return null;
    }
    const theme = (0, react_2.useTheme)();
    const series = {
        seriesName: (0, locale_1.t)('Count'),
        data: (0, utils_1.formatHistogramData)(chartData, { type: 'duration' }),
    };
    const xAxis = {
        type: 'category',
        truncate: true,
        boundaryGap: false,
        axisTick: {
            alignWithLabel: true,
        },
    };
    const allSeries = [];
    if (!isLoading && !isErrored) {
        allSeries.push(series);
    }
    const yAxis = {
        type: 'value',
        axisLabel: {
            color: theme.chartLabel,
        },
    };
    return (<react_1.Fragment>
      <barChartZoom_1.default minZoomWidth={Math.pow(10, -PRECISION) * NUM_BUCKETS} location={location} paramStart={`${field}:>=`} paramEnd={`${field}:<=`} xAxisIndex={[0]} buckets={(0, utils_1.computeBuckets)(chartData)} onHistoryPush={onFilterChange}>
        {zoomRenderProps => {
            return (<BarChartContainer>
              <MaskContainer>
                <transparentLoadingMask_1.default visible={isLoading}/>
                {(0, getDynamicText_1.default)({
                    value: (<barChart_1.default height={height !== null && height !== void 0 ? height : 250} series={allSeries} xAxis={disableXAxis ? { show: false } : xAxis} yAxis={yAxis} colors={colors} grid={grid !== null && grid !== void 0 ? grid : {
                            left: (0, space_1.default)(3),
                            right: (0, space_1.default)(3),
                            top: (0, space_1.default)(3),
                            bottom: isLoading ? (0, space_1.default)(4) : (0, space_1.default)(1.5),
                        }} stacked {...(disableZoom ? {} : zoomRenderProps)}/>),
                    fixed: <placeholder_1.default height="250px" testId="skeleton-ui"/>,
                })}
              </MaskContainer>
            </BarChartContainer>);
        }}
      </barChartZoom_1.default>
    </react_1.Fragment>);
}
exports.Chart = Chart;
const BarChartContainer = (0, styled_1.default)('div') `
  padding-top: ${(0, space_1.default)(1)};
  position: relative;
`;
const MaskContainer = (0, styled_1.default)('div') `
  position: relative;
`;
exports.default = HistogramChart;
//# sourceMappingURL=histogramChart.jsx.map