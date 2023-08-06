Object.defineProperty(exports, "__esModule", { value: true });
exports.renderModal = exports.renderComponent = exports.commonConditionCategories = void 0;
const tslib_1 = require("tslib");
const react_1 = require("react");
const initializeOrg_1 = require("sentry-test/initializeOrg");
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const globalModal_1 = (0, tslib_1.__importDefault)(require("app/components/globalModal"));
const filtersAndSampling_1 = (0, tslib_1.__importDefault)(require("app/views/settings/project/filtersAndSampling"));
exports.commonConditionCategories = [
    'Release',
    'Environment',
    'User Id',
    'User Segment',
    'Browser Extensions',
    'Localhost',
    'Legacy Browser',
    'Web Crawlers',
    'IP Address',
    'Content Security Policy',
    'Error Message',
    'Transaction',
];
function renderComponent(withModal = true) {
    const { organization, project } = (0, initializeOrg_1.initializeOrg)({
        organization: { features: ['filters-and-sampling'] },
    });
    return (0, reactTestingLibrary_1.mountWithTheme)(<react_1.Fragment>
      {withModal && <globalModal_1.default />}
      <filtersAndSampling_1.default organization={organization} project={project}/>
    </react_1.Fragment>);
}
exports.renderComponent = renderComponent;
function renderModal(actionElement, takeScreenshot = false) {
    return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
        // Open Modal
        reactTestingLibrary_1.userEvent.click(actionElement);
        const dialog = yield reactTestingLibrary_1.screen.findByRole('dialog');
        expect(dialog).toBeInTheDocument();
        if (takeScreenshot) {
            expect(dialog).toSnapshot();
        }
    });
}
exports.renderModal = renderModal;
//# sourceMappingURL=utils.jsx.map