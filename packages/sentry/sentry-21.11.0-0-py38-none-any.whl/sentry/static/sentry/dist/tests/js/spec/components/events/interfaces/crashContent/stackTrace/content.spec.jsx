Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const content_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/crashContent/stackTrace/content"));
const eventEntryStacktrace = TestStubs.EventEntryStacktrace();
const event = TestStubs.Event({ entries: [eventEntryStacktrace] });
const data = eventEntryStacktrace.data;
function renderedComponent(props) {
    return (0, reactTestingLibrary_1.mountWithTheme)(<content_1.default data={data} className="no-exception" platform="other" event={event} newestFirst includeSystemFrames {...props}/>);
}
describe('StackTrace', function () {
    it('renders', function () {
        const { container } = renderedComponent({});
        // stack trace content
        const stackTraceContent = reactTestingLibrary_1.screen.getByTestId('stack-trace-content');
        expect(stackTraceContent).toBeInTheDocument();
        // stack trace content has to have a platform icon and a frame list
        expect(stackTraceContent.children).toHaveLength(2);
        // platform icon
        expect(reactTestingLibrary_1.screen.getByTestId('platform-icon-python')).toBeInTheDocument();
        // frame list
        const frames = reactTestingLibrary_1.screen.getByTestId('frames');
        expect(frames.children).toHaveLength(5);
        expect(container).toSnapshot();
    });
    it('renders the frame in the correct order', function () {
        renderedComponent({});
        // frame - filename
        const frameFilenames = reactTestingLibrary_1.screen.getAllByTestId('filename');
        expect(frameFilenames).toHaveLength(5);
        expect(frameFilenames[0]).toHaveTextContent('raven/scripts/runner.py');
        expect(frameFilenames[1]).toHaveTextContent('raven/scripts/runner.py');
        expect(frameFilenames[2]).toHaveTextContent('raven/base.py');
        expect(frameFilenames[3]).toHaveTextContent('raven/base.py');
        expect(frameFilenames[4]).toHaveTextContent('raven/base.py');
        // frame - function
        const frameFunction = reactTestingLibrary_1.screen.getAllByTestId('function');
        expect(frameFunction).toHaveLength(5);
        expect(frameFunction[0]).toHaveTextContent('main');
        expect(frameFunction[1]).toHaveTextContent('send_test_message');
        expect(frameFunction[2]).toHaveTextContent('captureMessage');
        expect(frameFunction[3]).toHaveTextContent('capture');
        expect(frameFunction[4]).toHaveTextContent('build_msg');
    });
    it('collapse/expand frames by clicking anywhere in the frame element', function () {
        renderedComponent({});
        // frame list
        const frames = reactTestingLibrary_1.screen.getByTestId('frames');
        expect(frames.children).toHaveLength(5);
        // only one frame is expanded by default
        expect(reactTestingLibrary_1.screen.getByTestId('toggle-button-expanded')).toBeInTheDocument();
        expect(reactTestingLibrary_1.screen.getAllByTestId('toggle-button-collapsed')).toHaveLength(4);
        // clickable list item element
        const frameTitles = reactTestingLibrary_1.screen.getAllByTestId('title');
        // collapse the expanded frame (by default)
        reactTestingLibrary_1.userEvent.click(frameTitles[0]);
        // all frames are now collapsed
        expect(reactTestingLibrary_1.screen.queryByTestId('toggle-button-expanded')).not.toBeInTheDocument();
        expect(reactTestingLibrary_1.screen.getAllByTestId('toggle-button-collapsed')).toHaveLength(5);
        // expand penultimate and last frame
        reactTestingLibrary_1.userEvent.click(frameTitles[frameTitles.length - 2]);
        reactTestingLibrary_1.userEvent.click(frameTitles[frameTitles.length - 1]);
        // two frames are now collapsed
        expect(reactTestingLibrary_1.screen.getAllByTestId('toggle-button-expanded')).toHaveLength(2);
        expect(reactTestingLibrary_1.screen.getAllByTestId('toggle-button-collapsed')).toHaveLength(3);
    });
    it('collapse/expand frames by clicking on the toggle button', function () {
        renderedComponent({});
        // frame list
        const frames = reactTestingLibrary_1.screen.getByTestId('frames');
        expect(frames.children).toHaveLength(5);
        const expandedToggleButtons = reactTestingLibrary_1.screen.getByTestId('toggle-button-expanded');
        // only one frame is expanded by default
        expect(expandedToggleButtons).toBeInTheDocument();
        expect(reactTestingLibrary_1.screen.getAllByTestId('toggle-button-collapsed')).toHaveLength(4);
        // collapse the expanded frame (by default)
        reactTestingLibrary_1.userEvent.click(expandedToggleButtons);
        // all frames are now collapsed
        expect(reactTestingLibrary_1.screen.queryByTestId('toggle-button-expanded')).not.toBeInTheDocument();
        expect(reactTestingLibrary_1.screen.getAllByTestId('toggle-button-collapsed')).toHaveLength(5);
        const collapsedToggleButtons = reactTestingLibrary_1.screen.getAllByTestId('toggle-button-collapsed');
        // expand penultimate and last frame
        reactTestingLibrary_1.userEvent.click(collapsedToggleButtons[collapsedToggleButtons.length - 2]);
        reactTestingLibrary_1.userEvent.click(collapsedToggleButtons[collapsedToggleButtons.length - 1]);
        // two frames are now collapsed
        expect(reactTestingLibrary_1.screen.getAllByTestId('toggle-button-expanded')).toHaveLength(2);
        expect(reactTestingLibrary_1.screen.getAllByTestId('toggle-button-collapsed')).toHaveLength(3);
    });
    it('if all in_app equals false, all the frames are showing by default', function () {
        renderedComponent({});
        // frame list
        const frames = reactTestingLibrary_1.screen.getByTestId('frames');
        expect(frames.children).toHaveLength(5);
    });
    describe('if there is a frame with in_app equal to true, display only in_app frames', function () {
        it('displays crashed from only', function () {
            const dataFrames = [...data.frames];
            const newData = Object.assign(Object.assign({}, data), { hasSystemFrames: true, frames: [
                    Object.assign(Object.assign({}, dataFrames[0]), { inApp: true }),
                    ...dataFrames.splice(1, dataFrames.length),
                ] });
            renderedComponent({
                data: newData,
                event: Object.assign(Object.assign({}, event), { entries: [Object.assign(Object.assign({}, event.entries[0]), { stacktrace: newData.frames })] }),
                includeSystemFrames: false,
            });
            // clickable list item element
            const frameTitles = reactTestingLibrary_1.screen.getAllByTestId('title');
            // frame list - in app only
            expect(frameTitles).toHaveLength(2);
            expect(frameTitles[0]).toHaveTextContent('Crashed in non-app: raven/scripts/runner.py in main at line 112');
            expect(frameTitles[1]).toHaveTextContent('raven/base.py in build_msg at line 303');
        });
        it('displays called from only', function () {
            const dataFrames = [...data.frames];
            const newData = Object.assign(Object.assign({}, data), { hasSystemFrames: true, registers: {}, frames: [
                    ...dataFrames.splice(0, dataFrames.length - 1),
                    Object.assign(Object.assign({}, dataFrames[dataFrames.length - 1]), { inApp: true }),
                ] });
            renderedComponent({
                data: newData,
                event: Object.assign(Object.assign({}, event), { entries: [Object.assign(Object.assign({}, event.entries[0]), { stacktrace: newData.frames })] }),
                includeSystemFrames: false,
            });
            // clickable list item element
            const frameTitles = reactTestingLibrary_1.screen.getAllByTestId('title');
            // frame list - in app only
            expect(frameTitles).toHaveLength(2);
            expect(frameTitles[0]).toHaveTextContent('raven/scripts/runner.py in main at line 112');
            expect(frameTitles[1]).toHaveTextContent('Called from: raven/scripts/runner.py in send_test_message at line 77');
        });
        it('displays crashed from and called from', function () {
            const dataFrames = [...data.frames];
            const newData = Object.assign(Object.assign({}, data), { hasSystemFrames: true, frames: [
                    ...dataFrames.slice(0, 1),
                    Object.assign(Object.assign({}, dataFrames[1]), { inApp: true }),
                    ...dataFrames.slice(2, dataFrames.length),
                ] });
            renderedComponent({
                data: newData,
                event: Object.assign(Object.assign({}, event), { entries: [Object.assign(Object.assign({}, event.entries[0]), { stacktrace: newData.frames })] }),
                includeSystemFrames: false,
            });
            // clickable list item element
            const frameTitles = reactTestingLibrary_1.screen.getAllByTestId('title');
            // frame list - in app only
            expect(frameTitles).toHaveLength(3);
            expect(frameTitles[0]).toHaveTextContent('Crashed in non-app: raven/scripts/runner.py in main at line 112');
            expect(frameTitles[1]).toHaveTextContent('raven/base.py in capture at line 459');
            expect(frameTitles[2]).toHaveTextContent('Called from: raven/base.py in build_msg at line 303');
        });
    });
});
//# sourceMappingURL=content.spec.jsx.map