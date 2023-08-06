Object.defineProperty(exports, "__esModule", { value: true });
exports.TraceEventDataSectionContext = void 0;
const tslib_1 = require("tslib");
const react_1 = require("react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const button_1 = (0, tslib_1.__importDefault)(require("app/components/button"));
const iconAnchor_1 = require("app/icons/iconAnchor");
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const stacktrace_1 = require("app/types/stacktrace");
const platform_1 = require("app/utils/platform");
const useApi_1 = (0, tslib_1.__importDefault)(require("app/utils/useApi"));
const useOrganization_1 = (0, tslib_1.__importDefault)(require("app/utils/useOrganization"));
const booleanField_1 = (0, tslib_1.__importDefault)(require("app/views/settings/components/forms/booleanField"));
const eventDataSection_1 = (0, tslib_1.__importDefault)(require("../eventDataSection"));
const displayOptions_1 = (0, tslib_1.__importStar)(require("./displayOptions"));
const sortOptions_1 = (0, tslib_1.__importStar)(require("./sortOptions"));
const TraceEventDataSectionContext = (0, react_1.createContext)(undefined);
exports.TraceEventDataSectionContext = TraceEventDataSectionContext;
function TraceEventDataSection(_a) {
    var { title, type, children, projectId, eventId, stackType, platform, showPermalink, wrapTitle, hasVerboseFunctionNames, hasMinified, hasAbsoluteFilePaths, hasAbsoluteAddresses, hasAppOnlyFrames, hasNewestFirst, stackTraceNotFound } = _a, defaultStateProps = (0, tslib_1.__rest)(_a, ["title", "type", "children", "projectId", "eventId", "stackType", "platform", "showPermalink", "wrapTitle", "hasVerboseFunctionNames", "hasMinified", "hasAbsoluteFilePaths", "hasAbsoluteAddresses", "hasAppOnlyFrames", "hasNewestFirst", "stackTraceNotFound"]);
    const api = (0, useApi_1.default)();
    const organization = (0, useOrganization_1.default)();
    const [state, setState] = (0, react_1.useState)(() => {
        const { recentFirst, fullStackTrace } = defaultStateProps;
        return {
            raw: false,
            recentFirst,
            activeDisplayOptions: fullStackTrace ? [displayOptions_1.DisplayOption.FULL_STACK_TRACE] : [],
        };
    });
    const { recentFirst, raw, activeDisplayOptions } = state;
    (0, react_1.useEffect)(() => {
        if (raw || activeDisplayOptions.includes(displayOptions_1.DisplayOption.FULL_STACK_TRACE)) {
            return;
        }
        setState(Object.assign(Object.assign({}, state), { activeDisplayOptions: [...activeDisplayOptions, displayOptions_1.DisplayOption.FULL_STACK_TRACE] }));
    }, [defaultStateProps.fullStackTrace]);
    function getDownloadHref() {
        const minified = stackType === stacktrace_1.STACK_TYPE.MINIFIED;
        // Apple crash report endpoint
        const endpoint = `/projects/${organization.slug}/${projectId}/events/${eventId}/apple-crash-report?minified=${minified}`;
        return `${api.baseUrl}${endpoint}&download=1`;
    }
    const childProps = { recentFirst, raw, activeDisplayOptions };
    return (<eventDataSection_1.default type={type} title={<Header raw={raw}>
          {showPermalink ? (<div>
              <Permalink href={'#' + type} className="permalink">
                <StyledIconAnchor />
                {title}
              </Permalink>
            </div>) : (title)}
          {!stackTraceNotFound && (<react_1.Fragment>
              <RawContentWrapper>
                <RawToggler name="raw-stack-trace" label={(0, locale_1.t)('Raw')} hideControlState value={raw} onChange={() => setState(Object.assign(Object.assign({}, state), { raw: !raw }))}/>
                {raw && (0, platform_1.isNativePlatform)(platform) && (<LargeScreenDownloadButton size="small" href={getDownloadHref()} title={(0, locale_1.t)('Download raw stack trace file')}>
                    {(0, locale_1.t)('Download')}
                  </LargeScreenDownloadButton>)}
              </RawContentWrapper>
              {raw ? ((0, platform_1.isNativePlatform)(platform) && (<SmallScreenDownloadButton size="small" href={getDownloadHref()} title={(0, locale_1.t)('Download raw stack trace file')}>
                    {(0, locale_1.t)('Download')}
                  </SmallScreenDownloadButton>)) : (<react_1.Fragment>
                  <sortOptions_1.default disabled={!hasNewestFirst} activeSortOption={recentFirst ? sortOptions_1.SortOption.RECENT_FIRST : sortOptions_1.SortOption.RECENT_LAST} onChange={newSortOption => setState(Object.assign(Object.assign({}, state), { recentFirst: newSortOption === sortOptions_1.SortOption.RECENT_FIRST }))}/>
                  <displayOptions_1.default platform={platform} hasAppOnlyFrames={hasAppOnlyFrames} hasAbsoluteAddresses={hasAbsoluteAddresses} hasAbsoluteFilePaths={hasAbsoluteFilePaths} hasVerboseFunctionNames={hasVerboseFunctionNames} hasMinified={hasMinified} activeDisplayOptions={activeDisplayOptions} onChange={newActiveDisplayOptions => setState(Object.assign(Object.assign({}, state), { activeDisplayOptions: newActiveDisplayOptions }))}/>
                </react_1.Fragment>)}
            </react_1.Fragment>)}
        </Header>} showPermalink={false} wrapTitle={wrapTitle}>
      <TraceEventDataSectionContext.Provider value={childProps}>
        {children(childProps)}
      </TraceEventDataSectionContext.Provider>
    </eventDataSection_1.default>);
}
exports.default = TraceEventDataSection;
const Header = (0, styled_1.default)('div') `
  display: grid;
  grid-template-columns: 1fr max-content;
  grid-template-rows: ${p => (p.raw ? 'repeat(2, 1f)' : 'repeat(3, 1fr)')};
  grid-gap: ${(0, space_1.default)(1)};
  align-items: center;
  flex: 1;
  z-index: 3;

  @media (min-width: ${p => p.theme.breakpoints[0]}) {
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: ${p => (p.raw ? '1fr' : 'repeat(2, 1fr)')};
  }

  @media (min-width: ${p => p.theme.breakpoints[3]}) {
    grid-template-columns: ${p => p.raw
    ? '1fr repeat(2, max-content)'
    : '1fr max-content minmax(159px, auto) minmax(140px, auto)'};
    grid-template-rows: 1fr;
  }
`;
const RawToggler = (0, styled_1.default)(booleanField_1.default) `
  padding: 0;
  display: grid;
  grid-template-columns: repeat(2, max-content);
  grid-gap: ${(0, space_1.default)(1)};
  border-bottom: none;
  justify-content: flex-end;

  && {
    > * {
      padding: 0;
      width: auto;
    }
  }
`;
const RawContentWrapper = (0, styled_1.default)('div') `
  display: grid;
  grid-auto-flow: column;
  justify-content: flex-end;
`;
const LargeScreenDownloadButton = (0, styled_1.default)(button_1.default) `
  display: none;
  margin-left: ${(0, space_1.default)(1)};
  @media (min-width: ${p => p.theme.breakpoints[0]}) {
    display: block;
  }
`;
const SmallScreenDownloadButton = (0, styled_1.default)(button_1.default) `
  display: block;
  grid-column: 1/-1;
  @media (min-width: ${p => p.theme.breakpoints[0]}) {
    display: none;
  }
`;
const StyledIconAnchor = (0, styled_1.default)(iconAnchor_1.IconAnchor) `
  display: none;
  position: absolute;
  top: 4px;
  left: -22px;
`;
const Permalink = (0, styled_1.default)('a') `
  display: inline-flex;
  justify-content: flex-start;
  :hover ${StyledIconAnchor} {
    display: block;
    color: ${p => p.theme.gray300};
  }
`;
//# sourceMappingURL=index.jsx.map