Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const guideAnchor_1 = require("app/components/assistant/guideAnchor");
const smartSearchBar_1 = (0, tslib_1.__importDefault)(require("app/components/smartSearchBar"));
const locale_1 = require("app/locale");
const fields_1 = require("app/utils/discover/fields");
function ProjectFilters({ query, tagValueLoader, onSearch }) {
    const getTagValues = (tag, currentQuery) => (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
        const values = yield tagValueLoader(tag.key, currentQuery);
        return values.map(({ value }) => value);
    });
    return (<guideAnchor_1.GuideAnchor target="releases_search" position="bottom">
      <smartSearchBar_1.default searchSource="project_filters" query={query} placeholder={(0, locale_1.t)('Search by release version, build, package, or stage')} maxSearchItems={5} hasRecentSearches={false} supportedTags={Object.assign(Object.assign({}, fields_1.SEMVER_TAGS), { release: {
                key: 'release',
                name: 'release',
            } })} onSearch={onSearch} onGetTagValues={getTagValues}/>
    </guideAnchor_1.GuideAnchor>);
}
exports.default = ProjectFilters;
//# sourceMappingURL=projectFilters.jsx.map