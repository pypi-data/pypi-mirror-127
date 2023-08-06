Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const react_2 = require("@emotion/react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const pick_1 = (0, tslib_1.__importDefault)(require("lodash/pick"));
const moment_1 = (0, tslib_1.__importDefault)(require("moment"));
const teamSelector_1 = (0, tslib_1.__importDefault)(require("app/components/forms/teamSelector"));
const Layout = (0, tslib_1.__importStar)(require("app/components/layouts/thirds"));
const loadingIndicator_1 = (0, tslib_1.__importDefault)(require("app/components/loadingIndicator"));
const noProjectMessage_1 = (0, tslib_1.__importDefault)(require("app/components/noProjectMessage"));
const getParams_1 = require("app/components/organizations/globalSelectionHeader/getParams");
const pageTimeRangeSelector_1 = (0, tslib_1.__importDefault)(require("app/components/pageTimeRangeSelector"));
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const trackAdvancedAnalyticsEvent_1 = (0, tslib_1.__importDefault)(require("app/utils/analytics/trackAdvancedAnalyticsEvent"));
const isActiveSuperuser_1 = require("app/utils/isActiveSuperuser");
const localStorage_1 = (0, tslib_1.__importDefault)(require("app/utils/localStorage"));
const useOrganization_1 = (0, tslib_1.__importDefault)(require("app/utils/useOrganization"));
const useTeams_1 = (0, tslib_1.__importDefault)(require("app/utils/useTeams"));
const header_1 = (0, tslib_1.__importDefault)(require("../header"));
const descriptionCard_1 = (0, tslib_1.__importDefault)(require("./descriptionCard"));
const teamAlertsTriggered_1 = (0, tslib_1.__importDefault)(require("./teamAlertsTriggered"));
const teamIssuesReviewed_1 = (0, tslib_1.__importDefault)(require("./teamIssuesReviewed"));
const teamMisery_1 = (0, tslib_1.__importDefault)(require("./teamMisery"));
const teamReleases_1 = (0, tslib_1.__importDefault)(require("./teamReleases"));
const teamResolutionTime_1 = (0, tslib_1.__importDefault)(require("./teamResolutionTime"));
const teamStability_1 = (0, tslib_1.__importDefault)(require("./teamStability"));
const INSIGHTS_DEFAULT_STATS_PERIOD = '8w';
const PAGE_QUERY_PARAMS = [
    'pageStatsPeriod',
    'pageStart',
    'pageEnd',
    'pageUtc',
    'dataCategory',
    'transform',
    'sort',
    'query',
    'cursor',
    'team',
];
function TeamInsightsOverview({ location, router }) {
    var _a, _b, _c, _d;
    const isSuperuser = (0, isActiveSuperuser_1.isActiveSuperuser)();
    const organization = (0, useOrganization_1.default)();
    const { teams, initiallyLoaded } = (0, useTeams_1.default)({ provideUserTeams: true });
    const theme = (0, react_2.useTheme)();
    const query = (_a = location === null || location === void 0 ? void 0 : location.query) !== null && _a !== void 0 ? _a : {};
    const localStorageKey = `teamInsightsSelectedTeamId:${organization.slug}`;
    let localTeamId = (_b = query.team) !== null && _b !== void 0 ? _b : localStorage_1.default.getItem(localStorageKey);
    if (localTeamId && !teams.find(team => team.id === localTeamId)) {
        localTeamId = null;
    }
    const currentTeamId = localTeamId !== null && localTeamId !== void 0 ? localTeamId : (_c = teams[0]) === null || _c === void 0 ? void 0 : _c.id;
    const currentTeam = teams.find(team => team.id === currentTeamId);
    const projects = (_d = currentTeam === null || currentTeam === void 0 ? void 0 : currentTeam.projects) !== null && _d !== void 0 ? _d : [];
    (0, react_1.useEffect)(() => {
        (0, trackAdvancedAnalyticsEvent_1.default)('team_insights.viewed', {
            organization,
        });
    }, []);
    function handleChangeTeam(teamId) {
        localStorage_1.default.setItem(localStorageKey, teamId);
        setStateOnUrl({ team: teamId });
    }
    function handleUpdateDatetime(datetime) {
        const { start, end, relative, utc } = datetime;
        if (start && end) {
            const parser = utc ? moment_1.default.utc : moment_1.default;
            return setStateOnUrl({
                pageStatsPeriod: undefined,
                pageStart: parser(start).format(),
                pageEnd: parser(end).format(),
                pageUtc: utc !== null && utc !== void 0 ? utc : undefined,
            });
        }
        return setStateOnUrl({
            pageStatsPeriod: relative || undefined,
            pageStart: undefined,
            pageEnd: undefined,
            pageUtc: undefined,
        });
    }
    function setStateOnUrl(nextState) {
        const nextQueryParams = (0, pick_1.default)(nextState, PAGE_QUERY_PARAMS);
        const nextLocation = Object.assign(Object.assign({}, location), { query: Object.assign(Object.assign({}, query), nextQueryParams) });
        router.push(nextLocation);
        return nextLocation;
    }
    function dataDatetime() {
        const { start, end, statsPeriod, utc: utcString, } = (0, getParams_1.getParams)(query, {
            allowEmptyPeriod: true,
            allowAbsoluteDatetime: true,
            allowAbsolutePageDatetime: true,
        });
        if (!statsPeriod && !start && !end) {
            return { period: INSIGHTS_DEFAULT_STATS_PERIOD };
        }
        // Following getParams, statsPeriod will take priority over start/end
        if (statsPeriod) {
            return { period: statsPeriod };
        }
        const utc = utcString === 'true';
        if (start && end) {
            return utc
                ? {
                    start: moment_1.default.utc(start).format(),
                    end: moment_1.default.utc(end).format(),
                    utc,
                }
                : {
                    start: (0, moment_1.default)(start).utc().format(),
                    end: (0, moment_1.default)(end).utc().format(),
                    utc,
                };
        }
        return { period: INSIGHTS_DEFAULT_STATS_PERIOD };
    }
    const { period, start, end, utc } = dataDatetime();
    if (teams.length === 0) {
        return (<noProjectMessage_1.default organization={organization} superuserNeedsToBeProjectMember/>);
    }
    return (<react_1.Fragment>
      <header_1.default organization={organization} activeTab="team"/>

      <Body>
        {!initiallyLoaded && <loadingIndicator_1.default />}
        {initiallyLoaded && (<Layout.Main fullWidth>
            <ControlsWrapper>
              <StyledTeamSelector name="select-team" inFieldLabel={(0, locale_1.t)('Team: ')} value={currentTeam === null || currentTeam === void 0 ? void 0 : currentTeam.slug} onChange={choice => handleChangeTeam(choice.actor.id)} teamFilter={isSuperuser ? undefined : filterTeam => filterTeam.isMember} styles={{
                singleValue(provided) {
                    const custom = {
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center',
                        fontSize: theme.fontSizeMedium,
                        ':before': Object.assign(Object.assign({}, provided[':before']), { color: theme.textColor, marginRight: (0, space_1.default)(1.5), marginLeft: (0, space_1.default)(0.5) }),
                    };
                    return Object.assign(Object.assign({}, provided), custom);
                },
                input: (provided, state) => (Object.assign(Object.assign({}, provided), { display: 'grid', gridTemplateColumns: 'max-content 1fr', alignItems: 'center', gridGap: (0, space_1.default)(1), ':before': {
                        backgroundColor: state.theme.backgroundSecondary,
                        height: 24,
                        width: 38,
                        borderRadius: 3,
                        content: '""',
                        display: 'block',
                    } })),
            }}/>
              <StyledPageTimeRangeSelector organization={organization} relative={period !== null && period !== void 0 ? period : ''} start={start !== null && start !== void 0 ? start : null} end={end !== null && end !== void 0 ? end : null} utc={utc !== null && utc !== void 0 ? utc : null} onUpdate={handleUpdateDatetime} showAbsolute={false} relativeOptions={{
                '14d': (0, locale_1.t)('Last 2 weeks'),
                '4w': (0, locale_1.t)('Last 4 weeks'),
                [INSIGHTS_DEFAULT_STATS_PERIOD]: (0, locale_1.t)('Last 8 weeks'),
                '12w': (0, locale_1.t)('Last 12 weeks'),
            }}/>
            </ControlsWrapper>

            <SectionTitle>{(0, locale_1.t)('Project Health')}</SectionTitle>
            <descriptionCard_1.default title={(0, locale_1.t)('Crash Free Sessions')} description={(0, locale_1.t)('The percentage of healthy, errored, and abnormal sessions that didn’t cause a crash.')}>
              <teamStability_1.default projects={projects} organization={organization} period={period} start={start} end={end} utc={utc}/>
            </descriptionCard_1.default>

            <descriptionCard_1.default title={(0, locale_1.t)('User Misery')} description={(0, locale_1.t)('The number of unique users that experienced load times 4x the project’s configured threshold.')}>
              <teamMisery_1.default organization={organization} projects={projects} teamId={currentTeam.id} period={period} start={start === null || start === void 0 ? void 0 : start.toString()} end={end === null || end === void 0 ? void 0 : end.toString()} location={location}/>
            </descriptionCard_1.default>

            <descriptionCard_1.default title={(0, locale_1.t)('Metric Alerts Triggered')} description={(0, locale_1.t)('Alerts triggered from the Alert Rules your team created.')}>
              <teamAlertsTriggered_1.default organization={organization} teamSlug={currentTeam.slug} period={period} start={start === null || start === void 0 ? void 0 : start.toString()} end={end === null || end === void 0 ? void 0 : end.toString()} location={location}/>
            </descriptionCard_1.default>

            <SectionTitle>{(0, locale_1.t)('Team Activity')}</SectionTitle>
            <descriptionCard_1.default title={(0, locale_1.t)('Issues Reviewed')} description={(0, locale_1.t)('Issues triaged by your team taking an action on them such as resolving, ignoring, marking as reviewed, or deleting.')}>
              <teamIssuesReviewed_1.default organization={organization} projects={projects} teamSlug={currentTeam.slug} period={period} start={start === null || start === void 0 ? void 0 : start.toString()} end={end === null || end === void 0 ? void 0 : end.toString()} location={location}/>
            </descriptionCard_1.default>
            <descriptionCard_1.default title={(0, locale_1.t)('Time to Resolution')} description={(0, locale_1.t)(`The mean time it took for issues to be resolved by your team.`)}>
              <teamResolutionTime_1.default organization={organization} teamSlug={currentTeam.slug} period={period} start={start === null || start === void 0 ? void 0 : start.toString()} end={end === null || end === void 0 ? void 0 : end.toString()} location={location}/>
            </descriptionCard_1.default>
            <descriptionCard_1.default title={(0, locale_1.t)('Number of Releases')} description={(0, locale_1.t)('A breakdown showing how your team shipped releases over time.')}>
              <teamReleases_1.default projects={projects} organization={organization} teamSlug={currentTeam.slug} period={period} start={start} end={end} utc={utc}/>
            </descriptionCard_1.default>
          </Layout.Main>)}
      </Body>
    </react_1.Fragment>);
}
exports.default = TeamInsightsOverview;
const Body = (0, styled_1.default)(Layout.Body) `
  margin-bottom: -20px;

  @media (min-width: ${p => p.theme.breakpoints[1]}) {
    display: block;
  }
`;
const ControlsWrapper = (0, styled_1.default)('div') `
  display: grid;
  align-items: center;
  gap: ${(0, space_1.default)(1)};
  margin-bottom: ${(0, space_1.default)(2)};

  @media (min-width: ${p => p.theme.breakpoints[0]}) {
    grid-template-columns: 246px 1fr;
  }
`;
const StyledTeamSelector = (0, styled_1.default)(teamSelector_1.default) `
  & > div {
    box-shadow: ${p => p.theme.dropShadowLight};
  }
`;
const StyledPageTimeRangeSelector = (0, styled_1.default)(pageTimeRangeSelector_1.default) `
  height: 40px;

  div {
    min-height: unset;
  }
`;
const SectionTitle = (0, styled_1.default)(Layout.Title) `
  margin-bottom: ${(0, space_1.default)(1)} !important;
`;
//# sourceMappingURL=overview.jsx.map