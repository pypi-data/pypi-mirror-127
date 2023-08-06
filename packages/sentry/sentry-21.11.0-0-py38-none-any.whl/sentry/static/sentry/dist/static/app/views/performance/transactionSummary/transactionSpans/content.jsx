Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const react_router_1 = require("react-router");
const omit_1 = (0, tslib_1.__importDefault)(require("lodash/omit"));
const dropdownControl_1 = (0, tslib_1.__importStar)(require("app/components/dropdownControl"));
const emptyStateWarning_1 = (0, tslib_1.__importDefault)(require("app/components/emptyStateWarning"));
const searchBar_1 = (0, tslib_1.__importDefault)(require("app/components/events/searchBar"));
const Layout = (0, tslib_1.__importStar)(require("app/components/layouts/thirds"));
const loadingIndicator_1 = (0, tslib_1.__importDefault)(require("app/components/loadingIndicator"));
const getParams_1 = require("app/components/organizations/globalSelectionHeader/getParams");
const pagination_1 = (0, tslib_1.__importDefault)(require("app/components/pagination"));
const locale_1 = require("app/locale");
const utils_1 = require("app/utils");
const discoverQuery_1 = (0, tslib_1.__importDefault)(require("app/utils/discover/discoverQuery"));
const fields_1 = require("app/utils/discover/fields");
const suspectSpansQuery_1 = (0, tslib_1.__importDefault)(require("app/utils/performance/suspectSpans/suspectSpansQuery"));
const queryString_1 = require("app/utils/queryString");
const tokenizeSearch_1 = require("app/utils/tokenizeSearch");
const utils_2 = require("../utils");
const opsFilter_1 = (0, tslib_1.__importDefault)(require("./opsFilter"));
const styles_1 = require("./styles");
const suspectSpanCard_1 = (0, tslib_1.__importDefault)(require("./suspectSpanCard"));
const utils_3 = require("./utils");
function SpansContent(props) {
    const { location, organization, eventView, setError, transactionName } = props;
    const query = (0, queryString_1.decodeScalar)(location.query.query, '');
    function handleChange(key) {
        return function (value) {
            const queryParams = (0, getParams_1.getParams)(Object.assign(Object.assign({}, (location.query || {})), { [key]: value }));
            // do not propagate pagination when making a new search
            const toOmit = ['cursor'];
            if (!(0, utils_1.defined)(value)) {
                toOmit.push(key);
            }
            const searchQueryParams = (0, omit_1.default)(queryParams, toOmit);
            react_router_1.browserHistory.push(Object.assign(Object.assign({}, location), { query: searchQueryParams }));
        };
    }
    const spanOp = (0, queryString_1.decodeScalar)(location.query.spanOp);
    const sort = (0, utils_3.getSuspectSpanSortFromEventView)(eventView);
    const totalsView = getTotalsView(eventView);
    return (<Layout.Main fullWidth>
      <styles_1.Actions>
        <opsFilter_1.default location={location} eventView={eventView} organization={organization} handleOpChange={handleChange('spanOp')} transactionName={transactionName}/>
        <searchBar_1.default organization={organization} projectIds={eventView.project} query={query} fields={eventView.fields} onSearch={handleChange('query')}/>
        <dropdownControl_1.default buttonProps={{ prefix: sort.prefix }} label={sort.label}>
          {utils_3.SPAN_SORT_OPTIONS.map(option => (<dropdownControl_1.DropdownItem key={option.field} eventKey={option.field} isActive={option.field === sort.field} onSelect={handleChange('sort')}>
              {option.label}
            </dropdownControl_1.DropdownItem>))}
        </dropdownControl_1.default>
      </styles_1.Actions>
      <discoverQuery_1.default eventView={totalsView} orgSlug={organization.slug} location={location} referrer="api.performance.transaction-spans" cursor="0:0:1" noPagination>
        {({ tableData }) => {
            var _a, _b;
            const totals = (_b = (_a = tableData === null || tableData === void 0 ? void 0 : tableData.data) === null || _a === void 0 ? void 0 : _a[0]) !== null && _b !== void 0 ? _b : null;
            return (<suspectSpansQuery_1.default location={location} orgSlug={organization.slug} eventView={eventView} spanOps={(0, utils_1.defined)(spanOp) ? [spanOp] : []}>
              {({ suspectSpans, isLoading, error, pageLinks }) => {
                    if (error) {
                        setError(error);
                        return null;
                    }
                    // make sure to clear the clear the error message
                    setError(undefined);
                    if (isLoading) {
                        return <loadingIndicator_1.default />;
                    }
                    if (!(suspectSpans === null || suspectSpans === void 0 ? void 0 : suspectSpans.length)) {
                        return (<emptyStateWarning_1.default>
                      <p>{(0, locale_1.t)('No span data found')}</p>
                    </emptyStateWarning_1.default>);
                    }
                    return (<react_1.Fragment>
                    {suspectSpans.map(suspectSpan => (<suspectSpanCard_1.default key={`${suspectSpan.op}-${suspectSpan.group}`} location={location} organization={organization} suspectSpan={suspectSpan} generateTransactionLink={(0, utils_2.generateTransactionLink)(transactionName)} eventView={eventView} totals={totals}/>))}
                    <pagination_1.default pageLinks={pageLinks}/>
                  </react_1.Fragment>);
                }}
            </suspectSpansQuery_1.default>);
        }}
      </discoverQuery_1.default>
    </Layout.Main>);
}
/**
 * For the totals view, we want to get some transaction level stats like
 * the number of transactions and the sum of the transaction duration.
 * This requires the removal of any aggregate conditions as they can result
 * in unexpected empty responses.
 */
function getTotalsView(eventView) {
    const totalsView = eventView.withColumns([
        { kind: 'function', function: ['count', '', undefined, undefined] },
        { kind: 'function', function: ['sum', 'transaction.duration', undefined, undefined] },
    ]);
    const conditions = new tokenizeSearch_1.MutableSearch(eventView.query);
    // filter out any aggregate conditions
    Object.keys(conditions.filters).forEach(field => {
        if ((0, fields_1.isAggregateField)(field)) {
            conditions.removeFilter(field);
        }
    });
    totalsView.query = conditions.formatString();
    return totalsView;
}
exports.default = SpansContent;
//# sourceMappingURL=content.jsx.map