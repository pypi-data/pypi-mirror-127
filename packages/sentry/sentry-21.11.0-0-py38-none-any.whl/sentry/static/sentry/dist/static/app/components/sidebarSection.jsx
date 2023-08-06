Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const React = (0, tslib_1.__importStar)(require("react"));
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
/**
 * Used to add the new sidebar section on a page.
 */
function SidebarSection(_a) {
    var { title, children, icon } = _a, props = (0, tslib_1.__rest)(_a, ["title", "children", "icon"]);
    return (<Wrapper>
      <Heading {...props}>
        {title}
        {icon && <IconWrapper>{icon}</IconWrapper>}
      </Heading>
      <SectionContent>{children}</SectionContent>
    </Wrapper>);
}
const Wrapper = (0, styled_1.default)('div') `
  margin-bottom: ${(0, space_1.default)(3)};
`;
const Heading = (0, styled_1.default)('h6') `
  color: ${p => p.theme.textColor};
  display: flex;
  font-size: ${p => p.theme.fontSizeMedium};
  margin: ${(0, space_1.default)(1)} 0;
`;
const IconWrapper = (0, styled_1.default)('div') `
  color: ${p => p.theme.subText};
  margin-left: ${(0, space_1.default)(0.5)};
`;
const SectionContent = (0, styled_1.default)('div') `
  color: ${p => p.theme.subText};
`;
exports.default = SidebarSection;
//# sourceMappingURL=sidebarSection.jsx.map