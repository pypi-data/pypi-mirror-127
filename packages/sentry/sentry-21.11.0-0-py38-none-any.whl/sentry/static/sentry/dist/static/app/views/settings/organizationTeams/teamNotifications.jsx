Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const React = (0, tslib_1.__importStar)(require("react"));
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const indicator_1 = require("app/actionCreators/indicator");
const button_1 = (0, tslib_1.__importDefault)(require("app/components/button"));
const confirm_1 = (0, tslib_1.__importDefault)(require("app/components/confirm"));
const externalLink_1 = (0, tslib_1.__importDefault)(require("app/components/links/externalLink"));
const panels_1 = require("app/components/panels");
const tooltip_1 = (0, tslib_1.__importDefault)(require("app/components/tooltip"));
const icons_1 = require("app/icons");
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const utils_1 = require("app/utils");
const withOrganization_1 = (0, tslib_1.__importDefault)(require("app/utils/withOrganization"));
const asyncView_1 = (0, tslib_1.__importDefault)(require("app/views/asyncView"));
const emptyMessage_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/emptyMessage"));
const textField_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/forms/textField"));
const DOCS_LINK = 'https://docs.sentry.io/product/integrations/notification-incidents/slack/#team-notifications';
const NOTIFICATION_PROVIDERS = ['slack'];
class TeamNotificationSettings extends asyncView_1.default {
    constructor() {
        super(...arguments);
        this.handleDelete = (mapping) => (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            try {
                const { organization, team } = this.props;
                const endpoint = `/teams/${organization.slug}/${team.slug}/external-teams/${mapping.id}/`;
                yield this.api.requestPromise(endpoint, {
                    method: 'DELETE',
                });
                (0, indicator_1.addSuccessMessage)((0, locale_1.t)('Deletion successful'));
                this.fetchData();
            }
            catch (_a) {
                (0, indicator_1.addErrorMessage)((0, locale_1.t)('An error occurred'));
            }
        });
    }
    getTitle() {
        return 'Team Notification Settings';
    }
    getEndpoints() {
        const { organization, team } = this.props;
        return [
            [
                'teamDetails',
                `/teams/${organization.slug}/${team.slug}/`,
                { query: { expand: ['externalTeams'] } },
            ],
            [
                'integrations',
                `/organizations/${organization.slug}/integrations/`,
                { query: { includeConfig: 0 } },
            ],
        ];
    }
    renderBody() {
        return (<panels_1.Panel>
        <panels_1.PanelHeader>{(0, locale_1.t)('Notifications')}</panels_1.PanelHeader>
        <panels_1.PanelBody>{this.renderPanelBody()}</panels_1.PanelBody>
      </panels_1.Panel>);
    }
    renderPanelBody() {
        const { organization } = this.props;
        const { teamDetails, integrations } = this.state;
        const notificationIntegrations = integrations.filter(integration => NOTIFICATION_PROVIDERS.includes(integration.provider.key));
        if (!notificationIntegrations.length) {
            return (<emptyMessage_1.default>
          {(0, locale_1.t)('No Notification Integrations have been installed yet.')}
        </emptyMessage_1.default>);
        }
        const externalTeams = (teamDetails.externalTeams || []).filter(externalTeam => NOTIFICATION_PROVIDERS.includes(externalTeam.provider));
        if (!externalTeams.length) {
            return (<emptyMessage_1.default>
          <div>{(0, locale_1.t)('No teams have been linked yet.')}</div>
          <NotDisabledSubText>
            {(0, locale_1.tct)('Head over to Slack and type [code] to get started. [link].', {
                    code: <code>/sentry link team</code>,
                    link: <externalLink_1.default href={DOCS_LINK}>{(0, locale_1.t)('Learn more')}</externalLink_1.default>,
                })}
          </NotDisabledSubText>
        </emptyMessage_1.default>);
        }
        const integrationsById = Object.fromEntries(notificationIntegrations.map(integration => [integration.id, integration]));
        const access = new Set(organization.access);
        const hasAccess = access.has('team:write');
        return externalTeams.map(externalTeam => (<FormFieldWrapper key={externalTeam.id}>
        <StyledFormField disabled label={<div>
              <NotDisabledText>
                {(0, utils_1.toTitleCase)(externalTeam.provider)}:
                {integrationsById[externalTeam.integrationId].name}
              </NotDisabledText>
              <NotDisabledSubText>
                {(0, locale_1.tct)('Unlink this channel in Slack with [code]. [link].', {
                    code: <code>/sentry unlink team</code>,
                    link: <externalLink_1.default href={DOCS_LINK}>{(0, locale_1.t)('Learn more')}</externalLink_1.default>,
                })}
              </NotDisabledSubText>
            </div>} name="externalName" value={externalTeam.externalName}/>
        <DeleteButtonWrapper>
          <tooltip_1.default title={(0, locale_1.t)('You must be an organization owner, manager or admin to remove a Slack team link')} disabled={hasAccess}>
            <confirm_1.default disabled={!hasAccess} onConfirm={() => this.handleDelete(externalTeam)} message={(0, locale_1.t)('Are you sure you want to remove this Slack team link?')}>
              <button_1.default size="small" icon={<icons_1.IconDelete size="md"/>} label={(0, locale_1.t)('delete')} disabled={!hasAccess}/>
            </confirm_1.default>
          </tooltip_1.default>
        </DeleteButtonWrapper>
      </FormFieldWrapper>));
    }
}
exports.default = (0, withOrganization_1.default)(TeamNotificationSettings);
const NotDisabledText = (0, styled_1.default)('div') `
  color: ${p => p.theme.textColor};
  line-height: ${(0, space_1.default)(2)};
`;
const NotDisabledSubText = (0, styled_1.default)('div') `
  color: ${p => p.theme.subText};
  font-size: ${p => p.theme.fontSizeRelativeSmall};
  line-height: 1.4;
  margin-top: ${(0, space_1.default)(1)};
`;
const FormFieldWrapper = (0, styled_1.default)('div') `
  display: flex;
  align-items: center;
  justify-content: flex-start;
`;
const StyledFormField = (0, styled_1.default)(textField_1.default) `
  flex: 1;
`;
const DeleteButtonWrapper = (0, styled_1.default)('div') `
  margin-right: ${(0, space_1.default)(4)};
  padding-right: ${(0, space_1.default)(0.5)};
`;
//# sourceMappingURL=teamNotifications.jsx.map