Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const commandLine_1 = (0, tslib_1.__importDefault)(require("app/components/commandLine"));
describe('CommandLine', () => {
    it('renders', () => {
        const children = 'sentry devserver --workers';
        (0, reactTestingLibrary_1.mountWithTheme)(<commandLine_1.default>{children}</commandLine_1.default>);
        expect(reactTestingLibrary_1.screen.getByText(children)).toBeInTheDocument();
    });
});
//# sourceMappingURL=commandLine.spec.jsx.map