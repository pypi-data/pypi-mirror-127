Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_router_1 = require("react-router");
const react_1 = require("@emotion/react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const feature_1 = (0, tslib_1.__importDefault)(require("app/components/acl/feature"));
const chartZoom_1 = (0, tslib_1.__importDefault)(require("app/components/charts/chartZoom"));
const errorPanel_1 = (0, tslib_1.__importDefault)(require("app/components/charts/errorPanel"));
const lineChart_1 = (0, tslib_1.__importDefault)(require("app/components/charts/lineChart"));
const transitionChart_1 = (0, tslib_1.__importDefault)(require("app/components/charts/transitionChart"));
const transparentLoadingMask_1 = (0, tslib_1.__importDefault)(require("app/components/charts/transparentLoadingMask"));
const notAvailable_1 = (0, tslib_1.__importDefault)(require("app/components/notAvailable"));
const questionTooltip_1 = (0, tslib_1.__importDefault)(require("app/components/questionTooltip"));
const sidebarSection_1 = (0, tslib_1.__importDefault)(require("app/components/sidebarSection"));
const tag_1 = (0, tslib_1.__importDefault)(require("app/components/tag"));
const tooltip_1 = (0, tslib_1.__importDefault)(require("app/components/tooltip"));
const icons_1 = require("app/icons");
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const types_1 = require("app/types");
const formatters_1 = require("app/utils/formatters");
const sessions_1 = require("app/utils/sessions");
const utils_1 = require("../../../utils");
const utils_2 = require("../../utils");
const sessionsAxisIndex = 0;
const usersAxisIndex = 1;
const axisIndexToSessionsField = {
    [sessionsAxisIndex]: types_1.SessionField.SESSIONS,
    [usersAxisIndex]: types_1.SessionField.USERS,
};
function ReleaseAdoption({ release, project, environment, releaseSessions, allSessions, loading, reloading, errored, router, location, }) {
    var _a, _b;
    const theme = (0, react_1.useTheme)();
    const hasUsers = !!(0, sessions_1.getCount)(releaseSessions === null || releaseSessions === void 0 ? void 0 : releaseSessions.groups, types_1.SessionField.USERS);
    function getSeries() {
        if (!releaseSessions) {
            return [];
        }
        const sessionsMarkLines = (0, utils_2.generateReleaseMarkLines)(release, project, theme, location, {
            hideLabel: true,
            axisIndex: sessionsAxisIndex,
        });
        const series = [
            ...sessionsMarkLines,
            {
                seriesName: (0, locale_1.t)('Sessions'),
                connectNulls: true,
                yAxisIndex: sessionsAxisIndex,
                xAxisIndex: sessionsAxisIndex,
                data: (0, sessions_1.getAdoptionSeries)(releaseSessions.groups, allSessions === null || allSessions === void 0 ? void 0 : allSessions.groups, releaseSessions.intervals, types_1.SessionField.SESSIONS),
            },
        ];
        if (hasUsers) {
            const usersMarkLines = (0, utils_2.generateReleaseMarkLines)(release, project, theme, location, {
                hideLabel: true,
                axisIndex: usersAxisIndex,
            });
            series.push(...usersMarkLines);
            series.push({
                seriesName: (0, locale_1.t)('Users'),
                connectNulls: true,
                yAxisIndex: usersAxisIndex,
                xAxisIndex: usersAxisIndex,
                data: (0, sessions_1.getAdoptionSeries)(releaseSessions.groups, allSessions === null || allSessions === void 0 ? void 0 : allSessions.groups, releaseSessions.intervals, types_1.SessionField.USERS),
            });
        }
        return series;
    }
    const colors = theme.charts.getColorPalette(2);
    const axisLineConfig = {
        scale: true,
        axisLine: {
            show: false,
        },
        axisTick: {
            show: false,
        },
        splitLine: {
            show: false,
        },
        max: 100,
        axisLabel: {
            formatter: (value) => `${value}%`,
            color: theme.chartLabel,
        },
    };
    const chartOptions = {
        height: hasUsers ? 280 : 140,
        grid: [
            {
                top: '40px',
                left: '10px',
                right: '10px',
                height: '100px',
            },
            {
                top: '180px',
                left: '10px',
                right: '10px',
                height: '100px',
            },
        ],
        axisPointer: {
            // Link each x-axis together.
            link: [{ xAxisIndex: [sessionsAxisIndex, usersAxisIndex] }],
        },
        xAxes: Array.from(new Array(2)).map((_i, index) => ({
            gridIndex: index,
            type: 'time',
            show: false,
        })),
        yAxes: [
            Object.assign({ gridIndex: sessionsAxisIndex }, axisLineConfig),
            Object.assign({ gridIndex: usersAxisIndex }, axisLineConfig),
        ],
        // utc: utc === 'true', //TODO(release-comparison)
        isGroupedByDate: true,
        showTimeInTooltip: true,
        colors: [colors[0], colors[1]],
        tooltip: {
            trigger: 'axis',
            truncate: 80,
            valueFormatter: (value, label, seriesParams) => {
                const { axisIndex, dataIndex } = seriesParams || {};
                const absoluteCount = (0, sessions_1.getCountAtIndex)(releaseSessions === null || releaseSessions === void 0 ? void 0 : releaseSessions.groups, axisIndexToSessionsField[axisIndex !== null && axisIndex !== void 0 ? axisIndex : 0], dataIndex !== null && dataIndex !== void 0 ? dataIndex : 0);
                return label && Object.values(utils_2.releaseMarkLinesLabels).includes(label)
                    ? ''
                    : `<span>${(0, formatters_1.formatAbbreviatedNumber)(absoluteCount)} <span style="color: ${theme.white};margin-left: ${(0, space_1.default)(0.5)}">${value}%</span></span>`;
            },
            filter: (_, seriesParam) => {
                const { seriesName, axisIndex } = seriesParam;
                // do not display tooltips for "Users Adopted" marklines
                if (axisIndex === usersAxisIndex &&
                    Object.values(utils_2.releaseMarkLinesLabels).includes(seriesName)) {
                    return false;
                }
                return true;
            },
        },
    };
    const { statsPeriod: period, start, end, utc, } = (0, utils_1.getReleaseParams)({
        location,
        releaseBounds: (0, utils_1.getReleaseBounds)(release),
    });
    const adoptionStage = (_b = (_a = release.adoptionStages) === null || _a === void 0 ? void 0 : _a[project.slug]) === null || _b === void 0 ? void 0 : _b.stage;
    const adoptionStageLabel = utils_1.ADOPTION_STAGE_LABELS[adoptionStage];
    const multipleEnvironments = environment.length === 0 || environment.length > 1;
    return (<div>
      {(0, utils_1.isMobileRelease)(project.platform) && (<feature_1.default features={['release-adoption-stage']}>
          <sidebarSection_1.default title={(0, locale_1.t)('Adoption Stage')} icon={multipleEnvironments && (<questionTooltip_1.default position="top" title={(0, locale_1.t)('See if a release has low adoption, been adopted by users, or replaced by another release. Select an environment above to view the stage this release is in.')} size="sm"/>)}>
            {adoptionStageLabel && !multipleEnvironments ? (<div>
                <tooltip_1.default title={adoptionStageLabel.tooltipTitle} isHoverable>
                  <tag_1.default type={adoptionStageLabel.type}>{adoptionStageLabel.name}</tag_1.default>
                </tooltip_1.default>
                <AdoptionEnvironment>
                  {(0, locale_1.tct)(`in [environment]`, { environment })}
                </AdoptionEnvironment>
              </div>) : (<NotAvailableWrapper>
                <notAvailable_1.default />
              </NotAvailableWrapper>)}
          </sidebarSection_1.default>
        </feature_1.default>)}
      <RelativeBox>
        <ChartLabel top="0px">
          <ChartTitle title={(0, locale_1.t)('Sessions Adopted')} icon={<questionTooltip_1.default position="top" title={(0, locale_1.t)('Adoption compares the sessions of a release with the total sessions for this project.')} size="sm"/>}/>
        </ChartLabel>

        {hasUsers && (<ChartLabel top="140px">
            <ChartTitle title={(0, locale_1.t)('Users Adopted')} icon={<questionTooltip_1.default position="top" title={(0, locale_1.t)('Adoption compares the users of a release with the total users for this project.')} size="sm"/>}/>
          </ChartLabel>)}

        {errored ? (<errorPanel_1.default height="280px">
            <icons_1.IconWarning color="gray300" size="lg"/>
          </errorPanel_1.default>) : (<transitionChart_1.default loading={loading} reloading={reloading} height="280px">
            <transparentLoadingMask_1.default visible={reloading}/>
            <chartZoom_1.default router={router} period={period !== null && period !== void 0 ? period : undefined} utc={utc === 'true'} start={start} end={end} usePageDate xAxisIndex={[sessionsAxisIndex, usersAxisIndex]}>
              {zoomRenderProps => (<lineChart_1.default {...chartOptions} {...zoomRenderProps} series={getSeries()}/>)}
            </chartZoom_1.default>
          </transitionChart_1.default>)}
      </RelativeBox>
    </div>);
}
const NotAvailableWrapper = (0, styled_1.default)('div') `
  display: flex;
  align-items: center;
`;
const AdoptionEnvironment = (0, styled_1.default)('span') `
  color: ${p => p.theme.textColor};
  margin-left: ${(0, space_1.default)(0.5)};
  font-size: ${p => p.theme.fontSizeSmall};
`;
const RelativeBox = (0, styled_1.default)('div') `
  position: relative;
`;
const ChartTitle = (0, styled_1.default)(sidebarSection_1.default) `
  margin: 0;
`;
const ChartLabel = (0, styled_1.default)('div') `
  position: absolute;
  top: ${p => p.top};
  z-index: 1;
  left: 0;
  right: 0;
`;
exports.default = (0, react_router_1.withRouter)(ReleaseAdoption);
//# sourceMappingURL=releaseAdoption.jsx.map