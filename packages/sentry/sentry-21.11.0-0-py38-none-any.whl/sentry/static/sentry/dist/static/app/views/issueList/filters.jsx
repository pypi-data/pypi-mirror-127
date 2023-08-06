Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const React = (0, tslib_1.__importStar)(require("react"));
const react_1 = require("@emotion/react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const guideAnchor_1 = (0, tslib_1.__importDefault)(require("app/components/assistant/guideAnchor"));
const projectsStore_1 = (0, tslib_1.__importDefault)(require("app/stores/projectsStore"));
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const displayOptions_1 = (0, tslib_1.__importDefault)(require("./displayOptions"));
const searchBar_1 = (0, tslib_1.__importDefault)(require("./searchBar"));
const sortOptions_1 = (0, tslib_1.__importDefault)(require("./sortOptions"));
class IssueListFilters extends React.Component {
    render() {
        var _a, _b;
        const { organization, savedSearch, query, isSearchDisabled, sort, display, selectedProjects, onSidebarToggle, onSearch, onSortChange, onDisplayChange, tagValueLoader, tags, } = this.props;
        const isAssignedQuery = /\bassigned:/.test(query);
        const hasIssuePercentDisplay = organization.features.includes('issue-percent-display');
        const hasMultipleProjectsSelected = !selectedProjects || selectedProjects.length !== 1 || selectedProjects[0] === -1;
        const hasSessions = !hasMultipleProjectsSelected &&
            ((_b = (_a = projectsStore_1.default.getById(`${selectedProjects[0]}`)) === null || _a === void 0 ? void 0 : _a.hasSessions) !== null && _b !== void 0 ? _b : false);
        return (<SearchContainer hasIssuePercentDisplay={hasIssuePercentDisplay}>
        <react_1.ClassNames>
          {({ css }) => (<guideAnchor_1.default target="assigned_or_suggested_query" disabled={!isAssignedQuery} containerClassName={css `
                width: 100%;
              `}>
              <searchBar_1.default organization={organization} query={query || ''} sort={sort} onSearch={onSearch} disabled={isSearchDisabled} excludeEnvironment supportedTags={tags} tagValueLoader={tagValueLoader} savedSearch={savedSearch} onSidebarToggle={onSidebarToggle}/>
            </guideAnchor_1.default>)}
        </react_1.ClassNames>

        <DropdownsWrapper hasIssuePercentDisplay={hasIssuePercentDisplay}>
          {hasIssuePercentDisplay && (<displayOptions_1.default onDisplayChange={onDisplayChange} display={display} hasMultipleProjectsSelected={hasMultipleProjectsSelected} hasSessions={hasSessions}/>)}
          <sortOptions_1.default sort={sort} query={query} onSelect={onSortChange}/>
        </DropdownsWrapper>
      </SearchContainer>);
    }
}
const SearchContainer = (0, styled_1.default)('div') `
  display: inline-grid;
  grid-gap: ${(0, space_1.default)(1)};
  margin-bottom: ${(0, space_1.default)(2)};
  width: 100%;

  @media (min-width: ${p => p.theme.breakpoints[p.hasIssuePercentDisplay ? 1 : 0]}) {
    grid-template-columns: 1fr auto;
  }

  @media (max-width: ${p => p.theme.breakpoints[0]}) {
    grid-template-columns: 1fr;
  }
`;
const DropdownsWrapper = (0, styled_1.default)('div') `
  display: grid;
  grid-gap: ${(0, space_1.default)(1)};
  grid-template-columns: 1fr ${p => (p.hasIssuePercentDisplay ? '1fr' : '')};
  align-items: start;

  @media (max-width: ${p => p.theme.breakpoints[0]}) {
    grid-template-columns: 1fr;
  }
`;
exports.default = IssueListFilters;
//# sourceMappingURL=filters.jsx.map