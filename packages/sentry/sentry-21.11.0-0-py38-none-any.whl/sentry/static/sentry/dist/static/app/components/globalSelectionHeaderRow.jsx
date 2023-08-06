Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const React = (0, tslib_1.__importStar)(require("react"));
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const checkboxFancy_1 = (0, tslib_1.__importDefault)(require("app/components/checkboxFancy/checkboxFancy"));
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const defaultRenderCheckbox = ({ checkbox }) => checkbox;
function GlobalSelectionHeaderRow(_a) {
    var { checked, onCheckClick, children, multi = true, renderCheckbox = defaultRenderCheckbox } = _a, props = (0, tslib_1.__rest)(_a, ["checked", "onCheckClick", "children", "multi", "renderCheckbox"]);
    const checkbox = <checkboxFancy_1.default isDisabled={!multi} isChecked={checked}/>;
    return (<Container isChecked={checked} {...props}>
      <Content multi={multi}>{children}</Content>
      <CheckboxHitbox onClick={multi ? onCheckClick : undefined}>
        {renderCheckbox({ checkbox, checked })}
      </CheckboxHitbox>
    </Container>);
}
const Container = (0, styled_1.default)('div') `
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 14px;
  font-weight: 400;
  padding-left: ${(0, space_1.default)(0.5)};
  height: ${p => p.theme.headerSelectorRowHeight}px;
  flex-shrink: 0;

  ${checkboxFancy_1.default} {
    opacity: ${p => (p.isChecked ? 1 : 0.33)};
  }

  &:hover ${checkboxFancy_1.default} {
    opacity: 1;
  }
`;
const Content = (0, styled_1.default)('div') `
  display: flex;
  flex-shrink: 1;
  overflow: hidden;
  align-items: center;
  height: 100%;
  flex-grow: 1;
  user-select: none;

  &:hover {
    text-decoration: ${p => (p.multi ? 'underline' : null)};
    color: ${p => (p.multi ? p.theme.blue300 : null)};
  }
`;
const CheckboxHitbox = (0, styled_1.default)('div') `
  margin: 0 -${(0, space_1.default)(1)} 0 0; /* pushes the click box to be flush with the edge of the menu */
  padding: 0 ${(0, space_1.default)(1.5)};
  height: 100%;
  display: flex;
  justify-content: flex-end;
  align-items: center;
`;
exports.default = GlobalSelectionHeaderRow;
//# sourceMappingURL=globalSelectionHeaderRow.jsx.map