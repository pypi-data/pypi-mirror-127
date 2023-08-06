Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const errorPanel_1 = (0, tslib_1.__importDefault)(require("app/components/charts/errorPanel"));
const dropdownButton_1 = (0, tslib_1.__importDefault)(require("app/components/dropdownButton"));
const dropdownControl_1 = (0, tslib_1.__importDefault)(require("app/components/dropdownControl"));
const emptyStateWarning_1 = (0, tslib_1.__importDefault)(require("app/components/emptyStateWarning"));
const loadingIndicator_1 = (0, tslib_1.__importDefault)(require("app/components/loadingIndicator"));
const utils_1 = require("app/components/performance/waterfall/utils");
const radio_1 = (0, tslib_1.__importDefault)(require("app/components/radio"));
const icons_1 = require("app/icons");
const locale_1 = require("app/locale");
const overflowEllipsis_1 = (0, tslib_1.__importDefault)(require("app/styles/overflowEllipsis"));
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const utils_2 = require("app/utils");
const spanOpsQuery_1 = (0, tslib_1.__importDefault)(require("app/utils/performance/suspectSpans/spanOpsQuery"));
const queryString_1 = require("app/utils/queryString");
const tokenizeSearch_1 = require("app/utils/tokenizeSearch");
function OpsFilter(props) {
    const { location, eventView, organization, handleOpChange, transactionName } = props;
    // clear out the query string from the event view
    // as we want to restrict queries to the op names
    const conditions = new tokenizeSearch_1.MutableSearch('');
    conditions
        .setFilterValues('event.type', ['transaction'])
        .setFilterValues('transaction', [transactionName]);
    const opsFilterEventView = eventView.clone();
    opsFilterEventView.query = conditions.formatString();
    const currentOp = (0, queryString_1.decodeScalar)(location.query.spanOp);
    return (<dropdownControl_1.default menuWidth="240px" blendWithActor button={({ isOpen, getActorProps }) => (<dropdownButton_1.default data-test-id="ops-filter-button" {...getActorProps()} showChevron={false} isOpen={isOpen}>
          <react_1.Fragment>
            <icons_1.IconFilter size="xs"/>
            <FilterLabel>{(0, locale_1.t)('Filter')}</FilterLabel>
          </react_1.Fragment>
        </dropdownButton_1.default>)}>
      <List>
        <ListHeader data-test-id="span-op-filter-header" onClick={event => {
            event.stopPropagation();
            handleOpChange(undefined);
        }}>
          <HeaderTitle>{(0, locale_1.t)('All Operations')}</HeaderTitle>
          <radio_1.default radioSize="small" checked={!(0, utils_2.defined)(currentOp)} onChange={() => { }}/>
        </ListHeader>
        <spanOpsQuery_1.default location={location} orgSlug={organization.slug} eventView={opsFilterEventView} cursor="0:0:1" noPagination>
          {({ spanOps, isLoading, error }) => {
            if (isLoading) {
                return <StyledLoadingIndicator />;
            }
            if (error) {
                return (<errorPanel_1.default height="124px">
                  <icons_1.IconWarning color="gray300" size="lg"/>
                </errorPanel_1.default>);
            }
            if (!(0, utils_2.defined)(spanOps) || spanOps.length === 0) {
                return <emptyStateWarning_1.default small>{(0, locale_1.t)('No span ops')}</emptyStateWarning_1.default>;
            }
            return spanOps.map(spanOp => (<ListItem data-test-id="span-op-filter-item" key={spanOp.op} onClick={event => {
                    event.stopPropagation();
                    handleOpChange(spanOp.op);
                }}>
                <OperationDot backgroundColor={(0, utils_1.pickBarColor)(spanOp.op)}/>
                <OperationName>{spanOp.op}</OperationName>
                <radio_1.default radioSize="small" checked={spanOp.op === currentOp} onChange={() => { }}/>
              </ListItem>));
        }}
        </spanOpsQuery_1.default>
      </List>
    </dropdownControl_1.default>);
}
exports.default = OpsFilter;
const FilterLabel = (0, styled_1.default)('span') `
  margin-left: ${(0, space_1.default)(1)};
`;
const List = (0, styled_1.default)('ul') `
  max-height: 250px;
  overflow-y: auto;
  list-style: none;
  margin: 0;
  padding: 0;
`;
const ListHeader = (0, styled_1.default)('li') `
  display: grid;
  grid-template-columns: auto min-content;
  grid-column-gap: ${(0, space_1.default)(1)};
  align-items: center;

  margin: 0;
  background-color: ${p => p.theme.backgroundSecondary};
  color: ${p => p.theme.gray300};
  font-weight: normal;
  font-size: ${p => p.theme.fontSizeMedium};
  padding: ${(0, space_1.default)(1)} ${(0, space_1.default)(2)};
  border-bottom: 1px solid ${p => p.theme.border};
`;
const HeaderTitle = (0, styled_1.default)('span') `
  font-size: ${p => p.theme.fontSizeMedium};
`;
const ListItem = (0, styled_1.default)('li') `
  display: grid;
  grid-template-columns: max-content 1fr max-content;
  grid-column-gap: ${(0, space_1.default)(1)};
  align-items: center;
  padding: ${(0, space_1.default)(1)} ${(0, space_1.default)(2)};
  border-bottom: 1px solid ${p => p.theme.border};
  :hover {
    background-color: ${p => p.theme.backgroundSecondary};
  }

  &:hover span {
    color: ${p => p.theme.blue300};
    text-decoration: underline;
  }
`;
const OperationDot = (0, styled_1.default)('div') `
  content: '';
  display: block;
  width: 8px;
  min-width: 8px;
  height: 8px;
  margin-right: ${(0, space_1.default)(1)};
  border-radius: 100%;

  background-color: ${p => p.backgroundColor};
`;
const OperationName = (0, styled_1.default)('span') `
  font-size: ${p => p.theme.fontSizeMedium};
  ${overflowEllipsis_1.default};
`;
const StyledLoadingIndicator = (0, styled_1.default)(loadingIndicator_1.default) `
  margin: ${(0, space_1.default)(4)} auto;
`;
//# sourceMappingURL=opsFilter.jsx.map