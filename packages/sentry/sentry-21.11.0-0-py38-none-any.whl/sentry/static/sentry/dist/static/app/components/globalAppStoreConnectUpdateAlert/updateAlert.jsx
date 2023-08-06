Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const alert_1 = (0, tslib_1.__importDefault)(require("app/components/alert"));
const appStoreConnectContext_1 = (0, tslib_1.__importDefault)(require("app/components/projects/appStoreConnectContext"));
const icons_1 = require("app/icons");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
function UpdateAlert({ Wrapper, project, className }) {
    const appStoreConnectContext = (0, react_1.useContext)(appStoreConnectContext_1.default);
    if (!project ||
        !appStoreConnectContext ||
        !Object.keys(appStoreConnectContext).some(key => !!appStoreConnectContext[key].updateAlertMessage)) {
        return null;
    }
    const notices = (<Notices className={className}>
      {Object.keys(appStoreConnectContext).map(key => {
            const { updateAlertMessage } = appStoreConnectContext[key];
            if (!updateAlertMessage) {
                return null;
            }
            return (<NoMarginBottomAlert key={key} type="warning" icon={<icons_1.IconRefresh />}>
            <AlertContent>{updateAlertMessage}</AlertContent>
          </NoMarginBottomAlert>);
        })}
    </Notices>);
    return Wrapper ? <Wrapper>{notices}</Wrapper> : notices;
}
exports.default = UpdateAlert;
const Notices = (0, styled_1.default)('div') `
  display: grid;
  grid-gap: ${(0, space_1.default)(2)};
  margin-bottom: ${(0, space_1.default)(3)};
`;
const NoMarginBottomAlert = (0, styled_1.default)(alert_1.default) `
  margin-bottom: 0;
`;
const AlertContent = (0, styled_1.default)('div') `
  display: grid;
  grid-template-columns: 1fr max-content;
  grid-gap: ${(0, space_1.default)(1)};
`;
//# sourceMappingURL=updateAlert.jsx.map