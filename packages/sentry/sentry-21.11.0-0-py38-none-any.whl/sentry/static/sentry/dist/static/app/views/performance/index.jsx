Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const feature_1 = (0, tslib_1.__importDefault)(require("app/components/acl/feature"));
const alert_1 = (0, tslib_1.__importDefault)(require("app/components/alert"));
const locale_1 = require("app/locale");
const organization_1 = require("app/styles/organization");
const withOrganization_1 = (0, tslib_1.__importDefault)(require("app/utils/withOrganization"));
const metricsSwitch_1 = require("./metricsSwitch");
class PerformanceContainer extends react_1.Component {
    renderNoAccess() {
        return (<organization_1.PageContent>
        <alert_1.default type="warning">{(0, locale_1.t)("You don't have access to this feature")}</alert_1.default>
      </organization_1.PageContent>);
    }
    render() {
        const { organization, children } = this.props;
        return (<feature_1.default hookName="feature-disabled:performance-page" features={['performance-view']} organization={organization} renderDisabled={this.renderNoAccess}>
        <metricsSwitch_1.MetricsSwitchContextContainer>{children}</metricsSwitch_1.MetricsSwitchContextContainer>
      </feature_1.default>);
    }
}
exports.default = (0, withOrganization_1.default)(PerformanceContainer);
//# sourceMappingURL=index.jsx.map