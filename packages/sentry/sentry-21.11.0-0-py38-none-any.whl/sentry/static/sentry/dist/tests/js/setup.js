var _a;
var _b;
Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("@testing-library/react");
const enzyme_adapter_react_17_1 = (0, tslib_1.__importDefault)(require("@wojtekmaj/enzyme-adapter-react-17"));
const enzyme_1 = (0, tslib_1.__importDefault)(require("enzyme")); // eslint-disable-line no-restricted-imports
const mockdate_1 = (0, tslib_1.__importDefault)(require("mockdate"));
const prop_types_1 = (0, tslib_1.__importDefault)(require("prop-types"));
const configStore_1 = (0, tslib_1.__importDefault)(require("app/stores/configStore"));
const loadFixtures_1 = require("./sentry-test/loadFixtures");
/**
 * XXX(epurkhiser): Gross hack to fix a bug in jsdom which makes testing of
 * framer-motion SVG components fail
 *
 * See https://github.com/jsdom/jsdom/issues/1330
 */
// @ts-expect-error
(_a = (_b = SVGElement.prototype).getTotalLength) !== null && _a !== void 0 ? _a : (_b.getTotalLength = () => 1);
/**
 * React Testing Library configuration to override the default test id attribute
 *
 * See: https://testing-library.com/docs/queries/bytestid/#overriding-data-testid
 */
(0, react_1.configure)({ testIdAttribute: 'data-test-id' });
/**
 * Enzyme configuration
 *
 * TODO(epurkhiser): We're using @wojtekmaj's react-17 enzyme adapter, until
 * the offical adapter has been released.
 *
 * https://github.com/enzymejs/enzyme/issues/2429
 */
enzyme_1.default.configure({ adapter: new enzyme_adapter_react_17_1.default() });
/**
 * Mock (current) date to always be National Pasta Day
 * 2017-10-17T02:41:20.000Z
 */
const constantDate = new Date(1508208080000);
mockdate_1.default.set(constantDate);
/**
 * Load all files in `tests/js/fixtures/*` as a module.
 * These will then be added to the `TestStubs` global below
 */
const fixtures = (0, loadFixtures_1.loadFixtures)('js-stubs', { flatten: true });
/**
 * Global testing configuration
 */
configStore_1.default.loadInitialData(fixtures.Config());
/**
 * Mocks
 */
jest.mock('lodash/debounce', () => jest.fn(fn => fn));
jest.mock('app/utils/recreateRoute');
jest.mock('app/api');
jest.mock('app/utils/domId');
jest.mock('app/utils/withOrganization');
jest.mock('scroll-to-element', () => jest.fn());
jest.mock('react-router', () => {
    const ReactRouter = jest.requireActual('react-router');
    return Object.assign(Object.assign({}, ReactRouter), { browserHistory: {
            goBack: jest.fn(),
            push: jest.fn(),
            replace: jest.fn(),
            listen: jest.fn(() => { }),
        } });
});
jest.mock('react-lazyload', () => {
    const LazyLoadMock = ({ children }) => children;
    return LazyLoadMock;
});
jest.mock('react-virtualized', () => {
    const ActualReactVirtualized = jest.requireActual('react-virtualized');
    return Object.assign(Object.assign({}, ActualReactVirtualized), { AutoSizer: ({ children }) => children({ width: 100, height: 100 }) });
});
jest.mock('echarts-for-react/lib/core', () => {
    // We need to do this because `jest.mock` gets hoisted by babel and `React` is not
    // guaranteed to be in scope
    const ReactActual = require('react');
    // We need a class component here because `BaseChart` passes `ref` which will
    // error if we return a stateless/functional component
    return class extends ReactActual.Component {
        render() {
            return null;
        }
    };
});
jest.mock('@sentry/react', () => {
    const SentryReact = jest.requireActual('@sentry/react');
    return {
        init: jest.fn(),
        configureScope: jest.fn(),
        setTag: jest.fn(),
        setTags: jest.fn(),
        setExtra: jest.fn(),
        setExtras: jest.fn(),
        captureBreadcrumb: jest.fn(),
        addBreadcrumb: jest.fn(),
        captureMessage: jest.fn(),
        captureException: jest.fn(),
        showReportDialog: jest.fn(),
        startSpan: jest.fn(),
        finishSpan: jest.fn(),
        lastEventId: jest.fn(),
        getCurrentHub: jest.spyOn(SentryReact, 'getCurrentHub'),
        withScope: jest.spyOn(SentryReact, 'withScope'),
        Severity: SentryReact.Severity,
        withProfiler: SentryReact.withProfiler,
        startTransaction: () => ({
            finish: jest.fn(),
            setTag: jest.fn(),
            setData: jest.fn(),
            setStatus: jest.fn(),
        }),
    };
});
jest.mock('popper.js', () => {
    var _a;
    const PopperJS = jest.requireActual('popper.js');
    return _a = class {
            constructor() {
                return {
                    destroy: () => { },
                    scheduleUpdate: () => { },
                };
            }
        },
        _a.placements = PopperJS.placements,
        _a;
});
const routerFixtures = {
    router: (params = {}) => (Object.assign({ push: jest.fn(), replace: jest.fn(), go: jest.fn(), goBack: jest.fn(), goForward: jest.fn(), setRouteLeaveHook: jest.fn(), isActive: jest.fn(), createHref: jest.fn(), location: TestStubs.location(), createPath: jest.fn(), routes: [], params: {} }, params)),
    location: (params = {}) => (Object.assign({ key: '', search: '', hash: '', action: 'PUSH', state: null, query: {}, pathname: '/mock-pathname/' }, params)),
    routerProps: (params = {}) => (Object.assign({ location: TestStubs.location(), params: {}, routes: [], stepBack: () => { } }, params)),
    routerContext: ([context, childContextTypes] = []) => ({
        context: Object.assign({ location: TestStubs.location(), router: TestStubs.router(), organization: fixtures.Organization(), project: fixtures.Project() }, context),
        childContextTypes: Object.assign({ router: prop_types_1.default.object, location: prop_types_1.default.object, organization: prop_types_1.default.object, project: prop_types_1.default.object }, childContextTypes),
    }),
};
window.TestStubs = Object.assign(Object.assign({}, fixtures), routerFixtures);
// This is so we can use async/await in tests instead of wrapping with `setTimeout`.
window.tick = () => new Promise(resolve => setTimeout(resolve));
window.MockApiClient = jest.requireMock('app/api').Client;
window.scrollTo = jest.fn();
// We need to re-define `window.location`, otherwise we can't spyOn certain
// methods as `window.location` is read-only
Object.defineProperty(window, 'location', {
    value: Object.assign(Object.assign({}, window.location), { assign: jest.fn(), reload: jest.fn() }),
    configurable: true,
    writable: true,
});
//# sourceMappingURL=setup.js.map