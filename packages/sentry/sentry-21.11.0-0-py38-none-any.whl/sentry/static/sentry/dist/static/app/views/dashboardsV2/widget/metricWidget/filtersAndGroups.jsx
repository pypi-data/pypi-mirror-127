Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const groupByField_1 = (0, tslib_1.__importDefault)(require("./groupByField"));
const searchQueryField_1 = (0, tslib_1.__importDefault)(require("./searchQueryField"));
function FiltersAndGroups({ api, orgSlug, projSlug, searchQuery, groupBy, metricTags, onChangeSearchQuery, onChangeGroupBy, }) {
    return (<Wrapper>
      <searchQueryField_1.default api={api} tags={metricTags} orgSlug={orgSlug} projectSlug={projSlug} query={searchQuery} onSearch={onChangeSearchQuery} onBlur={onChangeSearchQuery}/>
      <groupByField_1.default metricTags={metricTags} groupBy={groupBy} onChange={onChangeGroupBy}/>
    </Wrapper>);
}
exports.default = FiltersAndGroups;
const Wrapper = (0, styled_1.default)('div') `
  display: grid;
  grid-gap: ${(0, space_1.default)(2)};

  @media (min-width: ${p => p.theme.breakpoints[3]}) {
    grid-template-columns: 1fr 33%;
    grid-gap: ${(0, space_1.default)(1)};
    align-items: center;
  }
`;
//# sourceMappingURL=filtersAndGroups.jsx.map