Object.defineProperty(exports, "__esModule", { value: true });
exports.LineChartListWidget = void 0;
const tslib_1 = require("tslib");
const react_1 = require("react");
const react_router_1 = require("react-router");
const pick_1 = (0, tslib_1.__importDefault)(require("lodash/pick"));
const eventsRequest_1 = (0, tslib_1.__importDefault)(require("app/components/charts/eventsRequest"));
const utils_1 = require("app/components/charts/utils");
const count_1 = (0, tslib_1.__importDefault)(require("app/components/count"));
const link_1 = (0, tslib_1.__importDefault)(require("app/components/links/link"));
const tooltip_1 = (0, tslib_1.__importDefault)(require("app/components/tooltip"));
const truncate_1 = (0, tslib_1.__importDefault)(require("app/components/truncate"));
const locale_1 = require("app/locale");
const discoverQuery_1 = (0, tslib_1.__importDefault)(require("app/utils/discover/discoverQuery"));
const fields_1 = require("app/utils/discover/fields");
const tokenizeSearch_1 = require("app/utils/tokenizeSearch");
const withApi_1 = (0, tslib_1.__importDefault)(require("app/utils/withApi"));
const chart_1 = (0, tslib_1.__importDefault)(require("app/views/performance/charts/chart"));
const utils_2 = require("app/views/performance/transactionSummary/utils");
const utils_3 = require("app/views/performance/utils");
const utils_4 = require("../../utils");
const performanceWidget_1 = require("../components/performanceWidget");
const selectableList_1 = (0, tslib_1.__importStar)(require("../components/selectableList"));
const transformDiscoverToList_1 = require("../transforms/transformDiscoverToList");
const transformEventsToArea_1 = require("../transforms/transformEventsToArea");
const utils_5 = require("../utils");
const widgetDefinitions_1 = require("../widgetDefinitions");
const slowList = [
    widgetDefinitions_1.PerformanceWidgetSetting.SLOW_HTTP_OPS,
    widgetDefinitions_1.PerformanceWidgetSetting.SLOW_DB_OPS,
    widgetDefinitions_1.PerformanceWidgetSetting.SLOW_BROWSER_OPS,
    widgetDefinitions_1.PerformanceWidgetSetting.SLOW_RESOURCE_OPS,
    widgetDefinitions_1.PerformanceWidgetSetting.MOST_SLOW_FRAMES,
    widgetDefinitions_1.PerformanceWidgetSetting.MOST_FROZEN_FRAMES,
];
function LineChartListWidget(props) {
    const [selectedListIndex, setSelectListIndex] = (0, react_1.useState)(0);
    const { ContainerActions } = props;
    if (props.fields.length !== 1) {
        throw new Error(`Line chart list widget can only accept a single field (${props.fields})`);
    }
    const field = props.fields[0];
    const isSlowestType = slowList.includes(props.chartSetting);
    const listQuery = (0, react_1.useMemo)(() => ({
        fields: field,
        component: provided => {
            const eventView = props.eventView.clone();
            eventView.sorts = [{ kind: 'desc', field }];
            if (props.chartSetting === widgetDefinitions_1.PerformanceWidgetSetting.MOST_RELATED_ISSUES) {
                eventView.fields = [
                    { field: 'issue' },
                    { field: 'transaction' },
                    { field: 'title' },
                    { field: 'project.id' },
                    { field },
                ];
                eventView.additionalConditions.setFilterValues('event.type', ['error']);
                eventView.additionalConditions.setFilterValues('!tags[transaction]', ['']);
                const mutableSearch = new tokenizeSearch_1.MutableSearch(eventView.query);
                mutableSearch.removeFilter('transaction.duration');
                eventView.additionalConditions.removeFilter('transaction.op'); // Remove transaction op incase it's applied from the performance view.
                eventView.additionalConditions.removeFilter('!transaction.op'); // Remove transaction op incase it's applied from the performance view.
                eventView.query = mutableSearch.formatString();
            }
            else if (isSlowestType) {
                eventView.additionalConditions.setFilterValues('epm()', ['>0.01']);
                eventView.fields = [
                    { field: 'transaction' },
                    { field: 'project.id' },
                    { field: 'epm()' },
                    { field },
                ];
            }
            else {
                // Most related errors
                eventView.fields = [{ field: 'transaction' }, { field: 'project.id' }, { field }];
            }
            // Don't retrieve list items with 0 in the field.
            eventView.additionalConditions.setFilterValues(field, ['>0']);
            return (<discoverQuery_1.default {...provided} eventView={eventView} location={props.location} limit={3}/>);
        },
        transform: transformDiscoverToList_1.transformDiscoverToList,
    }), [props.eventView, field, props.organization.slug]);
    const chartQuery = (0, react_1.useMemo)(() => {
        return {
            enabled: widgetData => {
                var _a, _b;
                return !!((_b = (_a = widgetData === null || widgetData === void 0 ? void 0 : widgetData.list) === null || _a === void 0 ? void 0 : _a.data) === null || _b === void 0 ? void 0 : _b.length);
            },
            fields: field,
            component: provided => {
                var _a, _b;
                const eventView = props.eventView.clone();
                if (!((_a = provided.widgetData.list.data[selectedListIndex]) === null || _a === void 0 ? void 0 : _a.transaction)) {
                    return null;
                }
                eventView.additionalConditions.setFilterValues('transaction', [
                    provided.widgetData.list.data[selectedListIndex].transaction,
                ]);
                if (props.chartSetting === widgetDefinitions_1.PerformanceWidgetSetting.MOST_RELATED_ISSUES) {
                    if (!((_b = provided.widgetData.list.data[selectedListIndex]) === null || _b === void 0 ? void 0 : _b.issue)) {
                        return null;
                    }
                    eventView.fields = [
                        { field: 'issue' },
                        { field: 'issue.id' },
                        { field: 'transaction' },
                        { field },
                    ];
                    eventView.additionalConditions.setFilterValues('issue', [
                        provided.widgetData.list.data[selectedListIndex].issue,
                    ]);
                    eventView.additionalConditions.setFilterValues('event.type', ['error']);
                    eventView.additionalConditions.setFilterValues('!tags[transaction]', ['']);
                    eventView.additionalConditions.removeFilter('transaction.op'); // Remove transaction op incase it's applied from the performance view.
                    eventView.additionalConditions.removeFilter('!transaction.op'); // Remove transaction op incase it's applied from the performance view.
                    const mutableSearch = new tokenizeSearch_1.MutableSearch(eventView.query);
                    mutableSearch.removeFilter('transaction.duration');
                    eventView.query = mutableSearch.formatString();
                }
                else {
                    eventView.fields = [{ field: 'transaction' }, { field }];
                }
                return (<EventsRequest {...(0, pick_1.default)(provided, utils_5.eventsRequestQueryProps)} limit={1} includePrevious includeTransformedData partial currentSeriesNames={[field]} query={eventView.getQueryWithAdditionalConditions()} interval={(0, utils_1.getInterval)({
                        start: provided.start,
                        end: provided.end,
                        period: provided.period,
                    }, 'medium')}/>);
            },
            transform: transformEventsToArea_1.transformEventsRequestToArea,
        };
    }, [props.eventView, field, props.organization.slug, selectedListIndex]);
    const Queries = {
        list: listQuery,
        chart: chartQuery,
    };
    return (<performanceWidget_1.GenericPerformanceWidget {...props} Subtitle={() => <selectableList_1.Subtitle>{(0, locale_1.t)('Suggested transactions')}</selectableList_1.Subtitle>} HeaderActions={provided => {
            var _a;
            return (<ContainerActions isLoading={(_a = provided.widgetData.list) === null || _a === void 0 ? void 0 : _a.isLoading}/>);
        }} EmptyComponent={selectableList_1.WidgetEmptyStateWarning} Queries={Queries} Visualizations={[
            {
                component: provided => (<DurationChart {...provided.widgetData.chart} {...provided} disableMultiAxis disableXAxis chartColors={props.chartColor ? [props.chartColor] : undefined} isLineChart/>),
                height: 160,
            },
            {
                component: provided => (<selectableList_1.default selectedIndex={selectedListIndex} setSelectedIndex={setSelectListIndex} items={provided.widgetData.list.data.map(listItem => () => {
                        const transaction = listItem.transaction;
                        const additionalQuery = {};
                        if (props.chartSetting === widgetDefinitions_1.PerformanceWidgetSetting.SLOW_HTTP_OPS) {
                            additionalQuery.breakdown = 'http';
                            additionalQuery.display = 'latency';
                        }
                        else if (props.chartSetting === widgetDefinitions_1.PerformanceWidgetSetting.SLOW_DB_OPS) {
                            additionalQuery.breakdown = 'db';
                            additionalQuery.display = 'latency';
                        }
                        else if (props.chartSetting === widgetDefinitions_1.PerformanceWidgetSetting.SLOW_BROWSER_OPS) {
                            additionalQuery.breakdown = 'browser';
                            additionalQuery.display = 'latency';
                        }
                        else if (props.chartSetting === widgetDefinitions_1.PerformanceWidgetSetting.SLOW_RESOURCE_OPS) {
                            additionalQuery.breakdown = 'resource';
                            additionalQuery.display = 'latency';
                        }
                        const transactionTarget = (0, utils_2.transactionSummaryRouteWithQuery)({
                            orgSlug: props.organization.slug,
                            projectID: listItem['project.id'],
                            transaction,
                            query: props.eventView.getGlobalSelectionQuery(),
                            additionalQuery,
                        });
                        const fieldString = (0, fields_1.getAggregateAlias)(field);
                        const valueMap = {
                            [widgetDefinitions_1.PerformanceWidgetSetting.MOST_RELATED_ERRORS]: listItem.failure_count,
                            [widgetDefinitions_1.PerformanceWidgetSetting.MOST_RELATED_ISSUES]: listItem.issue,
                            slowest: (0, utils_3.getPerformanceDuration)(listItem[fieldString]),
                        };
                        const rightValue = valueMap[isSlowestType ? 'slowest' : props.chartSetting];
                        switch (props.chartSetting) {
                            case widgetDefinitions_1.PerformanceWidgetSetting.MOST_RELATED_ISSUES:
                                return (<react_1.Fragment>
                        <selectableList_1.GrowLink to={transactionTarget} className="truncate">
                          <truncate_1.default value={transaction} maxLength={40}/>
                        </selectableList_1.GrowLink>
                        <selectableList_1.RightAlignedCell>
                          <tooltip_1.default title={listItem.title}>
                            <link_1.default to={`/organizations/${props.organization.slug}/issues/${listItem['issue.id']}/`}>
                              {rightValue}
                            </link_1.default>
                          </tooltip_1.default>
                        </selectableList_1.RightAlignedCell>
                        <selectableList_1.ListClose setSelectListIndex={setSelectListIndex} onClick={() => (0, utils_4.excludeTransaction)(listItem.transaction, props)}/>
                      </react_1.Fragment>);
                            case widgetDefinitions_1.PerformanceWidgetSetting.MOST_RELATED_ERRORS:
                                return (<react_1.Fragment>
                        <selectableList_1.GrowLink to={transactionTarget} className="truncate">
                          <truncate_1.default value={transaction} maxLength={40}/>
                        </selectableList_1.GrowLink>
                        <selectableList_1.RightAlignedCell>
                          {(0, locale_1.tct)('[count] errors', {
                                        count: <count_1.default value={rightValue}/>,
                                    })}
                        </selectableList_1.RightAlignedCell>
                        <selectableList_1.ListClose setSelectListIndex={setSelectListIndex} onClick={() => (0, utils_4.excludeTransaction)(listItem.transaction, props)}/>
                      </react_1.Fragment>);
                            default:
                                return (<react_1.Fragment>
                        <selectableList_1.GrowLink to={transactionTarget} className="truncate">
                          <truncate_1.default value={transaction} maxLength={40}/>
                        </selectableList_1.GrowLink>
                        <selectableList_1.RightAlignedCell>{rightValue}</selectableList_1.RightAlignedCell>
                        <selectableList_1.ListClose setSelectListIndex={setSelectListIndex} onClick={() => (0, utils_4.excludeTransaction)(listItem.transaction, props)}/>
                      </react_1.Fragment>);
                        }
                    })}/>),
                height: 200,
                noPadding: true,
            },
        ]}/>);
}
exports.LineChartListWidget = LineChartListWidget;
const EventsRequest = (0, withApi_1.default)(eventsRequest_1.default);
const DurationChart = (0, react_router_1.withRouter)(chart_1.default);
//# sourceMappingURL=lineChartListWidget.jsx.map