Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const resolutionBox_1 = (0, tslib_1.__importDefault)(require("app/components/resolutionBox"));
describe('ResolutionBox', function () {
    describe('render()', function () {
        it('handles inNextRelease', function () {
            const { container } = (0, reactTestingLibrary_1.mountWithTheme)(<resolutionBox_1.default statusDetails={{ inNextRelease: true }} projectId="1"/>);
            expect(container).toSnapshot();
        });
        it('handles inNextRelease with actor', function () {
            const { container } = (0, reactTestingLibrary_1.mountWithTheme)(<resolutionBox_1.default statusDetails={{
                    inNextRelease: true,
                    actor: {
                        id: '111',
                        name: 'David Cramer',
                        username: 'dcramer',
                        ip_address: '127.0.0.1',
                        email: 'david@sentry.io',
                    },
                }} projectId="1"/>);
            expect(container).toSnapshot();
        });
        it('handles inRelease', function () {
            const { container } = (0, reactTestingLibrary_1.mountWithTheme)(<resolutionBox_1.default statusDetails={{
                    inRelease: '1.0',
                }} projectId="1"/>);
            expect(container).toSnapshot();
        });
        it('handles inRelease with actor', function () {
            const { container } = (0, reactTestingLibrary_1.mountWithTheme)(<resolutionBox_1.default statusDetails={{
                    inRelease: '1.0',
                    actor: {
                        id: '111',
                        name: 'David Cramer',
                        username: 'dcramer',
                        ip_address: '127.0.0.1',
                        email: 'david@sentry.io',
                    },
                }} projectId="1"/>);
            expect(container).toSnapshot();
        });
        it('handles default', function () {
            const { container } = (0, reactTestingLibrary_1.mountWithTheme)(<resolutionBox_1.default statusDetails={{}} projectId="1"/>);
            expect(container).toSnapshot();
        });
        it('handles inCommit', function () {
            const { container } = (0, reactTestingLibrary_1.mountWithTheme)(<resolutionBox_1.default statusDetails={{
                    inCommit: TestStubs.Commit(),
                }} projectId="1"/>);
            expect(container).toSnapshot();
        });
    });
});
//# sourceMappingURL=resolutionBox.spec.jsx.map