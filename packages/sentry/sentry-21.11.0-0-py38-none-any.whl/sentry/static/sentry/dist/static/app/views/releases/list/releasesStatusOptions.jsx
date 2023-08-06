Object.defineProperty(exports, "__esModule", { value: true });
exports.ReleasesStatusOption = void 0;
const tslib_1 = require("tslib");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const locale_1 = require("app/locale");
const releasesDropdown_1 = (0, tslib_1.__importDefault)(require("./releasesDropdown"));
var ReleasesStatusOption;
(function (ReleasesStatusOption) {
    ReleasesStatusOption["ACTIVE"] = "active";
    ReleasesStatusOption["ARCHIVED"] = "archived";
})(ReleasesStatusOption = exports.ReleasesStatusOption || (exports.ReleasesStatusOption = {}));
const options = {
    [ReleasesStatusOption.ACTIVE]: { label: (0, locale_1.t)('Active') },
    [ReleasesStatusOption.ARCHIVED]: { label: (0, locale_1.t)('Archived') },
};
function ReleasesStatusOptions({ selected, onSelect }) {
    return (<StyledReleasesDropdown label={(0, locale_1.t)('Status')} options={options} selected={selected} onSelect={onSelect}/>);
}
exports.default = ReleasesStatusOptions;
const StyledReleasesDropdown = (0, styled_1.default)(releasesDropdown_1.default) `
  z-index: 3;
  @media (max-width: ${p => p.theme.breakpoints[2]}) {
    order: 1;
  }
`;
//# sourceMappingURL=releasesStatusOptions.jsx.map