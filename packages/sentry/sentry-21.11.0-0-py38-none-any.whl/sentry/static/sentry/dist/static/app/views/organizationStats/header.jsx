Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const button_1 = (0, tslib_1.__importDefault)(require("app/components/button"));
const featureBadge_1 = (0, tslib_1.__importDefault)(require("app/components/featureBadge"));
const Layout = (0, tslib_1.__importStar)(require("app/components/layouts/thirds"));
const link_1 = (0, tslib_1.__importDefault)(require("app/components/links/link"));
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
function StatsHeader({ organization, activeTab }) {
    return (<react_1.Fragment>
      <BorderlessHeader>
        <StyledHeaderContent>
          <StyledLayoutTitle>{(0, locale_1.t)('Stats')}</StyledLayoutTitle>
        </StyledHeaderContent>
        {activeTab === 'team' && (<Layout.HeaderActions>
            <button_1.default title={(0, locale_1.t)('Send us feedback via email')} size="small" href="mailto:workflow-feedback@sentry.io?subject=Team Stats Feedback">
              {(0, locale_1.t)('Give Feedback')}
            </button_1.default>
          </Layout.HeaderActions>)}
      </BorderlessHeader>
      <Layout.Header>
        <Layout.HeaderNavTabs underlined>
          <li className={`${activeTab === 'stats' ? 'active' : ''}`}>
            <link_1.default to={`/organizations/${organization.slug}/stats/`}>
              {(0, locale_1.t)('Usage Stats')}
            </link_1.default>
          </li>
          <li className={`${activeTab === 'team' ? 'active' : ''}`}>
            <link_1.default to={`/organizations/${organization.slug}/stats/team/`}>
              {(0, locale_1.t)('Team Stats')}
              <featureBadge_1.default type="beta"/>
            </link_1.default>
          </li>
        </Layout.HeaderNavTabs>
      </Layout.Header>
    </react_1.Fragment>);
}
exports.default = StatsHeader;
const BorderlessHeader = (0, styled_1.default)(Layout.Header) `
  border-bottom: 0;

  /* Not enough buttons to change direction for mobile view */
  grid-template-columns: 1fr auto;
`;
const StyledHeaderContent = (0, styled_1.default)(Layout.HeaderContent) `
  margin-bottom: 0;
`;
const StyledLayoutTitle = (0, styled_1.default)(Layout.Title) `
  margin-top: ${(0, space_1.default)(0.5)};
`;
//# sourceMappingURL=header.jsx.map