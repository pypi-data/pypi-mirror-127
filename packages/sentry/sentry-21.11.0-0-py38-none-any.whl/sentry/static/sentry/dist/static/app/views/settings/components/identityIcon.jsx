Object.defineProperty(exports, "__esModule", { value: true });
exports.ICON_PATHS = exports.DEFAULT_ICON = void 0;
const tslib_1 = require("tslib");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const logo_asana_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-asana.svg"));
const logo_auth0_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-auth0.svg"));
const logo_azure_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-azure.svg"));
const logo_bitbucket_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-bitbucket.svg"));
const logo_bitbucket_server_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-bitbucket-server.svg"));
const logo_default_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-default.svg"));
const logo_github_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-github.svg"));
const logo_github_enterprise_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-github-enterprise.svg"));
const logo_gitlab_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-gitlab.svg"));
const logo_google_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-google.svg"));
const logo_jira_server_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-jira-server.svg"));
const logo_msteams_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-msteams.svg"));
const logo_okta_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-okta.svg"));
const logo_onelogin_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-onelogin.svg"));
const logo_rippling_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-rippling.svg"));
const logo_saml2_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-saml2.svg"));
const logo_slack_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-slack.svg"));
const logo_visualstudio_svg_1 = (0, tslib_1.__importDefault)(require("sentry-logos/logo-visualstudio.svg"));
// Map of plugin id -> logo filename
exports.DEFAULT_ICON = logo_default_svg_1.default;
exports.ICON_PATHS = {
    _default: exports.DEFAULT_ICON,
    'active-directory': logo_azure_svg_1.default,
    asana: logo_asana_svg_1.default,
    auth0: logo_auth0_svg_1.default,
    bitbucket: logo_bitbucket_svg_1.default,
    bitbucket_server: logo_bitbucket_server_svg_1.default,
    github: logo_github_svg_1.default,
    github_enterprise: logo_github_enterprise_svg_1.default,
    gitlab: logo_gitlab_svg_1.default,
    google: logo_google_svg_1.default,
    jira_server: logo_jira_server_svg_1.default,
    msteams: logo_msteams_svg_1.default,
    okta: logo_okta_svg_1.default,
    onelogin: logo_onelogin_svg_1.default,
    rippling: logo_rippling_svg_1.default,
    saml2: logo_saml2_svg_1.default,
    slack: logo_slack_svg_1.default,
    visualstudio: logo_visualstudio_svg_1.default,
    vsts: logo_azure_svg_1.default,
};
const IdentityIcon = (0, styled_1.default)('div') `
  position: relative;
  height: ${p => p.size}px;
  width: ${p => p.size}px;
  border-radius: 2px;
  border: 0;
  display: inline-block;
  background-size: contain;
  background-position: center center;
  background-repeat: no-repeat;
  background-image: url(${({ providerId }) => (providerId !== undefined && exports.ICON_PATHS[providerId]) || exports.DEFAULT_ICON});
`;
IdentityIcon.defaultProps = {
    providerId: '_default',
    size: 36,
};
exports.default = IdentityIcon;
//# sourceMappingURL=identityIcon.jsx.map