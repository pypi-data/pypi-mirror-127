Object.defineProperty(exports, "__esModule", { value: true });
exports.SortOption = void 0;
const tslib_1 = require("tslib");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const dropdownControl_1 = (0, tslib_1.__importStar)(require("app/components/dropdownControl"));
const locale_1 = require("app/locale");
var SortOption;
(function (SortOption) {
    SortOption["RECENT_FIRST"] = "recent-first";
    SortOption["RECENT_LAST"] = "recent-last";
})(SortOption = exports.SortOption || (exports.SortOption = {}));
const SORT_OPTIONS = [
    {
        label: (0, locale_1.t)('Recent first'),
        value: SortOption.RECENT_FIRST,
    },
    {
        label: (0, locale_1.t)('Recent last'),
        value: SortOption.RECENT_LAST,
    },
];
function SortOptions({ activeSortOption, onChange, disabled }) {
    var _a;
    const { label: currentLabel, value: currentValue } = (_a = SORT_OPTIONS.find(sortOption => sortOption.value === activeSortOption)) !== null && _a !== void 0 ? _a : SORT_OPTIONS[0];
    return (<Wrapper buttonProps={{
            prefix: (0, locale_1.t)('Sort By'),
            size: 'small',
            disabled,
            title: disabled ? (0, locale_1.t)('Stack trace contains only 1 frame') : undefined,
        }} label={currentLabel}>
      {SORT_OPTIONS.map(({ label, value }) => (<dropdownControl_1.DropdownItem key={value} eventKey={value} isActive={value === currentValue} onSelect={(sortOption) => onChange(sortOption)} aria-label={(0, locale_1.t)('Sort option')}>
          {label}
        </dropdownControl_1.DropdownItem>))}
    </Wrapper>);
}
exports.default = SortOptions;
const Wrapper = (0, styled_1.default)(dropdownControl_1.default) `
  z-index: 2;
  &,
  button {
    width: 100%;
  }
  grid-column: 1/-1;
  grid-row: 2/3;

  @media (min-width: ${p => p.theme.breakpoints[0]}) {
    grid-column: 1/2;
    grid-row: 2/2;
  }

  @media (min-width: ${p => p.theme.breakpoints[2]}) {
    grid-column: auto;
    grid-row: auto;
  }
`;
//# sourceMappingURL=sortOptions.jsx.map