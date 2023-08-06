Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const React = (0, tslib_1.__importStar)(require("react"));
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const button_1 = (0, tslib_1.__importDefault)(require("app/components/button"));
const card_1 = (0, tslib_1.__importDefault)(require("app/components/card"));
const icons_1 = require("app/icons");
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const utils_1 = require("../utils");
function WidgetLibraryCard({ selectedWidgets, widget, setSelectedWidgets, setErrored, }) {
    const selectButton = (<StyledButton type="button" icon={<icons_1.IconAdd size="small" isCircled color="gray300"/>} onClick={() => {
            const updatedWidgets = selectedWidgets.slice().concat(widget);
            setErrored(false);
            setSelectedWidgets(updatedWidgets);
        }}>
      {(0, locale_1.t)('Select')}
    </StyledButton>);
    const selectedButton = (<StyledButton type="button" icon={<icons_1.IconCheckmark size="small" isCircled color="gray300"/>} onClick={() => {
            const updatedWidgets = selectedWidgets.filter(selected => widget !== selected);
            setSelectedWidgets(updatedWidgets);
        }} priority="primary">
      {(0, locale_1.t)('Selected')}
    </StyledButton>);
    return (<card_1.default>
      <CardHeader>
        <CardContent>
          <Title>{widget.title}</Title>
        </CardContent>
      </CardHeader>
      <CardBody>
        <WidgetImage src={(0, utils_1.miniWidget)(widget.displayType)}/>
      </CardBody>
      <CardFooter>
        {selectedWidgets.includes(widget) ? selectedButton : selectButton}
      </CardFooter>
    </card_1.default>);
}
const CardContent = (0, styled_1.default)('div') `
  flex-grow: 1;
  overflow: hidden;
  margin-right: ${(0, space_1.default)(1)};
`;
const CardHeader = (0, styled_1.default)('div') `
  display: flex;
  padding: ${(0, space_1.default)(1.5)} ${(0, space_1.default)(2)};
`;
const Title = (0, styled_1.default)('div') `
  color: ${p => p.theme.textColor};
`;
const CardBody = (0, styled_1.default)('div') `
  background: ${p => p.theme.gray100};
  padding: ${(0, space_1.default)(1.5)} ${(0, space_1.default)(2)};
  max-height: 150px;
  min-height: 150px;
  overflow: hidden;
`;
const CardFooter = (0, styled_1.default)('div') `
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: ${(0, space_1.default)(1)} ${(0, space_1.default)(2)};
`;
const StyledButton = (0, styled_1.default)(button_1.default) `
  width: 100%;
  vertical-align: middle;
  > span:first-child {
    padding: 8px 16px;
  }
`;
const WidgetImage = (0, styled_1.default)('img') `
  width: 100%;
  height: 100%;
`;
exports.default = WidgetLibraryCard;
//# sourceMappingURL=widgetCard.jsx.map