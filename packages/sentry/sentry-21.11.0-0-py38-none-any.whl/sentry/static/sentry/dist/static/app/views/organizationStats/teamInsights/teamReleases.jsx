Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const react_1 = require("react");
const react_2 = require("@emotion/react");
const styled_1 = (0, tslib_1.__importDefault)(require("@emotion/styled"));
const isEqual_1 = (0, tslib_1.__importDefault)(require("lodash/isEqual"));
const round_1 = (0, tslib_1.__importDefault)(require("lodash/round"));
const moment_1 = (0, tslib_1.__importDefault)(require("moment"));
const asyncComponent_1 = (0, tslib_1.__importDefault)(require("app/components/asyncComponent"));
const barChart_1 = (0, tslib_1.__importDefault)(require("app/components/charts/barChart"));
const markLine_1 = (0, tslib_1.__importDefault)(require("app/components/charts/components/markLine"));
const idBadge_1 = (0, tslib_1.__importDefault)(require("app/components/idBadge"));
const link_1 = (0, tslib_1.__importDefault)(require("app/components/links/link"));
const getParams_1 = require("app/components/organizations/globalSelectionHeader/getParams");
const panelTable_1 = (0, tslib_1.__importDefault)(require("app/components/panels/panelTable"));
const placeholder_1 = (0, tslib_1.__importDefault)(require("app/components/placeholder"));
const icons_1 = require("app/icons");
const locale_1 = require("app/locale");
const space_1 = (0, tslib_1.__importDefault)(require("app/styles/space"));
const utils_1 = require("./utils");
class TeamReleases extends asyncComponent_1.default {
    constructor() {
        super(...arguments);
        this.shouldRenderBadRequests = true;
    }
    getDefaultState() {
        return Object.assign(Object.assign({}, super.getDefaultState()), { weekReleases: null, periodReleases: null });
    }
    getEndpoints() {
        const { organization, start, end, period, utc, teamSlug } = this.props;
        const datetime = { start, end, period, utc };
        const endpoints = [
            [
                'periodReleases',
                `/teams/${organization.slug}/${teamSlug}/release-count/`,
                {
                    query: Object.assign({}, (0, getParams_1.getParams)(datetime)),
                },
            ],
            [
                'weekReleases',
                `/teams/${organization.slug}/${teamSlug}/release-count/`,
                {
                    query: {
                        statsPeriod: '7d',
                    },
                },
            ],
        ];
        return endpoints;
    }
    componentDidUpdate(prevProps) {
        const { teamSlug, start, end, period, utc } = this.props;
        if (prevProps.start !== start ||
            prevProps.end !== end ||
            prevProps.period !== period ||
            prevProps.utc !== utc ||
            !(0, isEqual_1.default)(prevProps.teamSlug, teamSlug)) {
            this.remountComponent();
        }
    }
    getReleaseCount(projectId, dataset) {
        const { periodReleases, weekReleases } = this.state;
        const releasesPeriod = dataset === 'week' ? weekReleases === null || weekReleases === void 0 ? void 0 : weekReleases.last_week_totals : periodReleases === null || periodReleases === void 0 ? void 0 : periodReleases.project_avgs;
        const count = (releasesPeriod === null || releasesPeriod === void 0 ? void 0 : releasesPeriod[projectId])
            ? Math.ceil(releasesPeriod === null || releasesPeriod === void 0 ? void 0 : releasesPeriod[projectId])
            : 0;
        return count;
    }
    getTrend(projectId) {
        const periodCount = this.getReleaseCount(projectId, 'period');
        const weekCount = this.getReleaseCount(projectId, 'week');
        if (periodCount === null || weekCount === null) {
            return null;
        }
        return weekCount - periodCount;
    }
    renderLoading() {
        return this.renderBody();
    }
    renderReleaseCount(projectId, dataset) {
        const { loading } = this.state;
        if (loading) {
            return (<div>
          <placeholder_1.default width="80px" height="25px"/>
        </div>);
        }
        const count = this.getReleaseCount(Number(projectId), dataset);
        if (count === null) {
            return '\u2014';
        }
        return count;
    }
    renderTrend(projectId) {
        const { loading } = this.state;
        if (loading) {
            return (<div>
          <placeholder_1.default width="80px" height="25px"/>
        </div>);
        }
        const trend = this.getTrend(Number(projectId));
        if (trend === null) {
            return '\u2014';
        }
        return (<SubText color={trend >= 0 ? 'green300' : 'red300'}>
        {`${(0, round_1.default)(Math.abs(trend), 3)}`}
        <PaddedIconArrow direction={trend >= 0 ? 'up' : 'down'} size="xs"/>
      </SubText>);
    }
    renderBody() {
        var _a, _b;
        const { projects, period, theme, organization } = this.props;
        const { periodReleases } = this.state;
        const sortedProjects = projects
            .map(project => { var _a; return ({ project, trend: (_a = this.getTrend(Number(project.id))) !== null && _a !== void 0 ? _a : 0 }); })
            .sort((a, b) => Math.abs(b.trend) - Math.abs(a.trend));
        const groupedProjects = (0, utils_1.groupByTrend)(sortedProjects);
        const data = Object.entries((_a = periodReleases === null || periodReleases === void 0 ? void 0 : periodReleases.release_counts) !== null && _a !== void 0 ? _a : {}).map(([bucket, count]) => ({
            value: Math.ceil(count),
            name: new Date(bucket).getTime(),
        }));
        const seriesData = (0, utils_1.convertDaySeriesToWeeks)(data);
        const averageValues = Object.values((_b = periodReleases === null || periodReleases === void 0 ? void 0 : periodReleases.project_avgs) !== null && _b !== void 0 ? _b : {});
        const projectAvgSum = averageValues.reduce((total, currentData) => total + currentData, 0);
        const totalPeriodAverage = Math.ceil(projectAvgSum / averageValues.length);
        return (<div>
        <ChartWrapper>
          <barChart_1.default style={{ height: 190 }} isGroupedByDate useShortDate period="7d" legend={{ right: 3, top: 0 }} yAxis={{ minInterval: 1 }} xAxis={(0, utils_1.barAxisLabel)(seriesData.length)} series={[
                {
                    seriesName: (0, locale_1.t)('This Period'),
                    // @ts-expect-error silent missing from type
                    silent: true,
                    data: seriesData,
                    markLine: (0, markLine_1.default)({
                        silent: true,
                        lineStyle: { color: theme.gray200, type: 'dashed', width: 1 },
                        // @ts-expect-error yAxis type not correct
                        data: [{ yAxis: totalPeriodAverage }],
                        label: {
                            show: false,
                        },
                    }),
                },
            ]} tooltip={{
                formatter: seriesParams => {
                    // `seriesParams` can be an array or an object :/
                    const [series] = Array.isArray(seriesParams)
                        ? seriesParams
                        : [seriesParams];
                    const dateFormat = 'MMM D';
                    const startDate = (0, moment_1.default)(series.axisValue).format(dateFormat);
                    const endDate = (0, moment_1.default)(series.axisValue)
                        .add(7, 'days')
                        .format(dateFormat);
                    return [
                        '<div class="tooltip-series">',
                        `<div><span class="tooltip-label">${series.marker} <strong>${series.seriesName}</strong></span> ${series.data[1]}</div>`,
                        `<div><span class="tooltip-label"><strong>Last ${period} Average</strong></span> ${totalPeriodAverage}</div>`,
                        '</div>',
                        `<div class="tooltip-date">${startDate} - ${endDate}</div>`,
                        '<div class="tooltip-arrow"></div>',
                    ].join('');
                },
            }}/>
        </ChartWrapper>
        <StyledPanelTable isEmpty={projects.length === 0} headers={[
                (0, locale_1.t)('Project'),
                <RightAligned key="last">
              {(0, locale_1.tct)('Last [period] Average', { period })}
            </RightAligned>,
                <RightAligned key="curr">{(0, locale_1.t)('Last 7 Days')}</RightAligned>,
                <RightAligned key="diff">{(0, locale_1.t)('Difference')}</RightAligned>,
            ]}>
          {groupedProjects.map(({ project }) => (<react_1.Fragment key={project.id}>
              <ProjectBadgeContainer>
                <ProjectBadge avatarSize={18} project={project}/>
              </ProjectBadgeContainer>

              <ScoreWrapper>{this.renderReleaseCount(project.id, 'period')}</ScoreWrapper>
              <ScoreWrapper>
                <link_1.default to={{
                    pathname: `/organizations/${organization.slug}/releases/`,
                    query: { project: project.id, statsPeriod: '7d' },
                }}>
                  {this.renderReleaseCount(project.id, 'week')}
                </link_1.default>
              </ScoreWrapper>
              <ScoreWrapper>{this.renderTrend(project.id)}</ScoreWrapper>
            </react_1.Fragment>))}
        </StyledPanelTable>
      </div>);
    }
}
exports.default = (0, react_2.withTheme)(TeamReleases);
const ChartWrapper = (0, styled_1.default)('div') `
  padding: ${(0, space_1.default)(2)} ${(0, space_1.default)(2)} 0 ${(0, space_1.default)(2)};
  border-bottom: 1px solid ${p => p.theme.border};
`;
const StyledPanelTable = (0, styled_1.default)(panelTable_1.default) `
  grid-template-columns: 1fr 0.2fr 0.2fr 0.2fr;
  white-space: nowrap;
  margin-bottom: 0;
  border: 0;
  font-size: ${p => p.theme.fontSizeMedium};
  box-shadow: unset;

  & > div {
    padding: ${(0, space_1.default)(1)} ${(0, space_1.default)(2)};
  }
`;
const RightAligned = (0, styled_1.default)('span') `
  text-align: right;
`;
const ScoreWrapper = (0, styled_1.default)('div') `
  display: flex;
  align-items: center;
  justify-content: flex-end;
  text-align: right;
`;
const PaddedIconArrow = (0, styled_1.default)(icons_1.IconArrow) `
  margin: 0 ${(0, space_1.default)(0.5)};
`;
const SubText = (0, styled_1.default)('div') `
  color: ${p => p.theme[p.color]};
`;
const ProjectBadgeContainer = (0, styled_1.default)('div') `
  display: flex;
`;
const ProjectBadge = (0, styled_1.default)(idBadge_1.default) `
  flex-shrink: 0;
`;
//# sourceMappingURL=teamReleases.jsx.map