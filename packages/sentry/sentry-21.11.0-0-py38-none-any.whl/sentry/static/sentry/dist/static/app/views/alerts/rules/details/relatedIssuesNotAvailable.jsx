Object.defineProperty(exports, "__esModule", { value: true });
exports.RelatedIssuesNotAvailable = exports.RELATED_ISSUES_QUERY_ERROR = void 0;
const tslib_1 = require("tslib");
const React = (0, tslib_1.__importStar)(require("react"));
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const feature_1 = (0, tslib_1.__importDefault)(require("app/components/acl/feature"));
const alert_1 = (0, tslib_1.__importDefault)(require("app/components/alert"));
const button_1 = (0, tslib_1.__importDefault)(require("app/components/button"));
const panels_1 = require("app/components/panels");
const icons_1 = require("app/icons");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
exports.RELATED_ISSUES_QUERY_ERROR = 'Error parsing search query: Boolean statements containing "OR" or "AND" are not supported in this search';
/**
 * Renders an Alert box of type "info" for boolean queries in alert details. Renders a discover link if the feature is available.
 */
const RelatedIssuesNotAvailable = ({ buttonTo, buttonText }) => (<StyledAlert type="info">
    <Content>
      <icons_1.IconInfo size="lg"/>
      <div data-test-id="loading-error-message">
        Related Issues unavailable for this alert.
      </div>
      <feature_1.default features={['discover-basic']}>
        <button_1.default type="button" priority="default" size="small" to={buttonTo}>
          {buttonText}
        </button_1.default>
      </feature_1.default>
    </Content>
  </StyledAlert>);
exports.RelatedIssuesNotAvailable = RelatedIssuesNotAvailable;
const StyledAlert = (0, styled_1.default)(alert_1.default) `
  ${ /* sc-selector */panels_1.Panel} & {
    border-radius: 0;
    border-width: 1px 0;
  }
`;
const Content = (0, styled_1.default)('div') `
  display: grid;
  grid-gap: ${(0, space_1.default)(1)};
  grid-template-columns: min-content auto max-content;
  align-items: center;
`;
//# sourceMappingURL=relatedIssuesNotAvailable.jsx.map