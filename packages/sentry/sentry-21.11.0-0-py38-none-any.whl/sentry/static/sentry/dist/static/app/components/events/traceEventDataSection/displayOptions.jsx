Object.defineProperty(exports, "__esModule", { value: true });
exports.DisplayOption = void 0;
const tslib_1 = require("tslib");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const button_1 = require("app/components/button");
const checkboxFancy_1 = (0, tslib_1.__importDefault)(require("app/components/checkboxFancy/checkboxFancy"));
const dropdownButton_1 = (0, tslib_1.__importDefault)(require("app/components/dropdownButton"));
const dropdownControl_1 = (0, tslib_1.__importStar)(require("app/components/dropdownControl"));
const list_1 = (0, tslib_1.__importDefault)(require("app/components/list"));
const listItem_1 = (0, tslib_1.__importDefault)(require("app/components/list/listItem"));
const tooltip_1 = (0, tslib_1.__importDefault)(require("app/components/tooltip"));
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
var DisplayOption;
(function (DisplayOption) {
    DisplayOption["ABSOLUTE_ADDRESSES"] = "absolute-addresses";
    DisplayOption["ABSOLUTE_FILE_PATHS"] = "absolute-file-paths";
    DisplayOption["VERBOSE_FUNCTION_NAMES"] = "verbose-function-names";
    DisplayOption["FULL_STACK_TRACE"] = "full-stack-trace";
    DisplayOption["MINIFIED"] = "minified";
})(DisplayOption = exports.DisplayOption || (exports.DisplayOption = {}));
function DisplayOptions({ activeDisplayOptions, onChange, hasMinified, hasVerboseFunctionNames, hasAbsoluteFilePaths, hasAbsoluteAddresses, hasAppOnlyFrames, platform, }) {
    function getDisplayOptions() {
        if (platform === 'objc' || platform === 'native' || platform === 'cocoa') {
            return [
                {
                    label: (0, locale_1.t)('Unsymbolicated'),
                    value: DisplayOption.MINIFIED,
                    disabled: !hasMinified,
                    tooltip: !hasMinified ? (0, locale_1.t)('Unsymbolicated version not available') : undefined,
                },
                {
                    label: (0, locale_1.t)('Absolute Addresses'),
                    value: DisplayOption.ABSOLUTE_ADDRESSES,
                    disabled: !hasAbsoluteAddresses,
                    tooltip: !hasAbsoluteAddresses
                        ? (0, locale_1.t)('Absolute Addresses not available')
                        : undefined,
                },
                {
                    label: (0, locale_1.t)('Absolute File Paths'),
                    value: DisplayOption.ABSOLUTE_FILE_PATHS,
                    disabled: !hasAbsoluteFilePaths,
                    tooltip: !hasAbsoluteFilePaths
                        ? (0, locale_1.t)('Absolute File Paths not available')
                        : undefined,
                },
                {
                    label: (0, locale_1.t)('Verbose Function Names'),
                    value: DisplayOption.VERBOSE_FUNCTION_NAMES,
                    disabled: !hasVerboseFunctionNames,
                    tooltip: !hasVerboseFunctionNames
                        ? (0, locale_1.t)('Verbose Function Names not available')
                        : undefined,
                },
                {
                    label: (0, locale_1.t)('Full Stack Trace'),
                    value: DisplayOption.FULL_STACK_TRACE,
                    disabled: !hasAppOnlyFrames,
                    tooltip: !hasAppOnlyFrames ? (0, locale_1.t)('Only full version available') : undefined,
                },
            ];
        }
        return [
            {
                label: (0, locale_1.t)('Minified'),
                value: DisplayOption.MINIFIED,
                disabled: !hasMinified,
                tooltip: !hasMinified ? (0, locale_1.t)('Minified version not available') : undefined,
            },
            {
                label: (0, locale_1.t)('Full Stack Trace'),
                value: DisplayOption.FULL_STACK_TRACE,
                disabled: !hasAppOnlyFrames,
                tooltip: !hasAppOnlyFrames ? (0, locale_1.t)('Only full version available') : undefined,
            },
        ];
    }
    function handleChange(value) {
        const newActiveDisplayOptions = activeDisplayOptions.includes(value)
            ? activeDisplayOptions.filter(activeDisplayOption => activeDisplayOption !== value)
            : [...activeDisplayOptions, value];
        onChange(newActiveDisplayOptions);
    }
    const displayOptions = getDisplayOptions();
    return (<Wrapper button={({ isOpen, getActorProps }) => (<OptionsButton {...getActorProps()} isOpen={isOpen} prefix={(0, locale_1.t)('Options')} size="small" hideBottomBorder={false}>
          {(0, locale_1.tct)('[activeOptionsQuantity] Active', {
                activeOptionsQuantity: activeDisplayOptions.length,
            })}
        </OptionsButton>)}>
      {({ getMenuProps, isOpen }) => (<DropdownMenu {...getMenuProps()} alignMenu="right" isOpen={isOpen} blendWithActor blendCorner>
          <OptionList>
            {displayOptions.map(({ label, value, disabled, tooltip }) => {
                const displayOption = value;
                const isDisabled = !!disabled;
                const isChecked = activeDisplayOptions.includes(displayOption);
                return (<Option key={value} onClick={event => {
                        event.stopPropagation();
                        if (isDisabled) {
                            return;
                        }
                        handleChange(displayOption);
                    }} aria-label={(0, locale_1.t)('Display option')}>
                  <OptionTooltip title={tooltip} disabled={!tooltip}>
                    <ItemContent isDisabled={isDisabled} isChecked={isChecked}>
                      {label}
                      <checkboxFancy_1.default isChecked={isChecked} isDisabled={isDisabled}/>
                    </ItemContent>
                  </OptionTooltip>
                </Option>);
            })}
          </OptionList>
        </DropdownMenu>)}
    </Wrapper>);
}
exports.default = DisplayOptions;
const Wrapper = (0, styled_1.default)(dropdownControl_1.default) `
  z-index: 1;
  &,
  button {
    width: 100%;
    max-width: 100%;
  }
  grid-column: 1/-1;
  grid-row: 3/3;

  @media (min-width: ${p => p.theme.breakpoints[0]}) {
    grid-column: 2/2;
    grid-row: 2/2;
  }

  @media (min-width: ${p => p.theme.breakpoints[3]}) {
    grid-column: auto;
    grid-row: auto;
  }
`;
const DropdownMenu = (0, styled_1.default)(dropdownControl_1.Content) `
  width: 100%;
  border-top: none;

  @media (min-width: ${p => p.theme.breakpoints[0]}) {
    top: calc(100% + ${(0, space_1.default)(0.5)} - 2px);
    border-radius: ${p => p.theme.borderRadius};
    border-top: 1px solid ${p => p.theme.border};
    width: 240px;
  }

  > ul:last-child {
    > li:last-child {
      border-bottom: none;
    }
  }
`;
const OptionsButton = (0, styled_1.default)(dropdownButton_1.default) `
  z-index: ${p => p.theme.zIndex.dropdownAutocomplete.actor};
  white-space: nowrap;

  @media (min-width: ${p => p.theme.breakpoints[0]}) {
    max-width: 200px;
    border-radius: ${p => p.theme.borderRadius};

    ${p => p.isOpen &&
    `
        :before,
        :after {
          position: absolute;
          bottom: calc(${(0, space_1.default)(0.5)} + 1px);
          content: '';
          width: 16px;
          border: 8px solid transparent;
          transform: translateY(calc(50% + 2px));
          right: 9px;
          border-bottom-color: ${p.theme.white};
        }

        :before {
          transform: translateY(calc(50% + 1px));
          border-bottom-color: ${p.theme.border};
        }
      `}
  }

  @media (min-width: ${p => p.theme.breakpoints[3]}) {
    ${button_1.ButtonLabel} {
      grid-template-columns: max-content 1fr max-content;
    }
  }
`;
const OptionList = (0, styled_1.default)(list_1.default) `
  grid-gap: 0;
`;
const ItemContent = (0, styled_1.default)('div') `
  display: grid;
  grid-template-columns: 1fr max-content;
  grid-column-gap: ${(0, space_1.default)(1)};
  padding: ${(0, space_1.default)(1)} ${(0, space_1.default)(2)};
  align-items: center;
  cursor: pointer;
  font-size: ${p => p.theme.fontSizeMedium};

  ${checkboxFancy_1.default} {
    opacity: ${p => (p.isChecked ? 1 : 0.3)};
  }

  :hover {
    background-color: ${p => p.theme.backgroundSecondary};
    ${checkboxFancy_1.default} {
      opacity: 1;
    }
  }

  ${p => p.isDisabled &&
    `
    color: ${p.theme.disabled};
    cursor: not-allowed;

    :hover {
      ${checkboxFancy_1.default} {
        opacity: 0.3;
      }
    }
  `}
`;
const Option = (0, styled_1.default)(listItem_1.default) `
  border-bottom: 1px solid ${p => p.theme.border};
`;
const OptionTooltip = (0, styled_1.default)(tooltip_1.default) `
  width: 100%;
`;
//# sourceMappingURL=displayOptions.jsx.map