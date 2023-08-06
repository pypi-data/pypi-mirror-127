Object.defineProperty(exports, "__esModule", { value: true });
exports.getTeamParams = void 0;
const tslib_1 = require("tslib");
const react_1 = require("react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const debounce_1 = (0, tslib_1.__importDefault)(require("lodash/debounce"));
const input_1 = (0, tslib_1.__importDefault)(require("app/components/forms/input"));
const loadingIndicator_1 = (0, tslib_1.__importDefault)(require("app/components/loadingIndicator"));
const constants_1 = require("app/constants");
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const useTeams_1 = (0, tslib_1.__importDefault)(require("app/utils/useTeams"));
const filter_1 = (0, tslib_1.__importDefault)(require("./filter"));
const ALERT_LIST_QUERY_DEFAULT_TEAMS = ['myteams', 'unassigned'];
function getTeamParams(team) {
    if (team === undefined) {
        return ALERT_LIST_QUERY_DEFAULT_TEAMS;
    }
    if (team === '') {
        return [];
    }
    if (Array.isArray(team)) {
        return team;
    }
    return [team];
}
exports.getTeamParams = getTeamParams;
function TeamFilter({ selectedTeams, showStatus = false, selectedStatus = new Set(), handleChangeFilter, }) {
    const { teams, onSearch, fetching } = (0, useTeams_1.default)();
    const debouncedSearch = (0, debounce_1.default)(onSearch, constants_1.DEFAULT_DEBOUNCE_DURATION);
    const [teamFilterSearch, setTeamFilterSearch] = (0, react_1.useState)();
    const statusOptions = [
        {
            label: (0, locale_1.t)('Unresolved'),
            value: 'open',
            checked: selectedStatus.has('open'),
            filtered: false,
        },
        {
            label: (0, locale_1.t)('Resolved'),
            value: 'closed',
            checked: selectedStatus.has('closed'),
            filtered: false,
        },
    ];
    const additionalOptions = [
        {
            label: (0, locale_1.t)('My Teams'),
            value: 'myteams',
            checked: selectedTeams.has('myteams'),
            filtered: false,
        },
        {
            label: (0, locale_1.t)('Unassigned'),
            value: 'unassigned',
            checked: selectedTeams.has('unassigned'),
            filtered: false,
        },
    ];
    const teamItems = teams.map(({ id, slug }) => ({
        label: slug,
        value: id,
        filtered: teamFilterSearch
            ? !slug.toLowerCase().includes(teamFilterSearch.toLowerCase())
            : false,
        checked: selectedTeams.has(id),
    }));
    return (<filter_1.default header={<InputWrapper>
          <StyledInput autoFocus placeholder={(0, locale_1.t)('Filter by team slug')} onClick={event => {
                event.stopPropagation();
            }} onChange={(event) => {
                const search = event.target.value;
                setTeamFilterSearch(search);
                debouncedSearch(search);
            }} value={teamFilterSearch || ''}/>
          {fetching && <StyledLoadingIndicator size={16} mini/>}
        </InputWrapper>} onFilterChange={handleChangeFilter} dropdownSections={[
            ...(showStatus
                ? [
                    {
                        id: 'status',
                        label: (0, locale_1.t)('Status'),
                        items: statusOptions,
                    },
                ]
                : []),
            {
                id: 'teams',
                label: (0, locale_1.t)('Teams'),
                items: [...additionalOptions, ...teamItems],
            },
        ]}/>);
}
exports.default = TeamFilter;
const InputWrapper = (0, styled_1.default)('div') `
  position: relative;
`;
const StyledInput = (0, styled_1.default)(input_1.default) `
  border: none;
  border-bottom: 1px solid transparent;
  border-radius: 0;
`;
const StyledLoadingIndicator = (0, styled_1.default)(loadingIndicator_1.default) `
  position: absolute;
  right: 0;
  top: ${(0, space_1.default)(0.75)};
`;
//# sourceMappingURL=teamFilter.jsx.map