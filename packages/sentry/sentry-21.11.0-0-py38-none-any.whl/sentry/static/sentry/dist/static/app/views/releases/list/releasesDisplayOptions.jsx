Object.defineProperty(exports, "__esModule", { value: true });
exports.ReleasesDisplayOption = void 0;
const tslib_1 = require("tslib");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const locale_1 = require("app/locale");
const releasesDropdown_1 = (0, tslib_1.__importDefault)(require("./releasesDropdown"));
var ReleasesDisplayOption;
(function (ReleasesDisplayOption) {
    ReleasesDisplayOption["USERS"] = "users";
    ReleasesDisplayOption["SESSIONS"] = "sessions";
})(ReleasesDisplayOption = exports.ReleasesDisplayOption || (exports.ReleasesDisplayOption = {}));
const displayOptions = {
    [ReleasesDisplayOption.SESSIONS]: { label: (0, locale_1.t)('Sessions') },
    [ReleasesDisplayOption.USERS]: { label: (0, locale_1.t)('Users') },
};
function ReleasesDisplayOptions({ selected, onSelect }) {
    return (<StyledReleasesDropdown label={(0, locale_1.t)('Display')} options={displayOptions} selected={selected} onSelect={onSelect}/>);
}
exports.default = ReleasesDisplayOptions;
const StyledReleasesDropdown = (0, styled_1.default)(releasesDropdown_1.default) `
  z-index: 1;
  @media (max-width: ${p => p.theme.breakpoints[2]}) {
    order: 3;
  }
`;
//# sourceMappingURL=releasesDisplayOptions.jsx.map