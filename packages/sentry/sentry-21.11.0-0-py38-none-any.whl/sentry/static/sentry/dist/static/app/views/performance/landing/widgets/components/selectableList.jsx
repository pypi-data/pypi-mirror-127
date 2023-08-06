Object.defineProperty(exports, "__esModule", { value: true });
exports.ListClose = exports.WidgetEmptyStateWarning = exports.GrowLink = exports.Subtitle = exports.RightAlignedCell = void 0;
const tslib_1 = require("tslib");
const react_1 = (0, tslib_1.__importDefault)(require("react"));
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const emptyStateWarning_1 = (0, tslib_1.__importDefault)(require("app/components/emptyStateWarning"));
const link_1 = (0, tslib_1.__importDefault)(require("app/components/links/link"));
const radio_1 = (0, tslib_1.__importDefault)(require("app/components/radio"));
const tooltip_1 = (0, tslib_1.__importDefault)(require("app/components/tooltip"));
const icons_1 = require("app/icons");
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const radioGroup_1 = require("app/views/settings/components/forms/controls/radioGroup");
function SelectableList(props) {
    return (<div>
      {props.items.map((item, index) => (<SelectableItem {...props} isSelected={index === props.selectedIndex} currentIndex={index} key={index}>
          {item()}
        </SelectableItem>))}
    </div>);
}
exports.default = SelectableList;
function SelectableItem({ isSelected, currentIndex: index, children, setSelectedIndex, radioColor, }) {
    return (<ListItemContainer>
      <ItemRadioContainer color={radioColor !== null && radioColor !== void 0 ? radioColor : ''}>
        <radioGroup_1.RadioLineItem index={index} role="radio">
          <radio_1.default checked={isSelected} onChange={() => setSelectedIndex(index)}/>
        </radioGroup_1.RadioLineItem>
      </ItemRadioContainer>
      {children}
    </ListItemContainer>);
}
exports.RightAlignedCell = (0, styled_1.default)('div') `
  text-align: right;
`;
exports.Subtitle = (0, styled_1.default)('span') `
  color: ${p => p.theme.gray300};
  font-size: ${p => p.theme.fontSizeMedium};
`;
exports.GrowLink = (0, styled_1.default)(link_1.default) `
  flex-grow: 1;
`;
const WidgetEmptyStateWarning = () => {
    return <StyledEmptyStateWarning small>{(0, locale_1.t)('No results')}</StyledEmptyStateWarning>;
};
exports.WidgetEmptyStateWarning = WidgetEmptyStateWarning;
function ListClose(props) {
    return (<CloseContainer>
      <tooltip_1.default title={(0, locale_1.t)('Exclude this transaction from the search filter.')}>
        <StyledIconClose onClick={() => {
            props.onClick();
            props.setSelectListIndex(0);
        }}/>
      </tooltip_1.default>
    </CloseContainer>);
}
exports.ListClose = ListClose;
const CloseContainer = (0, styled_1.default)('div') `
  display: flex;
  align-items: center;
  justify-content: center;
  padding-left: ${(0, space_1.default)(1)};
`;
const StyledIconClose = (0, styled_1.default)(icons_1.IconClose) `
  cursor: pointer;
  color: ${p => p.theme.gray200};

  &:hover {
    color: ${p => p.theme.gray300};
  }
`;
const StyledEmptyStateWarning = (0, styled_1.default)(emptyStateWarning_1.default) `
  min-height: 300px;
  justify-content: center;
`;
const ListItemContainer = (0, styled_1.default)('div') `
  display: flex;

  border-top: 1px solid ${p => p.theme.border};
  padding: ${(0, space_1.default)(1)} ${(0, space_1.default)(2)};
`;
const ItemRadioContainer = (0, styled_1.default)('div') `
  grid-row: 1/3;
  input {
    cursor: pointer;
  }
  input:checked::after {
    background-color: ${p => p.color};
  }
`;
//# sourceMappingURL=selectableList.jsx.map