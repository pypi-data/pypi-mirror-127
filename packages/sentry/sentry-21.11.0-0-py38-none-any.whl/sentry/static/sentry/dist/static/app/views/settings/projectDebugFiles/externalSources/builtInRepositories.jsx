Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const indicator_1 = require("app/actionCreators/indicator");
const projectActions_1 = (0, tslib_1.__importDefault)(require("app/actions/projectActions"));
const access_1 = (0, tslib_1.__importDefault)(require("app/components/acl/access"));
const panels_1 = require("app/components/panels");
const locale_1 = require("app/locale");
const selectField_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/forms/selectField"));
function BuiltInRepositories({ api, organization, builtinSymbolSourceOptions, builtinSymbolSources, projSlug, }) {
    // If the project details object has an unknown built-in source, this will be filtered here.
    // This prevents the UI from showing the wrong feedback message when updating the field
    const validBuiltInSymbolSources = builtinSymbolSources.filter(builtinSymbolSource => builtinSymbolSourceOptions.find(({ sentry_key }) => sentry_key === builtinSymbolSource));
    function getRequestMessages(builtinSymbolSourcesQuantity) {
        if (builtinSymbolSourcesQuantity === 0) {
            return {
                errorMessage: (0, locale_1.t)('This field requires at least one built-in repository'),
            };
        }
        if (builtinSymbolSourcesQuantity > validBuiltInSymbolSources.length) {
            return {
                successMessage: (0, locale_1.t)('Successfully added built-in repository'),
                errorMessage: (0, locale_1.t)('An error occurred while adding new built-in repository'),
            };
        }
        return {
            successMessage: (0, locale_1.t)('Successfully removed built-in repository'),
            errorMessage: (0, locale_1.t)('An error occurred while removing built-in repository'),
        };
    }
    function handleChange(value) {
        return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
            const { successMessage, errorMessage } = getRequestMessages((value !== null && value !== void 0 ? value : []).length);
            try {
                const updatedProjectDetails = yield api.requestPromise(`/projects/${organization.slug}/${projSlug}/`, {
                    method: 'PUT',
                    data: {
                        builtinSymbolSources: value,
                    },
                });
                projectActions_1.default.updateSuccess(updatedProjectDetails);
                (0, indicator_1.addSuccessMessage)(successMessage);
            }
            catch (_a) {
                (0, indicator_1.addErrorMessage)(errorMessage);
            }
        });
    }
    return (<panels_1.Panel>
      <panels_1.PanelHeader>{(0, locale_1.t)('Built-in Repositories')}</panels_1.PanelHeader>
      <panels_1.PanelBody>
        <access_1.default access={['project:write']}>
          {({ hasAccess }) => (<StyledSelectField disabled={!hasAccess} name="builtinSymbolSources" label={(0, locale_1.t)('Built-in Repositories')} help={(0, locale_1.t)('Configures which built-in repositories Sentry should use to resolve debug files.')} placeholder={(0, locale_1.t)('Select built-in repository')} value={validBuiltInSymbolSources} onChange={handleChange} options={builtinSymbolSourceOptions
                .filter(source => !source.hidden)
                .map(source => ({
                value: source.sentry_key,
                label: source.name,
            }))} getValue={value => (value === null ? [] : value)} flexibleControlStateSize multiple/>)}
        </access_1.default>
      </panels_1.PanelBody>
    </panels_1.Panel>);
}
exports.default = BuiltInRepositories;
const StyledSelectField = (0, styled_1.default)(selectField_1.default) `
  ${p => p.disabled && `cursor: not-allowed`}
`;
//# sourceMappingURL=builtInRepositories.jsx.map