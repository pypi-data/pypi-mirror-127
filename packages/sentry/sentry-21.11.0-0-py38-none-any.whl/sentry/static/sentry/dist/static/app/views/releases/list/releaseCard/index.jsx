Object.defineProperty(exports, "__esModule", { value: true });
exports.CrashesColumn = exports.CrashFreeRateColumn = exports.AdoptionStageColumn = exports.AdoptionColumn = exports.NewIssuesColumn = exports.ReleaseProjectColumn = exports.ReleaseProjectsLayout = void 0;
const tslib_1 = require("tslib");
const react_1 = require("react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const color_1 = (0, tslib_1.__importDefault)(require("color"));
const partition_1 = (0, tslib_1.__importDefault)(require("lodash/partition"));
const guideAnchor_1 = (0, tslib_1.__importDefault)(require("app/components/assistant/guideAnchor"));
const button_1 = (0, tslib_1.__importDefault)(require("app/components/button"));
const collapsible_1 = (0, tslib_1.__importDefault)(require("app/components/collapsible"));
const globalSelectionLink_1 = (0, tslib_1.__importDefault)(require("app/components/globalSelectionLink"));
const panels_1 = require("app/components/panels");
const textOverflow_1 = (0, tslib_1.__importDefault)(require("app/components/textOverflow"));
const timeSince_1 = (0, tslib_1.__importDefault)(require("app/components/timeSince"));
const tooltip_1 = (0, tslib_1.__importDefault)(require("app/components/tooltip"));
const version_1 = (0, tslib_1.__importDefault)(require("app/components/version"));
const locale_1 = require("app/locale");
const overflowEllipsis_1 = (0, tslib_1.__importDefault)(require("app/styles/overflowEllipsis"));
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const releaseCardCommits_1 = (0, tslib_1.__importDefault)(require("./releaseCardCommits"));
const releaseCardProjectRow_1 = (0, tslib_1.__importDefault)(require("./releaseCardProjectRow"));
const releaseCardStatsPeriod_1 = (0, tslib_1.__importDefault)(require("./releaseCardStatsPeriod"));
function getReleaseProjectId(release, selection) {
    // if a release has only one project
    if (release.projects.length === 1) {
        return release.projects[0].id;
    }
    // if only one project is selected in global header and release has it (second condition will prevent false positives like -1)
    if (selection.projects.length === 1 &&
        release.projects.map(p => p.id).includes(selection.projects[0])) {
        return selection.projects[0];
    }
    // project selector on release detail page will pick it up
    return undefined;
}
class ReleaseCard extends react_1.Component {
    shouldComponentUpdate(nextProps) {
        // we don't want project health rows to reorder/jump while the whole card is loading
        if (this.props.reloading && nextProps.reloading) {
            return false;
        }
        return true;
    }
    render() {
        const { release, organization, activeDisplay, location, reloading, selection, showHealthPlaceholders, isTopRelease, getHealthData, showReleaseAdoptionStages, } = this.props;
        const { version, commitCount, lastDeploy, dateCreated, versionInfo } = release;
        // sort health rows inside release card alphabetically by project name,
        // show only the ones that are selected in global header
        const [projectsToShow, projectsToHide] = (0, partition_1.default)(release.projects.sort((a, b) => a.slug.localeCompare(b.slug)), p => 
        // do not filter for My Projects & All Projects
        selection.projects.length > 0 && !selection.projects.includes(-1)
            ? selection.projects.includes(p.id)
            : true);
        function getHiddenProjectsTooltip() {
            const limitedProjects = projectsToHide.map(p => p.slug).slice(0, 5);
            const remainderLength = projectsToHide.length - limitedProjects.length;
            if (remainderLength) {
                limitedProjects.push((0, locale_1.tn)('and %s more', 'and %s more', remainderLength));
            }
            return limitedProjects.join(', ');
        }
        return (<StyledPanel reloading={reloading ? 1 : 0}>
        <ReleaseInfo>
          <ReleaseInfoHeader>
            <globalSelectionLink_1.default to={{
                pathname: `/organizations/${organization.slug}/releases/${encodeURIComponent(version)}/`,
                query: { project: getReleaseProjectId(release, selection) },
            }}>
              <guideAnchor_1.default disabled={!isTopRelease} target="release_version">
                <VersionWrapper>
                  <StyledVersion version={version} tooltipRawVersion anchor={false}/>
                </VersionWrapper>
              </guideAnchor_1.default>
            </globalSelectionLink_1.default>
            {commitCount > 0 && (<releaseCardCommits_1.default release={release} withHeading={false}/>)}
          </ReleaseInfoHeader>
          <ReleaseInfoSubheader>
            {(versionInfo === null || versionInfo === void 0 ? void 0 : versionInfo.package) && (<PackageName ellipsisDirection="left">{versionInfo.package}</PackageName>)}
            <timeSince_1.default date={(lastDeploy === null || lastDeploy === void 0 ? void 0 : lastDeploy.dateFinished) || dateCreated}/>
            {(lastDeploy === null || lastDeploy === void 0 ? void 0 : lastDeploy.dateFinished) && ` \u007C ${lastDeploy.environment}`}
          </ReleaseInfoSubheader>
        </ReleaseInfo>

        <ReleaseProjects>
          <ReleaseProjectsHeader>
            <exports.ReleaseProjectsLayout showReleaseAdoptionStages={showReleaseAdoptionStages}>
              <exports.ReleaseProjectColumn>{(0, locale_1.t)('Project Name')}</exports.ReleaseProjectColumn>
              {showReleaseAdoptionStages && (<exports.AdoptionStageColumn>{(0, locale_1.t)('Adoption Stage')}</exports.AdoptionStageColumn>)}
              <exports.AdoptionColumn>
                <span>{(0, locale_1.t)('Adoption')}</span>
                <releaseCardStatsPeriod_1.default location={location}/>
              </exports.AdoptionColumn>
              <exports.CrashFreeRateColumn>{(0, locale_1.t)('Crash Free Rate')}</exports.CrashFreeRateColumn>
              <exports.CrashesColumn>{(0, locale_1.t)('Crashes')}</exports.CrashesColumn>
              <exports.NewIssuesColumn>{(0, locale_1.t)('New Issues')}</exports.NewIssuesColumn>
            </exports.ReleaseProjectsLayout>
          </ReleaseProjectsHeader>

          <ProjectRows>
            <collapsible_1.default expandButton={({ onExpand, numberOfHiddenItems }) => (<ExpandButtonWrapper>
                  <button_1.default priority="primary" size="xsmall" onClick={onExpand}>
                    {(0, locale_1.tct)('Show [numberOfHiddenItems] More', { numberOfHiddenItems })}
                  </button_1.default>
                </ExpandButtonWrapper>)} collapseButton={({ onCollapse }) => (<CollapseButtonWrapper>
                  <button_1.default priority="primary" size="xsmall" onClick={onCollapse}>
                    {(0, locale_1.t)('Collapse')}
                  </button_1.default>
                </CollapseButtonWrapper>)}>
              {projectsToShow.map((project, index) => (<releaseCardProjectRow_1.default key={`${release.version}-${project.slug}-row`} index={index} organization={organization} project={project} location={location} getHealthData={getHealthData} releaseVersion={release.version} activeDisplay={activeDisplay} showPlaceholders={showHealthPlaceholders} showReleaseAdoptionStages={showReleaseAdoptionStages} isTopRelease={isTopRelease} adoptionStages={release.adoptionStages}/>))}
            </collapsible_1.default>
          </ProjectRows>

          {projectsToHide.length > 0 && (<HiddenProjectsMessage>
              <tooltip_1.default title={getHiddenProjectsTooltip()}>
                <textOverflow_1.default>
                  {projectsToHide.length === 1
                    ? (0, locale_1.tct)('[number:1] hidden project', { number: <strong /> })
                    : (0, locale_1.tct)('[number] hidden projects', {
                        number: <strong>{projectsToHide.length}</strong>,
                    })}
                </textOverflow_1.default>
              </tooltip_1.default>
            </HiddenProjectsMessage>)}
        </ReleaseProjects>
      </StyledPanel>);
    }
}
const VersionWrapper = (0, styled_1.default)('div') `
  display: flex;
  align-items: center;
`;
const StyledVersion = (0, styled_1.default)(version_1.default) `
  ${overflowEllipsis_1.default};
`;
const StyledPanel = (0, styled_1.default)(panels_1.Panel) `
  opacity: ${p => (p.reloading ? 0.5 : 1)};
  pointer-events: ${p => (p.reloading ? 'none' : 'auto')};

  @media (min-width: ${p => p.theme.breakpoints[1]}) {
    display: flex;
  }
`;
const ReleaseInfo = (0, styled_1.default)('div') `
  padding: ${(0, space_1.default)(1.5)} ${(0, space_1.default)(2)};
  flex-shrink: 0;

  @media (min-width: ${p => p.theme.breakpoints[1]}) {
    border-right: 1px solid ${p => p.theme.border};
    min-width: 260px;
    width: 22%;
    max-width: 300px;
  }
`;
const ReleaseInfoSubheader = (0, styled_1.default)('div') `
  font-size: ${p => p.theme.fontSizeSmall};
  color: ${p => p.theme.gray400};
`;
const PackageName = (0, styled_1.default)(textOverflow_1.default) `
  font-size: ${p => p.theme.fontSizeMedium};
  color: ${p => p.theme.textColor};
`;
const ReleaseProjects = (0, styled_1.default)('div') `
  border-top: 1px solid ${p => p.theme.border};
  flex-grow: 1;
  display: grid;

  @media (min-width: ${p => p.theme.breakpoints[1]}) {
    border-top: none;
  }
`;
const ReleaseInfoHeader = (0, styled_1.default)('div') `
  font-size: ${p => p.theme.fontSizeExtraLarge};
  display: grid;
  grid-template-columns: minmax(0, 1fr) max-content;
  grid-gap: ${(0, space_1.default)(2)};
  align-items: center;
`;
const ReleaseProjectsHeader = (0, styled_1.default)(panels_1.PanelHeader) `
  border-top-left-radius: 0;
  padding: ${(0, space_1.default)(1.5)} ${(0, space_1.default)(2)};
  font-size: ${p => p.theme.fontSizeSmall};
`;
const ProjectRows = (0, styled_1.default)('div') `
  position: relative;
`;
const ExpandButtonWrapper = (0, styled_1.default)('div') `
  position: absolute;
  width: 100%;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: linear-gradient(
    180deg,
    ${p => (0, color_1.default)(p.theme.background).alpha(0).string()} 0,
    ${p => p.theme.background}
  );
  background-repeat: repeat-x;
  border-bottom: ${(0, space_1.default)(1)} solid ${p => p.theme.background};
  border-top: ${(0, space_1.default)(1)} solid transparent;
  border-bottom-right-radius: ${p => p.theme.borderRadius};
  @media (max-width: ${p => p.theme.breakpoints[1]}) {
    border-bottom-left-radius: ${p => p.theme.borderRadius};
  }
`;
const CollapseButtonWrapper = (0, styled_1.default)('div') `
  display: flex;
  align-items: center;
  justify-content: center;
  height: 41px;
`;
exports.ReleaseProjectsLayout = (0, styled_1.default)('div') `
  display: grid;
  grid-template-columns: 1fr 1.4fr 0.6fr 0.7fr;

  grid-column-gap: ${(0, space_1.default)(1)};
  align-items: center;
  width: 100%;

  @media (min-width: ${p => p.theme.breakpoints[0]}) {
    grid-template-columns: 1fr 1fr 1fr 0.5fr 0.5fr 0.5fr;
  }

  @media (min-width: ${p => p.theme.breakpoints[1]}) {
    grid-template-columns: 1fr 1fr 1fr 0.5fr 0.5fr 0.5fr;
  }

  @media (min-width: ${p => p.theme.breakpoints[3]}) {
    ${p => p.showReleaseAdoptionStages
    ? `
      grid-template-columns: 1fr 0.7fr 1fr 1fr 0.7fr 0.7fr 0.5fr;
    `
    : `
      grid-template-columns: 1fr 1fr 1fr 0.7fr 0.7fr 0.5fr;
    `}
  }
`;
exports.ReleaseProjectColumn = (0, styled_1.default)('div') `
  ${overflowEllipsis_1.default};
  line-height: 20px;
`;
exports.NewIssuesColumn = (0, styled_1.default)(exports.ReleaseProjectColumn) `
  font-variant-numeric: tabular-nums;

  @media (min-width: ${p => p.theme.breakpoints[0]}) {
    text-align: right;
  }
`;
exports.AdoptionColumn = (0, styled_1.default)(exports.ReleaseProjectColumn) `
  display: none;
  font-variant-numeric: tabular-nums;

  @media (min-width: ${p => p.theme.breakpoints[0]}) {
    display: flex;
    /* Chart tooltips need overflow */
    overflow: visible;
  }

  & > * {
    flex: 1;
  }
`;
exports.AdoptionStageColumn = (0, styled_1.default)(exports.ReleaseProjectColumn) `
  display: none;
  font-variant-numeric: tabular-nums;

  @media (min-width: ${p => p.theme.breakpoints[3]}) {
    display: flex;

    /* Need to show the edges of the tags */
    overflow: visible;
  }
`;
exports.CrashFreeRateColumn = (0, styled_1.default)(exports.ReleaseProjectColumn) `
  font-variant-numeric: tabular-nums;

  @media (min-width: ${p => p.theme.breakpoints[0]}) {
    text-align: center;
  }

  @media (min-width: ${p => p.theme.breakpoints[3]}) {
    text-align: right;
  }
`;
exports.CrashesColumn = (0, styled_1.default)(exports.ReleaseProjectColumn) `
  display: none;
  font-variant-numeric: tabular-nums;

  @media (min-width: ${p => p.theme.breakpoints[0]}) {
    display: block;
    text-align: right;
  }
`;
const HiddenProjectsMessage = (0, styled_1.default)('div') `
  display: flex;
  align-items: center;
  font-size: ${p => p.theme.fontSizeSmall};
  padding: 0 ${(0, space_1.default)(2)};
  border-top: 1px solid ${p => p.theme.border};
  overflow: hidden;
  height: 24px;
  line-height: 24px;
  color: ${p => p.theme.gray300};
  background-color: ${p => p.theme.backgroundSecondary};
  border-bottom-right-radius: ${p => p.theme.borderRadius};
  @media (max-width: ${p => p.theme.breakpoints[1]}) {
    border-bottom-left-radius: ${p => p.theme.borderRadius};
  }
`;
exports.default = ReleaseCard;
//# sourceMappingURL=index.jsx.map