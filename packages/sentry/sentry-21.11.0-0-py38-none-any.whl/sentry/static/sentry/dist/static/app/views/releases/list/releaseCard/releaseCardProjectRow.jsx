Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_lazyload_1 = (0, tslib_1.__importDefault)(require("react-lazyload"));
const react_1 = require("@emotion/react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const guideAnchor_1 = (0, tslib_1.__importDefault)(require("app/components/assistant/guideAnchor"));
const button_1 = (0, tslib_1.__importDefault)(require("app/components/button"));
const miniBarChart_1 = (0, tslib_1.__importDefault)(require("app/components/charts/miniBarChart"));
const count_1 = (0, tslib_1.__importDefault)(require("app/components/count"));
const globalSelectionLink_1 = (0, tslib_1.__importDefault)(require("app/components/globalSelectionLink"));
const projectBadge_1 = (0, tslib_1.__importDefault)(require("app/components/idBadge/projectBadge"));
const link_1 = (0, tslib_1.__importDefault)(require("app/components/links/link"));
const notAvailable_1 = (0, tslib_1.__importDefault)(require("app/components/notAvailable"));
const utils_1 = require("app/components/organizations/globalSelectionHeader/utils");
const panels_1 = require("app/components/panels");
const placeholder_1 = (0, tslib_1.__importDefault)(require("app/components/placeholder"));
const tag_1 = (0, tslib_1.__importDefault)(require("app/components/tag"));
const tooltip_1 = (0, tslib_1.__importDefault)(require("app/components/tooltip"));
const locale_1 = require("app/locale");
const overflowEllipsis_1 = (0, tslib_1.__importDefault)(require("app/styles/overflowEllipsis"));
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const utils_2 = require("app/utils");
const sessions_1 = require("app/utils/sessions");
const utils_3 = require("../../utils");
const releasesDisplayOptions_1 = require("../releasesDisplayOptions");
const _1 = require(".");
function ReleaseCardProjectRow({ index, project, organization, location, getHealthData, releaseVersion, activeDisplay, showPlaceholders, showReleaseAdoptionStages, isTopRelease, adoptionStages, }) {
    const theme = (0, react_1.useTheme)();
    const { id, newGroups } = project;
    const crashCount = getHealthData.getCrashCount(releaseVersion, id, releasesDisplayOptions_1.ReleasesDisplayOption.SESSIONS);
    const crashFreeRate = getHealthData.getCrashFreeRate(releaseVersion, id, activeDisplay);
    const get24hCountByProject = getHealthData.get24hCountByProject(id, activeDisplay);
    const timeSeries = getHealthData.getTimeSeries(releaseVersion, id, activeDisplay);
    const adoption = getHealthData.getAdoption(releaseVersion, id, activeDisplay);
    const adoptionStage = showReleaseAdoptionStages &&
        (adoptionStages === null || adoptionStages === void 0 ? void 0 : adoptionStages[project.slug]) &&
        (adoptionStages === null || adoptionStages === void 0 ? void 0 : adoptionStages[project.slug].stage);
    const adoptionStageLabel = Boolean(get24hCountByProject && adoptionStage && (0, utils_3.isMobileRelease)(project.platform)) &&
        utils_3.ADOPTION_STAGE_LABELS[adoptionStage];
    return (<ProjectRow>
      <_1.ReleaseProjectsLayout showReleaseAdoptionStages={showReleaseAdoptionStages}>
        <_1.ReleaseProjectColumn>
          <projectBadge_1.default project={project} avatarSize={16}/>
        </_1.ReleaseProjectColumn>

        {showReleaseAdoptionStages && (<_1.AdoptionStageColumn>
            {adoptionStageLabel ? (<link_1.default to={{
                    pathname: `/organizations/${organization.slug}/releases/`,
                    query: Object.assign(Object.assign({}, location.query), { query: `release.stage:${adoptionStage}` }),
                }}>
                <tooltip_1.default title={adoptionStageLabel.tooltipTitle}>
                  <tag_1.default type={adoptionStageLabel.type}>{adoptionStageLabel.name}</tag_1.default>
                </tooltip_1.default>
              </link_1.default>) : (<notAvailable_1.default />)}
          </_1.AdoptionStageColumn>)}

        <_1.AdoptionColumn>
          {showPlaceholders ? (<StyledPlaceholder width="100px"/>) : (<AdoptionWrapper>
              <span>{adoption ? Math.round(adoption) : '0'}%</span>
              <react_lazyload_1.default debounce={50} height={20}>
                <miniBarChart_1.default series={timeSeries} height={20} isGroupedByDate showTimeInTooltip hideDelay={50} tooltipFormatter={(value) => {
                const suffix = activeDisplay === releasesDisplayOptions_1.ReleasesDisplayOption.USERS
                    ? (0, locale_1.tn)('user', 'users', value)
                    : (0, locale_1.tn)('session', 'sessions', value);
                return `${value.toLocaleString()} ${suffix}`;
            }} colors={[theme.purple300, theme.gray200]}/>
              </react_lazyload_1.default>
            </AdoptionWrapper>)}
        </_1.AdoptionColumn>

        <_1.CrashFreeRateColumn>
          {showPlaceholders ? (<StyledPlaceholder width="60px"/>) : (0, utils_2.defined)(crashFreeRate) ? (<CrashFreeWrapper>
              {(0, sessions_1.getCrashFreeIcon)(crashFreeRate)}
              {(0, utils_3.displayCrashFreePercent)(crashFreeRate)}
            </CrashFreeWrapper>) : (<notAvailable_1.default />)}
        </_1.CrashFreeRateColumn>

        <_1.CrashesColumn>
          {showPlaceholders ? (<StyledPlaceholder width="30px"/>) : (0, utils_2.defined)(crashCount) ? (<tooltip_1.default title={(0, locale_1.t)('Open in Issues')}>
              <globalSelectionLink_1.default to={(0, utils_3.getReleaseUnhandledIssuesUrl)(organization.slug, project.id, releaseVersion)}>
                <count_1.default value={crashCount}/>
              </globalSelectionLink_1.default>
            </tooltip_1.default>) : (<notAvailable_1.default />)}
        </_1.CrashesColumn>

        <_1.NewIssuesColumn>
          <tooltip_1.default title={(0, locale_1.t)('Open in Issues')}>
            <globalSelectionLink_1.default to={(0, utils_3.getReleaseNewIssuesUrl)(organization.slug, project.id, releaseVersion)}>
              <count_1.default value={newGroups || 0}/>
            </globalSelectionLink_1.default>
          </tooltip_1.default>
        </_1.NewIssuesColumn>

        <ViewColumn>
          <guideAnchor_1.default disabled={!isTopRelease || index !== 0} target="view_release">
            <button_1.default size="xsmall" to={{
            pathname: `/organizations/${organization.slug}/releases/${encodeURIComponent(releaseVersion)}/`,
            query: Object.assign(Object.assign({}, (0, utils_1.extractSelectionParameters)(location.query)), { project: project.id, yAxis: undefined }),
        }}>
              {(0, locale_1.t)('View')}
            </button_1.default>
          </guideAnchor_1.default>
        </ViewColumn>
      </_1.ReleaseProjectsLayout>
    </ProjectRow>);
}
exports.default = ReleaseCardProjectRow;
const ProjectRow = (0, styled_1.default)(panels_1.PanelItem) `
  padding: ${(0, space_1.default)(1)} ${(0, space_1.default)(2)};
  @media (min-width: ${p => p.theme.breakpoints[1]}) {
    font-size: ${p => p.theme.fontSizeMedium};
  }
`;
const StyledPlaceholder = (0, styled_1.default)(placeholder_1.default) `
  height: 15px;
  display: inline-block;
  position: relative;
  top: ${(0, space_1.default)(0.25)};
`;
const AdoptionWrapper = (0, styled_1.default)('span') `
  flex: 1;
  display: inline-grid;
  grid-template-columns: 30px 1fr;
  grid-gap: ${(0, space_1.default)(1)};
  align-items: center;

  /* Chart tooltips need overflow */
  overflow: visible;
`;
const CrashFreeWrapper = (0, styled_1.default)('div') `
  display: inline-grid;
  grid-auto-flow: column;
  grid-column-gap: ${(0, space_1.default)(1)};
  align-items: center;
  vertical-align: middle;
`;
const ViewColumn = (0, styled_1.default)('div') `
  ${overflowEllipsis_1.default};
  line-height: 20px;
  text-align: right;
`;
//# sourceMappingURL=releaseCardProjectRow.jsx.map