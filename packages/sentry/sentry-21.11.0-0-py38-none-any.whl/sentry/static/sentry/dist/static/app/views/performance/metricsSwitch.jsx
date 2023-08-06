Object.defineProperty(exports, "__esModule", { value: true });
exports.useMetricsSwitch = exports.MetricsSwitchContextContainer = exports.MetricsSwitch = void 0;
const tslib_1 = require("tslib");
const react_1 = require("react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const feature_1 = (0, tslib_1.__importDefault)(require("app/components/acl/feature"));
const switchButton_1 = (0, tslib_1.__importDefault)(require("app/components/switchButton"));
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const localStorage_1 = (0, tslib_1.__importDefault)(require("app/utils/localStorage"));
const useOrganization_1 = (0, tslib_1.__importDefault)(require("app/utils/useOrganization"));
const FEATURE_FLAG = 'metrics-performance-ui';
/**
 * This is a temporary component used for debugging metrics data on performance pages.
 * Visible only to small amount of internal users.
 */
function MetricsSwitch() {
    const organization = (0, useOrganization_1.default)();
    const { isMetricsData, setIsMetricsData } = useMetricsSwitch();
    return (<feature_1.default features={[FEATURE_FLAG]} organization={organization}>
      <Label>
        {(0, locale_1.t)('Metrics Data')}
        <switchButton_1.default isActive={isMetricsData} toggle={() => setIsMetricsData(!isMetricsData)} size="lg"/>
      </Label>
    </feature_1.default>);
}
exports.MetricsSwitch = MetricsSwitch;
const Label = (0, styled_1.default)('label') `
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 0;
  gap: ${(0, space_1.default)(1)};
  font-weight: normal;
`;
const MetricsSwitchContext = (0, react_1.createContext)({
    isMetricsData: false,
    setIsMetricsData: (_isMetricsData) => { },
});
function MetricsSwitchContextContainer({ children }) {
    const organization = (0, useOrganization_1.default)();
    const localStorageKey = `metrics-performance:${organization.slug}`;
    const [isMetricsData, setIsMetricsData] = (0, react_1.useState)(localStorage_1.default.getItem(localStorageKey) === 'true');
    function handleSetIsMetricsData(value) {
        localStorage_1.default.setItem(localStorageKey, value.toString());
        setIsMetricsData(value);
    }
    return (<MetricsSwitchContext.Provider value={{
            isMetricsData: isMetricsData && organization.features.includes(FEATURE_FLAG),
            setIsMetricsData: handleSetIsMetricsData,
        }}>
      {children}
    </MetricsSwitchContext.Provider>);
}
exports.MetricsSwitchContextContainer = MetricsSwitchContextContainer;
function useMetricsSwitch() {
    const contextValue = (0, react_1.useContext)(MetricsSwitchContext);
    return contextValue;
}
exports.useMetricsSwitch = useMetricsSwitch;
//# sourceMappingURL=metricsSwitch.jsx.map