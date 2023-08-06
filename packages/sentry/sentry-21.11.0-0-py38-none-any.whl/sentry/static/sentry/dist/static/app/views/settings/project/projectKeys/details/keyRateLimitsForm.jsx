Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const React = (0, tslib_1.__importStar)(require("react"));
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const sortBy_1 = (0, tslib_1.__importDefault)(require("lodash/sortBy"));
const feature_1 = (0, tslib_1.__importDefault)(require("app/components/acl/feature"));
const featureDisabled_1 = (0, tslib_1.__importDefault)(require("app/components/acl/featureDisabled"));
const panels_1 = require("app/components/panels");
const icons_1 = require("app/icons");
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const utils_1 = require("app/utils");
const formatters_1 = require("app/utils/formatters");
const input_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/forms/controls/input"));
const rangeSlider_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/forms/controls/rangeSlider"));
const form_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/forms/form"));
const formField_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/forms/formField"));
const PREDEFINED_RATE_LIMIT_VALUES = [
    0, 60, 300, 900, 3600, 7200, 14400, 21600, 43200, 86400,
];
function KeyRateLimitsForm({ data, disabled, params }) {
    function handleChangeWindow(onChange, onBlur, currentValueObj, value, event) {
        const valueObj = Object.assign(Object.assign({}, currentValueObj), { window: value });
        onChange(valueObj, event);
        onBlur(valueObj, event);
    }
    function handleChangeCount(callback, value, event) {
        const valueObj = Object.assign(Object.assign({}, value), { count: Number(event.target.value) });
        callback(valueObj, event);
    }
    function getAllowedRateLimitValues(currentRateLimit) {
        const { rateLimit } = data;
        const { window } = rateLimit !== null && rateLimit !== void 0 ? rateLimit : {};
        // The slider should display other values if they are set via the API, but still offer to select only the predefined values
        if ((0, utils_1.defined)(window)) {
            // If the API returns a value not found in the predefined values and the user selects another value through the UI,
            // he will no longer be able to reselect the "custom" value in the slider
            if (currentRateLimit !== window) {
                return PREDEFINED_RATE_LIMIT_VALUES;
            }
            // If the API returns a value not found in the predefined values, that value will be added to the slider
            if (!PREDEFINED_RATE_LIMIT_VALUES.includes(window)) {
                return (0, sortBy_1.default)([...PREDEFINED_RATE_LIMIT_VALUES, window]);
            }
        }
        return PREDEFINED_RATE_LIMIT_VALUES;
    }
    const { keyId, orgId, projectId } = params;
    const apiEndpoint = `/projects/${orgId}/${projectId}/keys/${keyId}/`;
    const disabledAlert = ({ features }) => (<featureDisabled_1.default alert={panels_1.PanelAlert} features={features} featureName={(0, locale_1.t)('Key Rate Limits')}/>);
    return (<form_1.default saveOnBlur apiEndpoint={apiEndpoint} apiMethod="PUT" initialData={data}>
      <feature_1.default features={['projects:rate-limits']} hookName="feature-disabled:rate-limits" renderDisabled={(_a) => {
            var { children } = _a, props = (0, tslib_1.__rest)(_a, ["children"]);
            return typeof children === 'function' &&
                children(Object.assign(Object.assign({}, props), { renderDisabled: disabledAlert }));
        }}>
        {({ hasFeature, features, organization, project, renderDisabled }) => (<panels_1.Panel>
            <panels_1.PanelHeader>{(0, locale_1.t)('Rate Limits')}</panels_1.PanelHeader>

            <panels_1.PanelBody>
              <panels_1.PanelAlert type="info" icon={<icons_1.IconFlag size="md"/>}>
                {(0, locale_1.t)(`Rate limits provide a flexible way to manage your error
                    volume. If you have a noisy project or environment you
                    can configure a rate limit for this key to reduce the
                    number of errors processed. To manage your transaction
                    volume, we recommend adjusting your sample rate in your
                    SDK configuration.`)}
              </panels_1.PanelAlert>
              {!hasFeature &&
                typeof renderDisabled === 'function' &&
                renderDisabled({
                    organization,
                    project,
                    features,
                    hasFeature,
                    children: null,
                })}
              <formField_1.default name="rateLimit" label={(0, locale_1.t)('Rate Limit')} disabled={disabled || !hasFeature} validate={({ form }) => {
                // TODO(TS): is validate actually doing anything because it's an unexpected prop
                const isValid = form &&
                    form.rateLimit &&
                    typeof form.rateLimit.count !== 'undefined' &&
                    typeof form.rateLimit.window !== 'undefined';
                if (isValid) {
                    return [];
                }
                return [['rateLimit', (0, locale_1.t)('Fill in both fields first')]];
            }} formatMessageValue={({ count, window }) => (0, locale_1.tct)('[errors] in [timeWindow]', {
                errors: (0, locale_1.tn)('%s error ', '%s errors ', count),
                timeWindow: window === 0 ? (0, locale_1.t)('no time window') : (0, formatters_1.getExactDuration)(window),
            })} help={(0, locale_1.t)('Apply a rate limit to this credential to cap the amount of errors accepted during a time window.')} inline={false}>
                {({ onChange, onBlur, value }) => {
                const window = typeof value === 'object' ? value.window : undefined;
                return (<RateLimitRow>
                      <input_1.default type="number" name="rateLimit.count" min={0} value={typeof value === 'object' ? value.count : undefined} placeholder={(0, locale_1.t)('Count')} disabled={disabled || !hasFeature} onChange={event => handleChangeCount(onChange, value, event)} onBlur={event => handleChangeCount(onBlur, value, event)}/>
                      <EventsIn>{(0, locale_1.t)('event(s) in')}</EventsIn>
                      <rangeSlider_1.default name="rateLimit.window" allowedValues={getAllowedRateLimitValues(window)} value={window} placeholder={(0, locale_1.t)('Window')} formatLabel={rangeValue => {
                        if (typeof rangeValue === 'number') {
                            if (rangeValue === 0) {
                                return (0, locale_1.t)('None');
                            }
                            return (0, formatters_1.getExactDuration)(rangeValue);
                        }
                        return undefined;
                    }} disabled={disabled || !hasFeature} onChange={(rangeValue, event) => handleChangeWindow(onChange, onBlur, value, Number(rangeValue), event)}/>
                    </RateLimitRow>);
            }}
              </formField_1.default>
            </panels_1.PanelBody>
          </panels_1.Panel>)}
      </feature_1.default>
    </form_1.default>);
}
exports.default = KeyRateLimitsForm;
const RateLimitRow = (0, styled_1.default)('div') `
  display: grid;
  grid-template-columns: 2fr 1fr 2fr;
  align-items: center;
  grid-gap: ${(0, space_1.default)(1)};
`;
const EventsIn = (0, styled_1.default)('small') `
  font-size: ${p => p.theme.fontSizeRelativeSmall};
  text-align: center;
  white-space: nowrap;
`;
//# sourceMappingURL=keyRateLimitsForm.jsx.map