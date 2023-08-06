Object.defineProperty(exports, "__esModule", { value: true });
exports.TrendsWidget = void 0;
const tslib_1 = require("tslib");
const react_1 = require("react");
const react_router_1 = require("react-router");
const truncate_1 = (0, tslib_1.__importDefault)(require("app/components/truncate"));
const locale_1 = require("app/locale");
const trendsDiscoverQuery_1 = (0, tslib_1.__importDefault)(require("app/utils/performance/trends/trendsDiscoverQuery"));
const tokenizeSearch_1 = require("app/utils/tokenizeSearch");
const withProjects_1 = (0, tslib_1.__importDefault)(require("app/utils/withProjects"));
const changedTransactions_1 = require("app/views/performance/trends/changedTransactions");
const utils_1 = require("app/views/performance/utils");
const chart_1 = require("../../../trends/chart");
const types_1 = require("../../../trends/types");
const utils_2 = require("../../utils");
const performanceWidget_1 = require("../components/performanceWidget");
const selectableList_1 = (0, tslib_1.__importStar)(require("../components/selectableList"));
const transformTrendsDiscover_1 = require("../transforms/transformTrendsDiscover");
const widgetDefinitions_1 = require("../widgetDefinitions");
const fields = [{ field: 'transaction' }, { field: 'project' }];
function TrendsWidget(props) {
    const { eventView: _eventView, ContainerActions } = props;
    const trendChangeType = props.chartSetting === widgetDefinitions_1.PerformanceWidgetSetting.MOST_IMPROVED
        ? types_1.TrendChangeType.IMPROVED
        : types_1.TrendChangeType.REGRESSION;
    const trendFunctionField = types_1.TrendFunctionField.AVG; // Average is the easiest chart to understand.
    const [selectedListIndex, setSelectListIndex] = (0, react_1.useState)(0);
    const eventView = _eventView.clone();
    eventView.fields = fields;
    eventView.sorts = [
        {
            kind: trendChangeType === types_1.TrendChangeType.IMPROVED ? 'asc' : 'desc',
            field: 'trend_percentage()',
        },
    ];
    const rest = Object.assign(Object.assign({}, props), { eventView });
    eventView.additionalConditions.addFilterValues('tpm()', ['>0.01']);
    eventView.additionalConditions.addFilterValues('count_percentage()', ['>0.25', '<4']);
    eventView.additionalConditions.addFilterValues('trend_percentage()', ['>0%']);
    eventView.additionalConditions.addFilterValues('confidence()', ['>6']);
    const chart = (0, react_1.useMemo)(() => ({
        fields: ['transaction', 'project'],
        component: provided => (<trendsDiscoverQuery_1.default {...provided} eventView={eventView} location={props.location} trendChangeType={trendChangeType} trendFunctionField={trendFunctionField} limit={3}/>),
        transform: transformTrendsDiscover_1.transformTrendsDiscover,
    }), [eventView, trendChangeType]);
    const Queries = {
        chart,
    };
    return (<performanceWidget_1.GenericPerformanceWidget {...rest} Subtitle={() => <selectableList_1.Subtitle>{(0, locale_1.t)('Trending Transactions')}</selectableList_1.Subtitle>} HeaderActions={provided => <ContainerActions {...provided.widgetData.chart}/>} EmptyComponent={selectableList_1.WidgetEmptyStateWarning} Queries={Queries} Visualizations={[
            {
                component: provided => (<TrendsChart {...provided} {...rest} isLoading={provided.widgetData.chart.isLoading} statsData={provided.widgetData.chart.statsData} query={eventView.query} project={eventView.project} environment={eventView.environment} start={eventView.start} end={eventView.end} statsPeriod={eventView.statsPeriod} transaction={provided.widgetData.chart.transactionsList[selectedListIndex]} trendChangeType={trendChangeType} trendFunctionField={trendFunctionField} disableXAxis disableLegend/>),
                bottomPadding: false,
                height: 160,
            },
            {
                component: provided => (<selectableList_1.default selectedIndex={selectedListIndex} setSelectedIndex={setSelectListIndex} items={provided.widgetData.chart.transactionsList.map(listItem => () => {
                        const initialConditions = new tokenizeSearch_1.MutableSearch([]);
                        initialConditions.addFilterValues('transaction', [listItem.transaction]);
                        const trendsTarget = (0, utils_1.trendsTargetRoute)({
                            organization: props.organization,
                            location: props.location,
                            initialConditions,
                            additionalQuery: {
                                trendFunction: trendFunctionField,
                            },
                        });
                        return (<react_1.Fragment>
                    <selectableList_1.GrowLink to={trendsTarget}>
                      <truncate_1.default value={listItem.transaction} maxLength={40}/>
                    </selectableList_1.GrowLink>
                    <selectableList_1.RightAlignedCell>
                      <changedTransactions_1.CompareDurations transaction={listItem}/>
                    </selectableList_1.RightAlignedCell>
                    <selectableList_1.ListClose setSelectListIndex={setSelectListIndex} onClick={() => (0, utils_2.excludeTransaction)(listItem.transaction, props)}/>
                  </react_1.Fragment>);
                    })}/>),
                height: 200,
                noPadding: true,
            },
        ]}/>);
}
exports.TrendsWidget = TrendsWidget;
const TrendsChart = (0, react_router_1.withRouter)((0, withProjects_1.default)(chart_1.Chart));
//# sourceMappingURL=trendsWidget.jsx.map