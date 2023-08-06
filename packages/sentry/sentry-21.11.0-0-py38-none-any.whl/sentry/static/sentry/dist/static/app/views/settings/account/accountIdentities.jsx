Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const moment_1 = (0, tslib_1.__importDefault)(require("moment"));
const account_1 = require("app/actionCreators/account");
const alert_1 = (0, tslib_1.__importDefault)(require("app/components/alert"));
const button_1 = (0, tslib_1.__importDefault)(require("app/components/button"));
const confirm_1 = (0, tslib_1.__importDefault)(require("app/components/confirm"));
const dateTime_1 = (0, tslib_1.__importDefault)(require("app/components/dateTime"));
const panels_1 = require("app/components/panels");
const tag_1 = (0, tslib_1.__importDefault)(require("app/components/tag"));
const icons_1 = require("app/icons");
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const types_1 = require("app/types");
const asyncView_1 = (0, tslib_1.__importDefault)(require("app/views/asyncView"));
const emptyMessage_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/emptyMessage"));
const identityIcon_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/identityIcon"));
const settingsPageHeader_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/settingsPageHeader"));
const textBlock_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/text/textBlock"));
const ENDPOINT = '/users/me/user-identities/';
class AccountIdentities extends asyncView_1.default {
    constructor() {
        super(...arguments);
        this.renderItem = (identity) => {
            return (<IdentityPanelItem key={`${identity.category}:${identity.id}`}>
        <InternalContainer>
          <identityIcon_1.default providerId={identity.provider.key}/>
          <IdentityText isSingleLine={!identity.dateAdded}>
            <IdentityName>{identity.provider.name}</IdentityName>
            {identity.dateAdded && <IdentityDateTime date={(0, moment_1.default)(identity.dateAdded)}/>}
          </IdentityText>
        </InternalContainer>
        <InternalContainer>
          <TagWrapper>
            {identity.category === types_1.UserIdentityCategory.SOCIAL_IDENTITY && (<tag_1.default type="default">{(0, locale_1.t)('Legacy')}</tag_1.default>)}
            {identity.category !== types_1.UserIdentityCategory.ORG_IDENTITY && (<tag_1.default type="default">
                {identity.isLogin ? (0, locale_1.t)('Sign In') : (0, locale_1.t)('Integration')}
              </tag_1.default>)}
            {identity.organization && (<tag_1.default type="highlight">{identity.organization.slug}</tag_1.default>)}
          </TagWrapper>

          {this.renderButton(identity)}
        </InternalContainer>
      </IdentityPanelItem>);
        };
        this.handleDisconnect = (identity) => {
            (0, account_1.disconnectIdentity)(identity, () => this.reloadData());
        };
        this.itemOrder = (a, b) => {
            var _a, _b, _c, _d, _e, _f, _g, _h;
            function categoryRank(c) {
                return [
                    types_1.UserIdentityCategory.GLOBAL_IDENTITY,
                    types_1.UserIdentityCategory.SOCIAL_IDENTITY,
                    types_1.UserIdentityCategory.ORG_IDENTITY,
                ].indexOf(c.category);
            }
            if (a.provider.name !== b.provider.name) {
                return a.provider.name < b.provider.name ? -1 : 1;
            }
            if (a.category !== b.category) {
                return categoryRank(a) - categoryRank(b);
            }
            if (((_b = (_a = a.organization) === null || _a === void 0 ? void 0 : _a.name) !== null && _b !== void 0 ? _b : '') !== ((_d = (_c = b.organization) === null || _c === void 0 ? void 0 : _c.name) !== null && _d !== void 0 ? _d : '')) {
                return ((_f = (_e = a.organization) === null || _e === void 0 ? void 0 : _e.name) !== null && _f !== void 0 ? _f : '') < ((_h = (_g = b.organization) === null || _g === void 0 ? void 0 : _g.name) !== null && _h !== void 0 ? _h : '') ? -1 : 1;
            }
            return 0;
        };
    }
    getDefaultState() {
        return Object.assign(Object.assign({}, super.getDefaultState()), { identities: [] });
    }
    getEndpoints() {
        return [['identities', ENDPOINT]];
    }
    getTitle() {
        return (0, locale_1.t)('Identities');
    }
    renderButton(identity) {
        return identity.status === types_1.UserIdentityStatus.CAN_DISCONNECT ? (<confirm_1.default onConfirm={() => this.handleDisconnect(identity)} priority="danger" confirmText={(0, locale_1.t)('Disconnect')} message={<react_1.Fragment>
            <alert_1.default type="error" icon={<icons_1.IconFlag size="md"/>}>
              {(0, locale_1.tct)('Disconnect Your [provider] Identity?', {
                    provider: identity.provider.name,
                })}
            </alert_1.default>
            <textBlock_1.default>
              {identity.isLogin
                    ? (0, locale_1.t)('After disconnecting, you will need to use a password or another identity to sign in.')
                    : (0, locale_1.t)("This action can't be undone.")}
            </textBlock_1.default>
          </react_1.Fragment>}>
        <button_1.default size="small">{(0, locale_1.t)('Disconnect')}</button_1.default>
      </confirm_1.default>) : (<button_1.default size="small" disabled title={identity.status === types_1.UserIdentityStatus.NEEDED_FOR_GLOBAL_AUTH
                ? (0, locale_1.t)('You need this identity to sign into your account. If you want to disconnect it, set a password first.')
                : identity.status === types_1.UserIdentityStatus.NEEDED_FOR_ORG_AUTH
                    ? (0, locale_1.t)('You need this identity to access your organization.')
                    : null}>
        {(0, locale_1.t)('Disconnect')}
      </button_1.default>);
    }
    renderBody() {
        var _a, _b;
        const appIdentities = (_a = this.state.identities) === null || _a === void 0 ? void 0 : _a.filter(identity => identity.category !== types_1.UserIdentityCategory.ORG_IDENTITY).sort(this.itemOrder);
        const orgIdentities = (_b = this.state.identities) === null || _b === void 0 ? void 0 : _b.filter(identity => identity.category === types_1.UserIdentityCategory.ORG_IDENTITY).sort(this.itemOrder);
        return (<react_1.Fragment>
        <settingsPageHeader_1.default title="Identities"/>

        <panels_1.Panel>
          <panels_1.PanelHeader>{(0, locale_1.t)('Application Identities')}</panels_1.PanelHeader>
          <panels_1.PanelBody>
            {!(appIdentities === null || appIdentities === void 0 ? void 0 : appIdentities.length) ? (<emptyMessage_1.default>
                {(0, locale_1.t)('There are no application identities associated with your Sentry account')}
              </emptyMessage_1.default>) : (appIdentities.map(this.renderItem))}
          </panels_1.PanelBody>
        </panels_1.Panel>

        <panels_1.Panel>
          <panels_1.PanelHeader>{(0, locale_1.t)('Organization Identities')}</panels_1.PanelHeader>
          <panels_1.PanelBody>
            {!(orgIdentities === null || orgIdentities === void 0 ? void 0 : orgIdentities.length) ? (<emptyMessage_1.default>
                {(0, locale_1.t)('There are no organization identities associated with your Sentry account')}
              </emptyMessage_1.default>) : (orgIdentities.map(this.renderItem))}
          </panels_1.PanelBody>
        </panels_1.Panel>
      </react_1.Fragment>);
    }
}
const IdentityPanelItem = (0, styled_1.default)(panels_1.PanelItem) `
  align-items: center;
  justify-content: space-between;
`;
const InternalContainer = (0, styled_1.default)('div') `
  display: flex;
  flex-direction: row;
  justify-content: center;
`;
const IdentityText = (0, styled_1.default)('div') `
  height: 36px;
  display: flex;
  flex-direction: column;
  justify-content: ${p => (p.isSingleLine ? 'center' : 'space-between')};
  margin-left: ${(0, space_1.default)(1.5)};
`;
const IdentityName = (0, styled_1.default)('div') `
  font-weight: bold;
`;
const IdentityDateTime = (0, styled_1.default)(dateTime_1.default) `
  font-size: ${p => p.theme.fontSizeRelativeSmall};
  color: ${p => p.theme.subText};
`;
const TagWrapper = (0, styled_1.default)('div') `
  display: flex;
  align-items: center;
  justify-content: flex-start;
  flex-grow: 1;
  margin-right: ${(0, space_1.default)(1)};
`;
exports.default = AccountIdentities;
//# sourceMappingURL=accountIdentities.jsx.map