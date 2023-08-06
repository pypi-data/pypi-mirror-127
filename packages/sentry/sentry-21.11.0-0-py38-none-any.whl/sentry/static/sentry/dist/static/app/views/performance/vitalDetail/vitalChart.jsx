Object.defineProperty(exports, "__esModule", { value: true });
exports._VitalChart = void 0;
const tslib_1 = require("tslib");
const react_router_1 = require("react-router");
const react_1 = require("@emotion/react");
const chartZoom_1 = (0, tslib_1.__importDefault)(require("app/components/charts/chartZoom"));
const markLine_1 = (0, tslib_1.__importDefault)(require("app/components/charts/components/markLine"));
const errorPanel_1 = (0, tslib_1.__importDefault)(require("app/components/charts/errorPanel"));
const eventsRequest_1 = (0, tslib_1.__importDefault)(require("app/components/charts/eventsRequest"));
const lineChart_1 = (0, tslib_1.__importDefault)(require("app/components/charts/lineChart"));
const releaseSeries_1 = (0, tslib_1.__importDefault)(require("app/components/charts/releaseSeries"));
const styles_1 = require("app/components/charts/styles");
const transitionChart_1 = (0, tslib_1.__importDefault)(require("app/components/charts/transitionChart"));
const transparentLoadingMask_1 = (0, tslib_1.__importDefault)(require("app/components/charts/transparentLoadingMask"));
const utils_1 = require("app/components/charts/utils");
const panels_1 = require("app/components/panels");
const questionTooltip_1 = (0, tslib_1.__importDefault)(require("app/components/questionTooltip"));
const icons_1 = require("app/icons");
const locale_1 = require("app/locale");
const dates_1 = require("app/utils/dates");
const charts_1 = require("app/utils/discover/charts");
const fields_1 = require("app/utils/discover/fields");
const getDynamicText_1 = (0, tslib_1.__importDefault)(require("app/utils/getDynamicText"));
const queryString_1 = require("app/utils/queryString");
const useApi_1 = (0, tslib_1.__importDefault)(require("app/utils/useApi"));
const utils_2 = require("../trends/utils");
const utils_3 = require("./utils");
const QUERY_KEYS = [
    'environment',
    'project',
    'query',
    'start',
    'end',
    'statsPeriod',
];
function VitalChart({ project, environment, location, organization, query, statsPeriod, router, start: propsStart, end: propsEnd, }) {
    const api = (0, useApi_1.default)();
    const theme = (0, react_1.useTheme)();
    const handleLegendSelectChanged = legendChange => {
        const { selected } = legendChange;
        const unselected = Object.keys(selected).filter(key => !selected[key]);
        const to = Object.assign(Object.assign({}, location), { query: Object.assign(Object.assign({}, location.query), { unselectedSeries: unselected }) });
        react_router_1.browserHistory.push(to);
    };
    const start = propsStart ? (0, dates_1.getUtcToLocalDateObject)(propsStart) : null;
    const end = propsEnd ? (0, dates_1.getUtcToLocalDateObject)(propsEnd) : null;
    const utc = (0, queryString_1.decodeScalar)(router.location.query.utc) !== 'false';
    const vitalName = (0, utils_3.vitalNameFromLocation)(location);
    const yAxis = `p75(${vitalName})`;
    const legend = {
        right: 10,
        top: 0,
        selected: (0, utils_1.getSeriesSelection)(location),
    };
    const datetimeSelection = {
        start,
        end,
        period: statsPeriod,
    };
    const vitalPoor = utils_3.webVitalPoor[vitalName];
    const vitalMeh = utils_3.webVitalMeh[vitalName];
    const markLines = [
        {
            seriesName: 'Thresholds',
            type: 'line',
            data: [],
            markLine: (0, markLine_1.default)({
                silent: true,
                lineStyle: {
                    color: theme.red300,
                    type: 'dashed',
                    width: 1.5,
                },
                label: {
                    show: true,
                    position: 'insideEndTop',
                    formatter: (0, locale_1.t)('Poor'),
                },
                data: [
                    {
                        yAxis: vitalPoor,
                    },
                ],
            }),
        },
        {
            seriesName: 'Thresholds',
            type: 'line',
            data: [],
            markLine: (0, markLine_1.default)({
                silent: true,
                lineStyle: {
                    color: theme.yellow300,
                    type: 'dashed',
                    width: 1.5,
                },
                label: {
                    show: true,
                    position: 'insideEndTop',
                    formatter: (0, locale_1.t)('Meh'),
                },
                data: [
                    {
                        yAxis: vitalMeh,
                    },
                ],
            }),
        },
    ];
    const chartOptions = {
        grid: {
            left: '5px',
            right: '10px',
            top: '35px',
            bottom: '0px',
        },
        seriesOptions: {
            showSymbol: false,
        },
        tooltip: {
            trigger: 'axis',
            valueFormatter: (value, seriesName) => (0, charts_1.tooltipFormatter)(value, vitalName === fields_1.WebVital.CLS ? seriesName : yAxis),
        },
        yAxis: {
            min: 0,
            max: vitalPoor,
            axisLabel: {
                color: theme.chartLabel,
                showMaxLabel: false,
                // coerces the axis to be time based
                formatter: (value) => (0, charts_1.axisLabelFormatter)(value, yAxis),
            },
        },
    };
    return (<panels_1.Panel>
      <styles_1.ChartContainer>
        <styles_1.HeaderTitleLegend>
          {(0, locale_1.t)('Duration p75')}
          <questionTooltip_1.default size="sm" position="top" title={(0, locale_1.t)(`The durations shown should fall under the vital threshold.`)}/>
        </styles_1.HeaderTitleLegend>
        <chartZoom_1.default router={router} period={statsPeriod} start={start} end={end} utc={utc}>
          {zoomRenderProps => (<eventsRequest_1.default api={api} organization={organization} period={statsPeriod} project={project} environment={environment} start={start} end={end} interval={(0, utils_1.getInterval)(datetimeSelection, 'high')} showLoading={false} query={query} includePrevious={false} yAxis={[yAxis]} partial>
              {({ timeseriesData: results, errored, loading, reloading }) => {
                if (errored) {
                    return (<errorPanel_1.default>
                      <icons_1.IconWarning color="gray500" size="lg"/>
                    </errorPanel_1.default>);
                }
                const colors = (results && theme.charts.getColorPalette(results.length - 2)) || [];
                const { smoothedResults } = (0, utils_2.transformEventStatsSmoothed)(results);
                const smoothedSeries = smoothedResults
                    ? smoothedResults.map((_a, i) => {
                        var { seriesName } = _a, rest = (0, tslib_1.__rest)(_a, ["seriesName"]);
                        return Object.assign(Object.assign({ seriesName: (0, utils_2.replaceSeriesName)(seriesName) || 'p75' }, rest), { color: colors[i], lineStyle: {
                                opacity: 1,
                                width: 2,
                            } });
                    })
                    : [];
                const seriesMax = (0, utils_3.getMaxOfSeries)(smoothedSeries);
                const yAxisMax = Math.max(seriesMax, vitalPoor);
                chartOptions.yAxis.max = yAxisMax * 1.1;
                return (<releaseSeries_1.default start={start} end={end} period={statsPeriod} utc={utc} projects={project} environments={environment}>
                    {({ releaseSeries }) => (<transitionChart_1.default loading={loading} reloading={reloading}>
                        <transparentLoadingMask_1.default visible={reloading}/>
                        {(0, getDynamicText_1.default)({
                            value: (<lineChart_1.default {...zoomRenderProps} {...chartOptions} legend={legend} onLegendSelectChanged={handleLegendSelectChanged} series={[...markLines, ...releaseSeries, ...smoothedSeries]}/>),
                            fixed: 'Web Vitals Chart',
                        })}
                      </transitionChart_1.default>)}
                  </releaseSeries_1.default>);
            }}
            </eventsRequest_1.default>)}
        </chartZoom_1.default>
      </styles_1.ChartContainer>
    </panels_1.Panel>);
}
exports.default = (0, react_router_1.withRouter)(VitalChart);
function fieldToVitalType(seriesName, vitalFields) {
    if (seriesName === (vitalFields === null || vitalFields === void 0 ? void 0 : vitalFields.poorCountField.replace('equation|', ''))) {
        return utils_3.VitalState.POOR;
    }
    if (seriesName === (vitalFields === null || vitalFields === void 0 ? void 0 : vitalFields.mehCountField.replace('equation|', ''))) {
        return utils_3.VitalState.MEH;
    }
    if (seriesName === (vitalFields === null || vitalFields === void 0 ? void 0 : vitalFields.goodCountField.replace('equation|', ''))) {
        return utils_3.VitalState.GOOD;
    }
    return undefined;
}
function __VitalChart(props) {
    const { field: yAxis, data: _results, loading, reloading, height, grid, vitalFields, } = props;
    if (!_results || !vitalFields) {
        return null;
    }
    const theme = (0, react_1.useTheme)();
    const chartOptions = {
        grid,
        seriesOptions: {
            showSymbol: false,
        },
        tooltip: {
            trigger: 'axis',
            valueFormatter: charts_1.tooltipFormatter,
        },
        xAxis: {
            axisLine: {
                show: false,
            },
            axisTick: {
                show: false,
            },
            splitLine: {
                show: false,
            },
        },
        yAxis: {
            axisLabel: {
                color: theme.chartLabel,
                showMaxLabel: false,
                formatter: (value) => (0, charts_1.axisLabelFormatter)(value, yAxis),
            },
        },
    };
    const results = _results.filter(s => !!fieldToVitalType(s.seriesName, vitalFields));
    const smoothedSeries = (results === null || results === void 0 ? void 0 : results.length)
        ? results.map((_a) => {
            var { seriesName } = _a, rest = (0, tslib_1.__rest)(_a, ["seriesName"]);
            const adjustedSeries = fieldToVitalType(seriesName, vitalFields) || 'count';
            return Object.assign(Object.assign({ seriesName: adjustedSeries }, rest), { color: theme[utils_3.vitalStateColors[adjustedSeries]], lineStyle: {
                    opacity: 1,
                    width: 2,
                } });
        })
        : [];
    return (<div>
      <transitionChart_1.default loading={loading} reloading={reloading}>
        <transparentLoadingMask_1.default visible={reloading}/>
        {(0, getDynamicText_1.default)({
            value: (<lineChart_1.default height={height} {...chartOptions} onLegendSelectChanged={() => { }} series={[...smoothedSeries]}/>),
            fixed: 'Web Vitals Chart',
        })}
      </transitionChart_1.default>
    </div>);
}
exports._VitalChart = (0, react_router_1.withRouter)(__VitalChart);
//# sourceMappingURL=vitalChart.jsx.map