Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const enzyme_1 = require("sentry-test/enzyme");
const projectSecurityAndPrivacy_1 = (0, tslib_1.__importDefault)(require("app/views/settings/projectSecurityAndPrivacy"));
const org = TestStubs.Organization();
const project = TestStubs.ProjectDetails();
function renderComponent(providedOrg) {
    const organization = providedOrg !== null && providedOrg !== void 0 ? providedOrg : org;
    MockApiClient.addMockResponse({
        url: `/projects/${organization.slug}/${project.slug}/`,
        method: 'GET',
        body: project,
    });
    return (0, enzyme_1.mountWithTheme)(<projectSecurityAndPrivacy_1.default {...TestStubs.routerContext().context} project={project} organization={organization} params={{ orgId: organization.slug, projectId: project.slug }}/>);
}
describe('projectSecurityAndPrivacy', function () {
    it('renders form fields', function () {
        const wrapper = renderComponent();
        expect(wrapper.find('Switch[name="dataScrubber"]').prop('isActive')).toBeFalsy();
        expect(wrapper.find('Switch[name="dataScrubberDefaults"]').prop('isActive')).toBeFalsy();
        expect(wrapper.find('Switch[name="scrubIPAddresses"]').prop('isActive')).toBeFalsy();
        expect(wrapper.find('TextArea[name="sensitiveFields"]').prop('value')).toBe('creditcard\nssn');
        expect(wrapper.find('TextArea[name="safeFields"]').prop('value')).toBe('business-email\ncompany');
    });
    it('disables field when equivalent org setting is true', function () {
        const newOrganization = Object.assign({}, org);
        newOrganization.dataScrubber = true;
        newOrganization.scrubIPAddresses = false;
        const wrapper = renderComponent(newOrganization);
        expect(wrapper.find('Switch[name="scrubIPAddresses"]').prop('isDisabled')).toBe(false);
        expect(wrapper.find('Switch[name="scrubIPAddresses"]').prop('isActive')).toBeFalsy();
        expect(wrapper.find('Switch[name="dataScrubber"]').prop('isDisabled')).toBe(true);
        expect(wrapper.find('Switch[name="dataScrubber"]').prop('isActive')).toBe(true);
    });
});
//# sourceMappingURL=projectSecurityAndPrivacy.spec.jsx.map