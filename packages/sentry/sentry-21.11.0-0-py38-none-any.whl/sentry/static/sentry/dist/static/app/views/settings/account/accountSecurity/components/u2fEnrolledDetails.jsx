Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = (0, tslib_1.__importStar)(require("react"));
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const button_1 = (0, tslib_1.__importDefault)(require("app/components/button"));
const confirm_1 = (0, tslib_1.__importDefault)(require("app/components/confirm"));
const dateTime_1 = (0, tslib_1.__importDefault)(require("app/components/dateTime"));
const panels_1 = require("app/components/panels");
const tooltip_1 = (0, tslib_1.__importDefault)(require("app/components/tooltip"));
const icons_1 = require("app/icons");
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const confirmHeader_1 = (0, tslib_1.__importDefault)(require("app/views/settings/account/accountSecurity/components/confirmHeader"));
const emptyMessage_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/emptyMessage"));
const input_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/forms/controls/input"));
const textBlock_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/text/textBlock"));
const U2fEnrolledDetails = props => {
    const { className, isEnrolled, devices, id, onRemoveU2fDevice, onRenameU2fDevice } = props;
    if (id !== 'u2f' || !isEnrolled) {
        return null;
    }
    const hasDevices = devices === null || devices === void 0 ? void 0 : devices.length;
    // Note Tooltip doesn't work because of bootstrap(?) pointer events for disabled buttons
    const isLastDevice = hasDevices === 1;
    return (<panels_1.Panel className={className}>
      <panels_1.PanelHeader>{(0, locale_1.t)('Device name')}</panels_1.PanelHeader>

      <panels_1.PanelBody>
        {!hasDevices && (<emptyMessage_1.default>{(0, locale_1.t)('You have not added any U2F devices')}</emptyMessage_1.default>)}
        {hasDevices &&
            (devices === null || devices === void 0 ? void 0 : devices.map((device, i) => (<Device key={i} device={device} isLastDevice={isLastDevice} onRenameU2fDevice={onRenameU2fDevice} onRemoveU2fDevice={onRemoveU2fDevice}/>)))}
        <AddAnotherPanelItem>
          <button_1.default type="button" to="/settings/account/security/mfa/u2f/enroll/" size="small">
            {(0, locale_1.t)('Add Another Device')}
          </button_1.default>
        </AddAnotherPanelItem>
      </panels_1.PanelBody>
    </panels_1.Panel>);
};
const Device = props => {
    const { device, isLastDevice, onRenameU2fDevice, onRemoveU2fDevice } = props;
    const [deviceName, setDeviceName] = (0, react_1.useState)(device.name);
    const [isEditing, setEditting] = (0, react_1.useState)(false);
    if (!isEditing) {
        return (<DevicePanelItem key={device.name}>
        <DeviceInformation>
          <Name>{device.name}</Name>
          <FadedDateTime date={device.timestamp}/>
        </DeviceInformation>
        <Actions>
          <button_1.default size="small" onClick={() => setEditting(true)}>
            {(0, locale_1.t)('Rename Device')}
          </button_1.default>
        </Actions>
        <Actions>
          <confirm_1.default onConfirm={() => onRemoveU2fDevice(device)} disabled={isLastDevice} message={<react_1.Fragment>
                <confirmHeader_1.default>{(0, locale_1.t)('Do you want to remove U2F device?')}</confirmHeader_1.default>
                <textBlock_1.default>
                  {(0, locale_1.t)(`Are you sure you want to remove the U2F device "${device.name}"?`)}
                </textBlock_1.default>
              </react_1.Fragment>}>
            <button_1.default size="small" priority="danger">
              <tooltip_1.default disabled={!isLastDevice} title={(0, locale_1.t)('Can not remove last U2F device')}>
                <icons_1.IconDelete size="xs"/>
              </tooltip_1.default>
            </button_1.default>
          </confirm_1.default>
        </Actions>
      </DevicePanelItem>);
    }
    return (<DevicePanelItem key={device.name}>
      <DeviceInformation>
        <DeviceNameInput type="text" value={deviceName} onChange={e => {
            setDeviceName(e.target.value);
        }}/>
        <FadedDateTime date={device.timestamp}/>
      </DeviceInformation>
      <Actions>
        <button_1.default priority="primary" size="small" onClick={() => {
            onRenameU2fDevice(device, deviceName);
            setEditting(false);
        }}>
          Rename Device
        </button_1.default>
      </Actions>

      <Actions>
        <button_1.default size="small" title="Cancel rename" onClick={() => {
            setDeviceName(device.name);
            setEditting(false);
        }}>
          <icons_1.IconClose size="xs"/>
        </button_1.default>
      </Actions>
    </DevicePanelItem>);
};
const DeviceNameInput = (0, styled_1.default)(input_1.default) `
  width: 50%;
  margin-right: ${(0, space_1.default)(2)};
`;
const DevicePanelItem = (0, styled_1.default)(panels_1.PanelItem) `
  padding: 0;
`;
const DeviceInformation = (0, styled_1.default)('div') `
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex: 1 1;
  height: 72px;

  padding: ${(0, space_1.default)(2)};
  padding-right: 0;
`;
const FadedDateTime = (0, styled_1.default)(dateTime_1.default) `
  font-size: ${p => p.theme.fontSizeRelativeSmall};
  opacity: 0.6;
`;
const Name = (0, styled_1.default)('div') `
  flex: 1;
`;
const Actions = (0, styled_1.default)('div') `
  margin: ${(0, space_1.default)(2)};
`;
const AddAnotherPanelItem = (0, styled_1.default)(panels_1.PanelItem) `
  justify-content: flex-end;
  padding: ${(0, space_1.default)(2)};
`;
exports.default = (0, styled_1.default)(U2fEnrolledDetails) `
  margin-top: ${(0, space_1.default)(4)};
`;
//# sourceMappingURL=u2fEnrolledDetails.jsx.map