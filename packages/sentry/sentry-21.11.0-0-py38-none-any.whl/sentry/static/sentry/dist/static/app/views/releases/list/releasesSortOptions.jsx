Object.defineProperty(exports, "__esModule", { value: true });
exports.ReleasesSortOption = void 0;
const tslib_1 = require("tslib");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const locale_1 = require("app/locale");
const releasesDisplayOptions_1 = require("./releasesDisplayOptions");
const releasesDropdown_1 = (0, tslib_1.__importDefault)(require("./releasesDropdown"));
var ReleasesSortOption;
(function (ReleasesSortOption) {
    ReleasesSortOption["CRASH_FREE_USERS"] = "crash_free_users";
    ReleasesSortOption["CRASH_FREE_SESSIONS"] = "crash_free_sessions";
    ReleasesSortOption["USERS_24_HOURS"] = "users_24h";
    ReleasesSortOption["SESSIONS_24_HOURS"] = "sessions_24h";
    ReleasesSortOption["SESSIONS"] = "sessions";
    ReleasesSortOption["DATE"] = "date";
    ReleasesSortOption["BUILD"] = "build";
    ReleasesSortOption["SEMVER"] = "semver";
    ReleasesSortOption["ADOPTION"] = "adoption";
})(ReleasesSortOption = exports.ReleasesSortOption || (exports.ReleasesSortOption = {}));
function ReleasesSortOptions({ selected, selectedDisplay, onSelect, organization, environments, }) {
    const sortOptions = Object.assign({ [ReleasesSortOption.DATE]: { label: (0, locale_1.t)('Date Created') }, [ReleasesSortOption.SESSIONS]: { label: (0, locale_1.t)('Total Sessions') } }, (selectedDisplay === releasesDisplayOptions_1.ReleasesDisplayOption.USERS
        ? {
            [ReleasesSortOption.USERS_24_HOURS]: { label: (0, locale_1.t)('Active Users') },
            [ReleasesSortOption.CRASH_FREE_USERS]: { label: (0, locale_1.t)('Crash Free Users') },
        }
        : {
            [ReleasesSortOption.SESSIONS_24_HOURS]: { label: (0, locale_1.t)('Active Sessions') },
            [ReleasesSortOption.CRASH_FREE_SESSIONS]: { label: (0, locale_1.t)('Crash Free Sessions') },
        }));
    if (organization.features.includes('semver')) {
        sortOptions[ReleasesSortOption.BUILD] = { label: (0, locale_1.t)('Build Number') };
        sortOptions[ReleasesSortOption.SEMVER] = { label: (0, locale_1.t)('Semantic Version') };
    }
    if (organization.features.includes('release-adoption-stage')) {
        const isDisabled = environments.length !== 1;
        sortOptions[ReleasesSortOption.ADOPTION] = {
            label: (0, locale_1.t)('Date Adopted'),
            disabled: isDisabled,
            tooltip: isDisabled
                ? (0, locale_1.t)('Select one environment to use this sort option.')
                : undefined,
        };
    }
    return (<StyledReleasesDropdown label={(0, locale_1.t)('Sort By')} options={sortOptions} selected={selected} onSelect={onSelect}/>);
}
exports.default = ReleasesSortOptions;
const StyledReleasesDropdown = (0, styled_1.default)(releasesDropdown_1.default) `
  z-index: 2;
  @media (max-width: ${p => p.theme.breakpoints[2]}) {
    order: 2;
  }
`;
//# sourceMappingURL=releasesSortOptions.jsx.map