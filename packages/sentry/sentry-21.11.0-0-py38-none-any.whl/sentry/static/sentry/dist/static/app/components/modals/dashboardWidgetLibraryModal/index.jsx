Object.defineProperty(exports, "__esModule", { value: true });
exports.modalCss = exports.TAB = void 0;
const tslib_1 = require("tslib");
const React = (0, tslib_1.__importStar)(require("react"));
const react_1 = require("react");
const react_2 = require("@emotion/react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const tagDeprecated_1 = (0, tslib_1.__importDefault)(require("app/components/tagDeprecated"));
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const button_1 = (0, tslib_1.__importDefault)(require("../../button"));
const buttonBar_1 = (0, tslib_1.__importDefault)(require("../../buttonBar"));
const customTab_1 = (0, tslib_1.__importDefault)(require("./customTab"));
const libraryTab_1 = (0, tslib_1.__importDefault)(require("./libraryTab"));
var TAB;
(function (TAB) {
    TAB["Library"] = "library";
    TAB["Custom"] = "custom";
})(TAB = exports.TAB || (exports.TAB = {}));
function DashboardWidgetLibraryModal({ Header, Body, Footer, dashboard, closeModal, onAddWidget, }) {
    const [tab, setTab] = (0, react_1.useState)(TAB.Library);
    const [selectedWidgets, setSelectedWidgets] = (0, react_1.useState)([]);
    const [errored, setErrored] = (0, react_1.useState)(false);
    function handleSubmit() {
        onAddWidget([...dashboard.widgets, ...selectedWidgets]);
        closeModal();
    }
    return (<React.Fragment>
      <Header closeButton>
        <h4>{(0, locale_1.t)('Add Widget')}</h4>
      </Header>
      <Body>
        <StyledButtonBar active={tab}>
          <button_1.default barId={TAB.Library} onClick={() => setTab(TAB.Library)}>
            {(0, locale_1.t)('Library')}
          </button_1.default>
          <button_1.default barId={TAB.Custom} onClick={() => setTab(TAB.Custom)}>
            {(0, locale_1.t)('Custom')}
          </button_1.default>
        </StyledButtonBar>
        {tab === TAB.Library ? (<libraryTab_1.default selectedWidgets={selectedWidgets} errored={errored} setSelectedWidgets={setSelectedWidgets} setErrored={setErrored}/>) : (<customTab_1.default />)}
      </Body>
      <Footer>
        <FooterButtonbar gap={1}>
          <button_1.default external href="https://docs.sentry.io/product/dashboards/custom-dashboards/#widget-builder">
            {(0, locale_1.t)('Read the docs')}
          </button_1.default>
          <div>
            <SelectedBadge data-test-id="selected-badge">
              {`${selectedWidgets.length} Selected`}
            </SelectedBadge>
            <button_1.default data-test-id="confirm-widgets" priority="primary" type="button" onClick={(event) => {
            event.preventDefault();
            if (!!!selectedWidgets.length) {
                setErrored(true);
                return;
            }
            handleSubmit();
        }}>
              {(0, locale_1.t)('Confirm')}
            </button_1.default>
          </div>
        </FooterButtonbar>
      </Footer>
    </React.Fragment>);
}
exports.modalCss = (0, react_2.css) `
  width: 100%;
  max-width: 700px;
  margin: 70px auto;
`;
const StyledButtonBar = (0, styled_1.default)(buttonBar_1.default) `
  grid-template-columns: repeat(2, minmax(0, 1fr));
  margin-bottom: ${(0, space_1.default)(1)};
`;
const FooterButtonbar = (0, styled_1.default)(buttonBar_1.default) `
  justify-content: space-between;
  width: 100%;
`;
const SelectedBadge = (0, styled_1.default)(tagDeprecated_1.default) `
  padding: 3px ${(0, space_1.default)(0.75)};
  display: inline-flex;
  align-items: center;
  margin-left: ${(0, space_1.default)(1)};
  margin-right: ${(0, space_1.default)(1)};
  top: -1px;
`;
exports.default = DashboardWidgetLibraryModal;
//# sourceMappingURL=index.jsx.map