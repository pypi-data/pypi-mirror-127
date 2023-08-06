Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const React = (0, tslib_1.__importStar)(require("react"));
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const alert_1 = (0, tslib_1.__importDefault)(require("app/components/alert"));
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const data_1 = require("app/views/dashboardsV2/widgetLibrary/data");
const widgetCard_1 = (0, tslib_1.__importDefault)(require("app/views/dashboardsV2/widgetLibrary/widgetCard"));
function DashboardWidgetLibraryTab({ selectedWidgets, errored, setSelectedWidgets, setErrored, }) {
    return (<React.Fragment>
      {errored && !!!selectedWidgets.length ? (<alert_1.default type="error">
          {(0, locale_1.t)('Please select at least one Widget from our Library. Alternatively, you can build a custom widget from scratch.')}
        </alert_1.default>) : null}
      <Title>{(0, locale_1.t)('%s WIDGETS', data_1.DEFAULT_WIDGETS.length)}</Title>
      <ScrollGrid>
        <WidgetLibraryGrid>
          {data_1.DEFAULT_WIDGETS.map(widgetCard => {
            return (<widgetCard_1.default key={widgetCard.title} widget={widgetCard} selectedWidgets={selectedWidgets} setSelectedWidgets={setSelectedWidgets} setErrored={setErrored}/>);
        })}
        </WidgetLibraryGrid>
      </ScrollGrid>
    </React.Fragment>);
}
const WidgetLibraryGrid = (0, styled_1.default)('div') `
  display: grid;
  grid-template-columns: repeat(2, minmax(100px, 1fr));
  grid-template-rows: repeat(2, max-content);
  grid-gap: ${(0, space_1.default)(1)};
`;
const ScrollGrid = (0, styled_1.default)('div') `
  max-height: 550px;
  overflow: scroll;
  -ms-overflow-style: none;
  scrollbar-width: none;
  &::-webkit-scrollbar {
    display: none;
  }
`;
const Title = (0, styled_1.default)('h3') `
  margin-bottom: ${(0, space_1.default)(1)};
  padding: 0 !important;
  font-size: ${p => p.theme.fontSizeSmall};
  text-transform: uppercase;
  color: ${p => p.theme.gray300};
`;
exports.default = DashboardWidgetLibraryTab;
//# sourceMappingURL=libraryTab.jsx.map