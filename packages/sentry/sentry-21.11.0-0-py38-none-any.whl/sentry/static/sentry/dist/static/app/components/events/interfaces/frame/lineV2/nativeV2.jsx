Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const scroll_to_element_1 = (0, tslib_1.__importDefault)(require("scroll-to-element"));
const traceEventDataSection_1 = require("app/components/events/traceEventDataSection");
const displayOptions_1 = require("app/components/events/traceEventDataSection/displayOptions");
const locale_1 = require("app/locale");
const debugMetaStore_1 = require("app/stores/debugMetaStore");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const utils_1 = require("../../debugMeta/utils");
const types_1 = require("../../types");
const packageLink_1 = (0, tslib_1.__importDefault)(require("../packageLink"));
const packageStatus_1 = (0, tslib_1.__importDefault)(require("../packageStatus"));
const symbol_1 = (0, tslib_1.__importDefault)(require("../symbol"));
const togglableAddress_1 = (0, tslib_1.__importDefault)(require("../togglableAddress"));
const utils_2 = require("../utils");
const expander_1 = (0, tslib_1.__importDefault)(require("./expander"));
const leadHint_1 = (0, tslib_1.__importDefault)(require("./leadHint"));
const wrapper_1 = (0, tslib_1.__importDefault)(require("./wrapper"));
function Native(_a) {
    var { frame, isFrameAfterLastNonApp, isExpanded, isHoverPreviewed, image, includeSystemFrames, maxLengthOfRelativeAddress, platform, prevFrame, isUsedForGrouping, nextFrame, leadsToApp, onMouseDown, onClick } = _a, props = (0, tslib_1.__rest)(_a, ["frame", "isFrameAfterLastNonApp", "isExpanded", "isHoverPreviewed", "image", "includeSystemFrames", "maxLengthOfRelativeAddress", "platform", "prevFrame", "isUsedForGrouping", "nextFrame", "leadsToApp", "onMouseDown", "onClick"]);
    const traceEventDataSectionContext = (0, react_1.useContext)(traceEventDataSection_1.TraceEventDataSectionContext);
    if (!traceEventDataSectionContext) {
        return null;
    }
    const { instructionAddr, trust, addrMode, symbolicatorStatus } = frame !== null && frame !== void 0 ? frame : {};
    function packageStatus() {
        // this is the status of image that belongs to this frame
        if (!image) {
            return 'empty';
        }
        const combinedStatus = (0, utils_1.combineStatus)(image.debug_status, image.unwind_status);
        switch (combinedStatus) {
            case 'unused':
                return 'empty';
            case 'found':
                return 'success';
            default:
                return 'error';
        }
    }
    function makeFilter(addr) {
        if (!(!addrMode || addrMode === 'abs') && image) {
            return `${image.debug_id}!${addr}`;
        }
        return addr;
    }
    function scrollToImage(event) {
        event.stopPropagation(); // to prevent collapsing if collapsible
        if (instructionAddr) {
            debugMetaStore_1.DebugMetaActions.updateFilter(makeFilter(instructionAddr));
        }
        (0, scroll_to_element_1.default)('#images-loaded');
    }
    const shouldShowLinkToImage = !!symbolicatorStatus &&
        symbolicatorStatus !== types_1.SymbolicatorStatus.UNKNOWN_IMAGE &&
        !isHoverPreviewed;
    const isInlineFrame = prevFrame &&
        (0, utils_2.getPlatform)(frame.platform, platform !== null && platform !== void 0 ? platform : 'other') ===
            (prevFrame.platform || platform) &&
        instructionAddr === prevFrame.instructionAddr;
    const isFoundByStackScanning = trust === 'scan' || trust === 'cfi-scan';
    return (<wrapper_1.default className="title as-table" onMouseDown={onMouseDown} onClick={onClick}>
      <NativeLineContent isFrameAfterLastNonApp={!!isFrameAfterLastNonApp}>
        <PackageInfo>
          <leadHint_1.default isExpanded={isExpanded} nextFrame={nextFrame} leadsToApp={leadsToApp}/>
          <packageLink_1.default includeSystemFrames={!!includeSystemFrames} withLeadHint={!(isExpanded || !leadsToApp)} packagePath={frame.package} onClick={scrollToImage} isClickable={shouldShowLinkToImage} isHoverPreviewed={isHoverPreviewed}>
            {!isHoverPreviewed && (<packageStatus_1.default status={packageStatus()} tooltip={(0, locale_1.t)('Go to Images Loaded')}/>)}
          </packageLink_1.default>
        </PackageInfo>
        {instructionAddr && (<togglableAddress_1.default address={instructionAddr} startingAddress={image ? image.image_addr : null} isAbsolute={traceEventDataSectionContext.activeDisplayOptions.includes(displayOptions_1.DisplayOption.ABSOLUTE_ADDRESSES)} isFoundByStackScanning={isFoundByStackScanning} isInlineFrame={!!isInlineFrame} relativeAddressMaxlength={maxLengthOfRelativeAddress} isHoverPreviewed={isHoverPreviewed}/>)}
        <symbol_1.default frame={frame} showCompleteFunctionName={traceEventDataSectionContext.activeDisplayOptions.includes(displayOptions_1.DisplayOption.VERBOSE_FUNCTION_NAMES)} absoluteFilePaths={traceEventDataSectionContext.activeDisplayOptions.includes(displayOptions_1.DisplayOption.ABSOLUTE_FILE_PATHS)} isHoverPreviewed={isHoverPreviewed} isUsedForGrouping={isUsedForGrouping} nativeStackTraceV2/>
      </NativeLineContent>
      <expander_1.default isExpanded={isExpanded} isHoverPreviewed={isHoverPreviewed} platform={platform} {...props}/>
    </wrapper_1.default>);
}
exports.default = Native;
const PackageInfo = (0, styled_1.default)('span') `
  display: grid;
  grid-template-columns: auto 1fr;
  order: 2;
  align-items: flex-start;
  @media (min-width: ${props => props.theme.breakpoints[0]}) {
    order: 0;
  }
`;
const NativeLineContent = (0, styled_1.default)('div') `
  display: grid;
  flex: 1;
  grid-gap: ${(0, space_1.default)(0.5)};
  grid-template-columns: auto 1fr;
  align-items: center;
  justify-content: flex-start;

  @media (min-width: ${props => props.theme.breakpoints[0]}) {
    grid-template-columns:
      ${p => (p.isFrameAfterLastNonApp ? '200px' : '150px')} minmax(117px, auto)
      1fr;
  }

  @media (min-width: ${props => props.theme.breakpoints[2]}) and (max-width: ${props => props.theme.breakpoints[3]}) {
    grid-template-columns:
      ${p => (p.isFrameAfterLastNonApp ? '180px' : '140px')} minmax(117px, auto)
      1fr;
  }
`;
//# sourceMappingURL=nativeV2.jsx.map