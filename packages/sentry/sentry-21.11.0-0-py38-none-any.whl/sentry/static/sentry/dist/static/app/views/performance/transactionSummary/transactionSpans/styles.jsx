Object.defineProperty(exports, "__esModule", { value: true });
exports.SpanDurationBar = exports.emptyValue = exports.SpanLabelContainer = exports.HeaderItemContainer = exports.HeaderItem = exports.LowerPanel = exports.UpperPanel = exports.Actions = void 0;
const tslib_1 = require("tslib");
const react_1 = require("@emotion/react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const styles_1 = require("app/components/charts/styles");
const panels_1 = require("app/components/panels");
const rowBar_1 = require("app/components/performance/waterfall/rowBar");
const utils_1 = require("app/components/performance/waterfall/utils");
const tooltip_1 = (0, tslib_1.__importDefault)(require("app/components/tooltip"));
const icons_1 = require("app/icons");
const locale_1 = require("app/locale");
const overflowEllipsis_1 = (0, tslib_1.__importDefault)(require("app/styles/overflowEllipsis"));
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const formatters_1 = require("app/utils/formatters");
const utils_2 = require("../../utils");
exports.Actions = (0, styled_1.default)('div') `
  display: grid;
  grid-gap: ${(0, space_1.default)(2)};
  grid-template-columns: min-content 1fr min-content;
  align-items: center;
`;
exports.UpperPanel = (0, styled_1.default)(panels_1.Panel) `
  padding: ${(0, space_1.default)(1.5)} ${(0, space_1.default)(3)};
  margin-top: ${(0, space_1.default)(3)};
  margin-bottom: 0;
  border-bottom: 0;
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;

  display: grid;

  grid-template-columns: 1fr;
  grid-gap: ${(0, space_1.default)(1.5)};

  @media (min-width: ${p => p.theme.breakpoints[1]}) {
    grid-template-columns: auto repeat(3, max-content);
    grid-gap: 48px;
  }
`;
exports.LowerPanel = (0, styled_1.default)('div') `
  > div {
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
`;
function HeaderItem(props) {
    const { label, value, align, isSortKey } = props;
    const theme = (0, react_1.useTheme)();
    return (<exports.HeaderItemContainer align={align}>
      {isSortKey && (<StyledIconArrow data-test-id="span-sort-arrow" size="xs" color={theme.subText} direction="down"/>)}
      <styles_1.SectionHeading>{label}</styles_1.SectionHeading>
      <SectionValue>{value}</SectionValue>
    </exports.HeaderItemContainer>);
}
exports.HeaderItem = HeaderItem;
exports.HeaderItemContainer = (0, styled_1.default)('div') `
  ${overflowEllipsis_1.default};

  @media (min-width: ${p => p.theme.breakpoints[1]}) {
    text-align: ${p => p.align};
  }
`;
const StyledIconArrow = (0, styled_1.default)(icons_1.IconArrow) `
  margin-right: ${(0, space_1.default)(0.5)};
`;
const SectionValue = (0, styled_1.default)('h1') `
  font-size: ${p => p.theme.headerFontSize};
  font-weight: normal;
  line-height: 1.2;
  color: ${p => p.theme.textColor};
  margin-bottom: 0;
`;
exports.SpanLabelContainer = (0, styled_1.default)('div') `
  ${overflowEllipsis_1.default};
`;
const EmptyValueContainer = (0, styled_1.default)('span') `
  color: ${p => p.theme.gray300};
`;
exports.emptyValue = <EmptyValueContainer>{(0, locale_1.t)('n/a')}</EmptyValueContainer>;
const DurationBar = (0, styled_1.default)('div') `
  position: relative;
  display: flex;
  top: ${(0, space_1.default)(0.5)};
  background-color: ${p => p.theme.gray100};
`;
const DurationBarSection = (0, styled_1.default)(rowBar_1.RowRectangle) `
  position: relative;
  width: 100%;
  top: 0;
`;
function SpanDurationBar(props) {
    const { spanOp, spanDuration, transactionDuration } = props;
    const widthPercentage = spanDuration / transactionDuration;
    const position = widthPercentage < 0.7 ? 'right' : 'inset';
    return (<DurationBar>
      <div style={{ width: (0, utils_1.toPercent)(widthPercentage) }}>
        <tooltip_1.default title={(0, formatters_1.formatPercentage)(widthPercentage)} containerDisplayMode="block">
          <DurationBarSection spanBarHatch={false} style={{ backgroundColor: (0, utils_1.pickBarColor)(spanOp) }}>
            <rowBar_1.DurationPill durationDisplay={position} showDetail={false} spanBarHatch={false}>
              <utils_2.PerformanceDuration abbreviation milliseconds={spanDuration}/>
            </rowBar_1.DurationPill>
          </DurationBarSection>
        </tooltip_1.default>
      </div>
    </DurationBar>);
}
exports.SpanDurationBar = SpanDurationBar;
//# sourceMappingURL=styles.jsx.map