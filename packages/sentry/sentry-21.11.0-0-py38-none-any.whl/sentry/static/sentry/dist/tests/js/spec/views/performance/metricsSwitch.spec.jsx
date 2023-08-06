Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = (0, tslib_1.__importDefault)(require("react"));
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const metricsSwitch_1 = require("app/views/performance/metricsSwitch");
function TestComponent() {
    const { isMetricsData } = (0, metricsSwitch_1.useMetricsSwitch)();
    return (<react_1.default.Fragment>
      <metricsSwitch_1.MetricsSwitch />
      {isMetricsData ? 'using metrics' : 'using transactions'}
    </react_1.default.Fragment>);
}
describe('MetricsSwitch', () => {
    it('MetricsSwitchContextContainer renders children', () => {
        (0, reactTestingLibrary_1.mountWithTheme)(<metricsSwitch_1.MetricsSwitchContextContainer>abc</metricsSwitch_1.MetricsSwitchContextContainer>, {
            organization: TestStubs.Organization(),
        });
        expect(reactTestingLibrary_1.screen.getByText('abc')).toBeInTheDocument();
    });
    it('MetricsSwitch is not visible to users without feature flag', () => {
        const { container } = (0, reactTestingLibrary_1.mountWithTheme)(<metricsSwitch_1.MetricsSwitch />, {
            organization: TestStubs.Organization(),
        });
        expect(container).toBeEmptyDOMElement();
    });
    it('toggles between transactions and metrics', () => {
        (0, reactTestingLibrary_1.mountWithTheme)(<metricsSwitch_1.MetricsSwitchContextContainer>
        <TestComponent />
      </metricsSwitch_1.MetricsSwitchContextContainer>, {
            organization: TestStubs.Organization({ features: ['metrics-performance-ui'] }),
        });
        expect(reactTestingLibrary_1.screen.getByText('using transactions')).toBeInTheDocument();
        reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByRole('checkbox'));
        expect(reactTestingLibrary_1.screen.getByText('using metrics')).toBeInTheDocument();
    });
});
//# sourceMappingURL=metricsSwitch.spec.jsx.map