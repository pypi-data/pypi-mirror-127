Object.defineProperty(exports, "__esModule", { value: true });
exports.fireEvent = exports.userEvent = exports.mountWithTheme = void 0;
const tslib_1 = require("tslib");
const react_1 = require("react");
const css_1 = require("@emotion/css");
const react_2 = require("@emotion/react");
const react_3 = require("@testing-library/react");
const user_event_1 = (0, tslib_1.__importDefault)(require("@testing-library/user-event"));
exports.userEvent = user_event_1.default;
const theme_1 = require("app/utils/theme");
const organizationContext_1 = require("app/views/organizationContext");
function createProvider(contextDefs) {
    var _a;
    return _a = class ContextProvider extends react_1.Component {
            getChildContext() {
                return contextDefs.context;
            }
            render() {
                return this.props.children;
            }
        },
        _a.childContextTypes = contextDefs.childContextTypes,
        _a;
}
function makeAllTheProviders({ context, organization }) {
    return function ({ children }) {
        const ContextProvider = context ? createProvider(context) : react_1.Fragment;
        return (<ContextProvider>
        <react_2.CacheProvider value={css_1.cache}>
          <react_2.ThemeProvider theme={theme_1.lightTheme}>
            {organization ? (<organizationContext_1.OrganizationContext.Provider value={organization}>
                {children}
              </organizationContext_1.OrganizationContext.Provider>) : (children)}
          </react_2.ThemeProvider>
        </react_2.CacheProvider>
      </ContextProvider>);
    };
}
/**
 * Migrating from enzyme? Pass context via the options object
 * Before
 * mountWithTheme(<Something />, routerContext);
 * After
 * mountWithTheme(<Something />, {context: routerContext});
 */
const mountWithTheme = (ui, options) => {
    const _a = options !== null && options !== void 0 ? options : {}, { context, organization } = _a, otherOptions = (0, tslib_1.__rest)(_a, ["context", "organization"]);
    const AllTheProviders = makeAllTheProviders({ context, organization });
    return (0, react_3.render)(ui, Object.assign({ wrapper: AllTheProviders }, otherOptions));
};
exports.mountWithTheme = mountWithTheme;
(0, tslib_1.__exportStar)(require("@testing-library/react"), exports);
/**
 * @deprecated
 * Use userEvent over fireEvent where possible.
 * More details: https://kentcdodds.com/blog/common-mistakes-with-react-testing-library#not-using-testing-libraryuser-event
 */
const fireEvent = react_3.fireEvent;
exports.fireEvent = fireEvent;
//# sourceMappingURL=reactTestingLibrary.jsx.map