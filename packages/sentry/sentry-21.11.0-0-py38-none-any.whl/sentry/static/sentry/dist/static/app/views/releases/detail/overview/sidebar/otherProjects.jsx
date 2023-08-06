Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const button_1 = (0, tslib_1.__importDefault)(require("app/components/button"));
const collapsible_1 = (0, tslib_1.__importDefault)(require("app/components/collapsible"));
const idBadge_1 = (0, tslib_1.__importDefault)(require("app/components/idBadge"));
const utils_1 = require("app/components/organizations/globalSelectionHeader/utils");
const sidebarSection_1 = (0, tslib_1.__importDefault)(require("app/components/sidebarSection"));
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
function OtherProjects({ projects, location, version, organization }) {
    return (<sidebarSection_1.default title={(0, locale_1.tn)('Other Project for This Release', 'Other Projects for This Release', projects.length)}>
      <collapsible_1.default expandButton={({ onExpand, numberOfHiddenItems }) => (<button_1.default priority="link" onClick={onExpand}>
            {(0, locale_1.tn)('Show %s collapsed project', 'Show %s collapsed projects', numberOfHiddenItems)}
          </button_1.default>)}>
        {projects.map(project => (<Row key={project.id}>
            <idBadge_1.default project={project} avatarSize={16}/>
            <button_1.default size="xsmall" to={{
                pathname: `/organizations/${organization.slug}/releases/${encodeURIComponent(version)}/`,
                query: Object.assign(Object.assign({}, (0, utils_1.extractSelectionParameters)(location.query)), { project: project.id, yAxis: undefined }),
            }}>
              {(0, locale_1.t)('View')}
            </button_1.default>
          </Row>))}
      </collapsible_1.default>
    </sidebarSection_1.default>);
}
const Row = (0, styled_1.default)('div') `
  display: grid;
  grid-template-columns: 1fr max-content;
  align-items: center;
  justify-content: space-between;
  margin-bottom: ${(0, space_1.default)(0.75)};
  font-size: ${p => p.theme.fontSizeMedium};

  @media (min-width: ${p => p.theme.breakpoints[1]}) and (max-width: ${p => p.theme.breakpoints[2]}) {
    grid-template-columns: 200px max-content;
  }
`;
exports.default = OtherProjects;
//# sourceMappingURL=otherProjects.jsx.map