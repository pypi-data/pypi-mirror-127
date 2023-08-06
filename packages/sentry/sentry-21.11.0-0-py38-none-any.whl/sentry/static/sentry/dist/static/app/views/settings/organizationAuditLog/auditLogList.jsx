Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const userAvatar_1 = (0, tslib_1.__importDefault)(require("app/components/avatar/userAvatar"));
const dateTime_1 = (0, tslib_1.__importDefault)(require("app/components/dateTime"));
const selectField_1 = (0, tslib_1.__importDefault)(require("app/components/forms/selectField"));
const pagination_1 = (0, tslib_1.__importDefault)(require("app/components/pagination"));
const panels_1 = require("app/components/panels");
const tooltip_1 = (0, tslib_1.__importDefault)(require("app/components/tooltip"));
const locale_1 = require("app/locale");
const overflowEllipsis_1 = (0, tslib_1.__importDefault)(require("app/styles/overflowEllipsis"));
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const dates_1 = require("app/utils/dates");
const settingsPageHeader_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/settingsPageHeader"));
const avatarStyle = {
    width: 36,
    height: 36,
    marginRight: 8,
};
const AuditLogList = ({ isLoading, pageLinks, entries, eventType, eventTypes, onEventSelect, }) => {
    const is24Hours = (0, dates_1.use24Hours)();
    const hasEntries = entries && entries.length > 0;
    const ipv4Length = 15;
    const options = [
        { value: '', label: (0, locale_1.t)('Any action'), clearableVaue: false },
        ...eventTypes.map(type => ({ label: type, value: type, clearableValue: false })),
    ];
    const action = (<form>
      <selectField_1.default name="event" onChange={onEventSelect} value={eventType} style={{ width: 250 }} options={options}/>
    </form>);
    return (<div>
      <settingsPageHeader_1.default title={(0, locale_1.t)('Audit Log')} action={action}/>
      <panels_1.PanelTable headers={[(0, locale_1.t)('Member'), (0, locale_1.t)('Action'), (0, locale_1.t)('IP'), (0, locale_1.t)('Time')]} isEmpty={!hasEntries} emptyMessage={(0, locale_1.t)('No audit entries available')} isLoading={isLoading}>
        {entries === null || entries === void 0 ? void 0 : entries.map(entry => (<react_1.Fragment key={entry.id}>
            <UserInfo>
              <div>
                {entry.actor.email && (<userAvatar_1.default style={avatarStyle} user={entry.actor}/>)}
              </div>
              <NameContainer>
                <Name data-test-id="actor-name">
                  {entry.actor.isSuperuser
                ? (0, locale_1.t)('%s (Sentry Staff)', entry.actor.name)
                : entry.actor.name}
                </Name>
                <Note>{entry.note}</Note>
              </NameContainer>
            </UserInfo>
            <FlexCenter>
              <MonoDetail>{entry.event}</MonoDetail>
            </FlexCenter>
            <FlexCenter>
              {entry.ipAddress && (<IpAddressOverflow>
                  <tooltip_1.default title={entry.ipAddress} disabled={entry.ipAddress.length <= ipv4Length}>
                    <MonoDetail>{entry.ipAddress}</MonoDetail>
                  </tooltip_1.default>
                </IpAddressOverflow>)}
            </FlexCenter>
            <TimestampInfo>
              <dateTime_1.default dateOnly date={entry.dateCreated}/>
              <dateTime_1.default timeOnly format={is24Hours ? 'HH:mm zz' : 'LT zz'} date={entry.dateCreated}/>
            </TimestampInfo>
          </react_1.Fragment>))}
      </panels_1.PanelTable>
      {pageLinks && <pagination_1.default pageLinks={pageLinks}/>}
    </div>);
};
const UserInfo = (0, styled_1.default)('div') `
  display: flex;
  align-items: center;
  line-height: 1.2;
  font-size: 13px;
  min-width: 250px;
`;
const NameContainer = (0, styled_1.default)('div') `
  display: flex;
  flex-direction: column;
  justify-content: center;
`;
const Name = (0, styled_1.default)('div') `
  font-weight: 600;
  font-size: 15px;
`;
const Note = (0, styled_1.default)('div') `
  font-size: 13px;
  word-break: break-word;
`;
const FlexCenter = (0, styled_1.default)('div') `
  display: flex;
  align-items: center;
`;
const IpAddressOverflow = (0, styled_1.default)('div') `
  ${overflowEllipsis_1.default};
  min-width: 90px;
`;
const MonoDetail = (0, styled_1.default)('code') `
  font-size: ${p => p.theme.fontSizeMedium};
  white-space: no-wrap;
`;
const TimestampInfo = (0, styled_1.default)('div') `
  display: grid;
  grid-template-rows: auto auto;
  grid-gap: ${(0, space_1.default)(1)};
  font-size: ${p => p.theme.fontSizeMedium};
`;
exports.default = AuditLogList;
//# sourceMappingURL=auditLogList.jsx.map