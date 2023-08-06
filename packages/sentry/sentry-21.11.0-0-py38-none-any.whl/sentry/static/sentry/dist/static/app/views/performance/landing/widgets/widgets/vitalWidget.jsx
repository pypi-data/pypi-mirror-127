Object.defineProperty(exports, "__esModule", { value: true });
exports.VitalWidget = exports.transformFieldsWithStops = void 0;
const tslib_1 = require("tslib");
const react_1 = require("react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const pick_1 = (0, tslib_1.__importDefault)(require("lodash/pick"));
const button_1 = (0, tslib_1.__importDefault)(require("app/components/button"));
const eventsRequest_1 = (0, tslib_1.__importDefault)(require("app/components/charts/eventsRequest"));
const utils_1 = require("app/components/charts/utils");
const truncate_1 = (0, tslib_1.__importDefault)(require("app/components/truncate"));
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const utils_2 = require("app/utils");
const discoverQuery_1 = (0, tslib_1.__importDefault)(require("app/utils/discover/discoverQuery"));
const fields_1 = require("app/utils/discover/fields");
const queryString_1 = require("app/utils/queryString");
const tokenizeSearch_1 = require("app/utils/tokenizeSearch");
const withApi_1 = (0, tslib_1.__importDefault)(require("app/utils/withApi"));
const utils_3 = require("app/views/performance/vitalDetail/utils");
const vitalChart_1 = require("app/views/performance/vitalDetail/vitalChart");
const utils_4 = require("../../utils");
const vitalsCards_1 = require("../../vitalsCards");
const performanceWidget_1 = require("../components/performanceWidget");
const selectableList_1 = (0, tslib_1.__importStar)(require("../components/selectableList"));
const transformDiscoverToList_1 = require("../transforms/transformDiscoverToList");
const transformEventsToVitals_1 = require("../transforms/transformEventsToVitals");
const utils_5 = require("../utils");
const widgetDefinitions_1 = require("../widgetDefinitions");
function transformFieldsWithStops(props) {
    const { field, fields, vitalStops } = props;
    const poorStop = vitalStops === null || vitalStops === void 0 ? void 0 : vitalStops.poor;
    const mehStop = vitalStops === null || vitalStops === void 0 ? void 0 : vitalStops.meh;
    if (!(0, utils_2.defined)(poorStop) || !(0, utils_2.defined)(mehStop)) {
        return {
            sortField: fields[0],
            fieldsList: fields,
        };
    }
    const poorCountField = `count_if(${field},greaterOrEquals,${poorStop})`;
    const mehCountField = `equation|count_if(${field},greaterOrEquals,${mehStop}) - count_if(${field},greaterOrEquals,${poorStop})`;
    const goodCountField = `equation|count_if(${field},greaterOrEquals,0) - count_if(${field},greaterOrEquals,${mehStop})`;
    const otherRequiredFieldsForQuery = [
        `count_if(${field},greaterOrEquals,${mehStop})`,
        `count_if(${field},greaterOrEquals,0)`,
    ];
    const vitalFields = {
        poorCountField,
        mehCountField,
        goodCountField,
    };
    const fieldsList = [
        poorCountField,
        ...otherRequiredFieldsForQuery,
        mehCountField,
        goodCountField,
    ];
    return {
        sortField: poorCountField,
        vitalFields,
        fieldsList,
    };
}
exports.transformFieldsWithStops = transformFieldsWithStops;
function VitalWidget(props) {
    const { ContainerActions, eventView, organization, location } = props;
    const [selectedListIndex, setSelectListIndex] = (0, react_1.useState)(0);
    const field = props.fields[0];
    const { fieldsList, vitalFields, sortField } = transformFieldsWithStops({
        field,
        fields: props.fields,
        vitalStops: props.chartDefinition.vitalStops,
    });
    const Queries = {
        list: (0, react_1.useMemo)(() => ({
            fields: sortField,
            component: provided => {
                const _eventView = props.eventView.clone();
                const fieldFromProps = fieldsList.map(propField => ({
                    field: propField,
                }));
                _eventView.sorts = [{ kind: 'desc', field: sortField }];
                _eventView.fields = [
                    { field: 'transaction' },
                    { field: 'title' },
                    { field: 'project.id' },
                    ...fieldFromProps,
                ];
                const mutableSearch = new tokenizeSearch_1.MutableSearch(_eventView.query);
                _eventView.query = mutableSearch.formatString();
                return (<discoverQuery_1.default {...provided} eventView={_eventView} location={props.location} limit={3}/>);
            },
            transform: transformDiscoverToList_1.transformDiscoverToList,
        }), [props.eventView, fieldsList, props.organization.slug]),
        chart: (0, react_1.useMemo)(() => ({
            enabled: widgetData => {
                var _a, _b;
                return !!((_b = (_a = widgetData === null || widgetData === void 0 ? void 0 : widgetData.list) === null || _a === void 0 ? void 0 : _a.data) === null || _b === void 0 ? void 0 : _b.length);
            },
            fields: fieldsList,
            component: provided => {
                const _eventView = props.eventView.clone();
                _eventView.additionalConditions.setFilterValues('transaction', [
                    provided.widgetData.list.data[selectedListIndex].transaction,
                ]);
                return (<EventsRequest {...(0, pick_1.default)(provided, utils_5.eventsRequestQueryProps)} limit={1} currentSeriesNames={[sortField]} includePrevious={false} partial={false} includeTransformedData query={_eventView.getQueryWithAdditionalConditions()} interval={(0, utils_1.getInterval)({
                        start: provided.start,
                        end: provided.end,
                        period: provided.period,
                    }, 'medium')}/>);
            },
            transform: transformEventsToVitals_1.transformEventsRequestToVitals,
        }), [props.eventView, selectedListIndex, props.chartSetting, props.organization.slug]),
    };
    const settingToVital = {
        [widgetDefinitions_1.PerformanceWidgetSetting.WORST_LCP_VITALS]: fields_1.WebVital.LCP,
        [widgetDefinitions_1.PerformanceWidgetSetting.WORST_FCP_VITALS]: fields_1.WebVital.FCP,
        [widgetDefinitions_1.PerformanceWidgetSetting.WORST_FID_VITALS]: fields_1.WebVital.FID,
        [widgetDefinitions_1.PerformanceWidgetSetting.WORST_CLS_VITALS]: fields_1.WebVital.CLS,
    };
    const handleViewAllClick = () => {
        // TODO(k-fish): Add analytics.
    };
    return (<performanceWidget_1.GenericPerformanceWidget {...props} Subtitle={provided => {
            var _a, _b;
            const listItem = (_a = provided.widgetData.list) === null || _a === void 0 ? void 0 : _a.data[selectedListIndex];
            if (!listItem) {
                return <selectableList_1.Subtitle> </selectableList_1.Subtitle>;
            }
            const data = {
                [settingToVital[props.chartSetting]]: getVitalDataForListItem(listItem),
            };
            return (<selectableList_1.Subtitle>
            <vitalsCards_1.VitalBar isLoading={(_b = provided.widgetData.list) === null || _b === void 0 ? void 0 : _b.isLoading} vital={settingToVital[props.chartSetting]} data={data} showBar={false} showDurationDetail={false} showDetail/>
          </selectableList_1.Subtitle>);
        }} HeaderActions={provided => {
            const vital = settingToVital[props.chartSetting];
            const target = (0, utils_3.vitalDetailRouteWithQuery)({
                orgSlug: organization.slug,
                query: eventView.generateQueryStringObject(),
                vitalName: vital,
                projectID: (0, queryString_1.decodeList)(location.query.project),
            });
            return (<react_1.Fragment>
            <div>
              <button_1.default onClick={handleViewAllClick} to={target} size="small" data-test-id="view-all-button">
                {(0, locale_1.t)('View All')}
              </button_1.default>
            </div>
            <ContainerActions {...provided.widgetData.chart}/>
          </react_1.Fragment>);
        }} Queries={Queries} Visualizations={[
            {
                component: provided => (<vitalChart_1._VitalChart {...provided.widgetData.chart} {...provided} field={field} vitalFields={vitalFields} organization={organization} query={eventView.query} project={eventView.project} environment={eventView.environment} grid={{
                        left: (0, space_1.default)(0),
                        right: (0, space_1.default)(0),
                        top: (0, space_1.default)(2),
                        bottom: (0, space_1.default)(2),
                    }}/>),
                height: 160,
            },
            {
                component: provided => (<selectableList_1.default selectedIndex={selectedListIndex} setSelectedIndex={setSelectListIndex} items={provided.widgetData.list.data.map(listItem => () => {
                        var _a;
                        const transaction = listItem.transaction;
                        const _eventView = eventView.clone();
                        const initialConditions = new tokenizeSearch_1.MutableSearch(_eventView.query);
                        initialConditions.addFilterValues('transaction', [transaction]);
                        const vital = settingToVital[props.chartSetting];
                        _eventView.query = initialConditions.formatString();
                        const target = (0, utils_3.vitalDetailRouteWithQuery)({
                            orgSlug: organization.slug,
                            query: _eventView.generateQueryStringObject(),
                            vitalName: vital,
                            projectID: (0, queryString_1.decodeList)(location.query.project),
                        });
                        const data = {
                            [settingToVital[props.chartSetting]]: getVitalDataForListItem(listItem),
                        };
                        return (<react_1.Fragment>
                    <selectableList_1.GrowLink to={target}>
                      <truncate_1.default value={transaction} maxLength={40}/>
                    </selectableList_1.GrowLink>
                    <VitalBarCell>
                      <vitalsCards_1.VitalBar isLoading={(_a = provided.widgetData.list) === null || _a === void 0 ? void 0 : _a.isLoading} vital={settingToVital[props.chartSetting]} data={data} showBar showDurationDetail={false} showDetail={false} barHeight={24}/>
                    </VitalBarCell>
                    <selectableList_1.ListClose setSelectListIndex={setSelectListIndex} onClick={() => (0, utils_4.excludeTransaction)(listItem.transaction, props)}/>
                  </react_1.Fragment>);
                    })}/>),
                height: 200,
                noPadding: true,
            },
        ]}/>);
}
exports.VitalWidget = VitalWidget;
function getVitalDataForListItem(listItem) {
    const poorData = listItem.count_if_measurements_lcp_greaterOrEquals_4000 || 0;
    const mehData = listItem['equation[0]'] || 0;
    const goodData = listItem['equation[1]'] || 0;
    const _vitalData = {
        poor: poorData,
        meh: mehData,
        good: goodData,
        p75: 0,
    };
    const vitalData = Object.assign(Object.assign({}, _vitalData), { total: _vitalData.poor + _vitalData.meh + _vitalData.good });
    return vitalData;
}
const VitalBarCell = (0, styled_1.default)(selectableList_1.RightAlignedCell) `
  width: 120px;
  margin-left: ${(0, space_1.default)(1)};
  margin-right: ${(0, space_1.default)(1)};
  display: flex;
  align-items: center;
  justify-content: center;
`;
const EventsRequest = (0, withApi_1.default)(eventsRequest_1.default);
//# sourceMappingURL=vitalWidget.jsx.map