Object.defineProperty(exports, "__esModule", { value: true });
const tslib_1 = require("tslib");
const initializeOrg_1 = require("sentry-test/initializeOrg");
const reactTestingLibrary_1 = require("sentry-test/reactTestingLibrary");
const threadsV2_1 = (0, tslib_1.__importDefault)(require("app/components/events/interfaces/threadsV2"));
const types_1 = require("app/types");
const event_1 = require("app/types/event");
describe('ThreadsV2', function () {
    const { project, organization } = (0, initializeOrg_1.initializeOrg)();
    const org = Object.assign(Object.assign({}, organization), { features: ['native-stack-trace-v2'] });
    describe('non native platform', function () {
        describe('other platform', function () {
            const event = {
                id: '020eb33f6ce64ed6adc60f8993535816',
                groupID: '68',
                eventID: '020eb33f6ce64ed6adc60f8993535816',
                projectID: '2',
                size: 3481,
                entries: [
                    {
                        data: {
                            values: [
                                {
                                    type: 'ZeroDivisionError',
                                    value: 'divided by 0',
                                    mechanism: null,
                                    threadId: null,
                                    module: '',
                                    stacktrace: {
                                        frames: [
                                            {
                                                filename: 'puma (3.12.6) lib/puma/thread_pool.rb',
                                                absPath: 'puma (3.12.6) lib/puma/thread_pool.rb',
                                                module: null,
                                                package: null,
                                                platform: null,
                                                instructionAddr: null,
                                                symbolAddr: null,
                                                function: 'block in spawn_thread',
                                                rawFunction: null,
                                                symbol: null,
                                                context: [],
                                                lineNo: 135,
                                                colNo: null,
                                                inApp: false,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                            },
                                            {
                                                filename: 'puma (3.12.6) lib/puma/server.rb',
                                                absPath: 'puma (3.12.6) lib/puma/server.rb',
                                                module: null,
                                                package: null,
                                                platform: null,
                                                instructionAddr: null,
                                                symbolAddr: null,
                                                function: 'block in run',
                                                rawFunction: null,
                                                symbol: null,
                                                context: [],
                                                lineNo: 334,
                                                colNo: null,
                                                inApp: false,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                            },
                                            {
                                                filename: 'app/controllers/welcome_controller.rb',
                                                absPath: 'app/controllers/welcome_controller.rb',
                                                module: null,
                                                package: null,
                                                platform: null,
                                                instructionAddr: null,
                                                symbolAddr: null,
                                                function: 'index',
                                                rawFunction: null,
                                                symbol: null,
                                                context: [
                                                    [2, '  before_action :set_sentry_context\n'],
                                                    [3, '\n'],
                                                    [4, '  def index\n'],
                                                    [5, '    1 / 0\n'],
                                                    [6, '  end\n'],
                                                    [7, '\n'],
                                                    [8, '  def view_error\n'],
                                                ],
                                                lineNo: 5,
                                                colNo: null,
                                                inApp: true,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                                minGroupingLevel: 1,
                                            },
                                            {
                                                filename: 'app/controllers/welcome_controller.rb',
                                                absPath: 'app/controllers/welcome_controller.rb',
                                                module: null,
                                                package: null,
                                                platform: null,
                                                instructionAddr: null,
                                                symbolAddr: null,
                                                function: '/',
                                                rawFunction: null,
                                                symbol: null,
                                                context: [
                                                    [2, '  before_action :set_sentry_context\n'],
                                                    [3, '\n'],
                                                    [4, '  def index\n'],
                                                    [5, '    1 / 0\n'],
                                                    [6, '  end\n'],
                                                    [7, '\n'],
                                                    [8, '  def view_error\n'],
                                                ],
                                                lineNo: 5,
                                                colNo: null,
                                                inApp: true,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                                minGroupingLevel: 0,
                                            },
                                        ],
                                        framesOmitted: null,
                                        registers: null,
                                        hasSystemFrames: true,
                                    },
                                    rawStacktrace: null,
                                    frames: null,
                                },
                            ],
                            hasSystemFrames: true,
                            excOmitted: null,
                        },
                        type: event_1.EntryType.EXCEPTION,
                    },
                    {
                        data: {
                            values: [
                                {
                                    id: 13920,
                                    current: true,
                                    crashed: true,
                                    name: 'puma 002',
                                    stacktrace: null,
                                    rawStacktrace: null,
                                },
                            ],
                        },
                        type: event_1.EntryType.THREADS,
                    },
                ],
                dist: null,
                message: '',
                title: 'ZeroDivisionError: divided by 0',
                location: 'app/controllers/welcome_controller.rb',
                user: null,
                contexts: {},
                sdk: null,
                context: {},
                packages: {},
                type: types_1.EventOrGroupType.ERROR,
                metadata: {
                    display_title_with_tree_label: false,
                    filename: 'app/controllers/welcome_controller.rb',
                    finest_tree_label: [
                        { filebase: 'welcome_controller.rb', function: '/' },
                        { filebase: 'welcome_controller.rb', function: 'index' },
                    ],
                    function: '/',
                    type: 'ZeroDivisionError',
                    value: 'divided by 0',
                },
                tags: [{ key: 'level', value: 'error' }],
                platform: 'other',
                dateReceived: '2021-10-28T12:28:22.318469Z',
                errors: [],
                crashFile: null,
                culprit: 'app/controllers/welcome_controller.rb in /',
                dateCreated: '2021-10-28T12:28:22.318469Z',
                fingerprints: ['58f1f47bea5239ea25397888dc9253d1'],
                groupingConfig: {
                    enhancements: 'eJybzDRxY25-UmZOqpWRgZGhroGJroHRBABbUQb_',
                    id: 'mobile:2021-02-12',
                },
                release: null,
                userReport: null,
                sdkUpdates: [],
                nextEventID: null,
                previousEventID: null,
            };
            const props = {
                type: event_1.EntryType.THREADS,
                data: event.entries[1].data,
                event,
                groupingCurrentLevel: 0,
                hasHierarchicalGrouping: true,
                projectId: project.id,
            };
            it('renders', function () {
                const { container } = (0, reactTestingLibrary_1.mountWithTheme)(<threadsV2_1.default {...props}/>, {
                    organization: org,
                });
                // Title
                expect(reactTestingLibrary_1.screen.getByRole('heading', { name: 'Stack Trace' })).toBeInTheDocument();
                // Actions
                expect(reactTestingLibrary_1.screen.getByRole('checkbox', { name: 'Raw' })).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByRole('checkbox', { name: 'Raw' })).not.toBeChecked();
                expect(reactTestingLibrary_1.screen.getByRole('button', { name: 'Options 1 Active' })).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByRole('button', { name: 'Sort By Recent first' })).toBeInTheDocument();
                // Stack Trace
                expect(reactTestingLibrary_1.screen.getByRole('heading', { name: 'ZeroDivisionError' })).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('divided by 0')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByTestId('stack-trace')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.queryAllByTestId('stack-trace-frame')).toHaveLength(4);
                expect(container).toSnapshot();
            });
            it('toggle raw button', function () {
                (0, reactTestingLibrary_1.mountWithTheme)(<threadsV2_1.default {...props}/>, { organization: org });
                expect(reactTestingLibrary_1.screen.getByRole('checkbox', { name: 'Raw' })).not.toBeChecked();
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByRole('checkbox', { name: 'Raw' }));
                expect(reactTestingLibrary_1.screen.getByRole('checkbox', { name: 'Raw' })).toBeChecked();
                // Actions must not be rendered
                expect(reactTestingLibrary_1.screen.queryByRole('button', { name: 'Options 1 Active' })).not.toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.queryByRole('button', { name: 'Sort By Recent first' })).not.toBeInTheDocument();
                // Raw content is displayed
                expect(reactTestingLibrary_1.screen.queryByRole('list', { name: 'Stack trace' })).not.toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByTestId('raw-stack-trace')).toBeInTheDocument();
            });
            it('toggle sort by', function () {
                (0, reactTestingLibrary_1.mountWithTheme)(<threadsV2_1.default {...props}/>, { organization: org });
                expect((0, reactTestingLibrary_1.within)(reactTestingLibrary_1.screen.queryAllByTestId('stack-trace-frame')[0]).getByText('app/controllers/welcome_controller.rb')).toBeInTheDocument();
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByRole('button', { name: 'Sort By Recent first' }));
                expect(reactTestingLibrary_1.screen.queryAllByLabelText('Sort option')).toHaveLength(2);
                expect(reactTestingLibrary_1.screen.queryAllByLabelText('Sort option')[0]).toHaveTextContent('Recent first');
                expect(reactTestingLibrary_1.screen.queryAllByLabelText('Sort option')[1]).toHaveTextContent('Recent last');
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByText('Recent last'));
                expect(reactTestingLibrary_1.screen.getByRole('button', { name: 'Sort By Recent last' })).toBeInTheDocument();
                expect((0, reactTestingLibrary_1.within)(reactTestingLibrary_1.screen.queryAllByTestId('stack-trace-frame')[0]).getByText('puma (3.12.6) lib/puma/thread_pool.rb')).toBeInTheDocument();
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByRole('button', { name: 'Sort By Recent last' }));
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByText('Recent first'));
                expect(reactTestingLibrary_1.screen.getByRole('button', { name: 'Sort By Recent first' })).toBeInTheDocument();
            });
            it('check options', function () {
                return (0, tslib_1.__awaiter)(this, void 0, void 0, function* () {
                    (0, reactTestingLibrary_1.mountWithTheme)(<threadsV2_1.default {...props}/>, { organization: org });
                    expect(reactTestingLibrary_1.screen.getByRole('button', { name: 'Options 1 Active' })).toBeInTheDocument();
                    reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByRole('button', { name: 'Options 1 Active' }));
                    expect(reactTestingLibrary_1.screen.queryAllByLabelText('Display option')).toHaveLength(2);
                    const displayOption0 = reactTestingLibrary_1.screen.queryAllByLabelText('Display option')[0];
                    expect(displayOption0).toHaveTextContent('Minified');
                    expect((0, reactTestingLibrary_1.within)(displayOption0).getByRole('checkbox')).not.toBeChecked();
                    expect((0, reactTestingLibrary_1.within)(displayOption0).getByRole('checkbox')).toHaveAttribute('aria-disabled', 'true');
                    // hover over the Minified option
                    reactTestingLibrary_1.userEvent.hover((0, reactTestingLibrary_1.within)(displayOption0).getByText('Minified'));
                    expect(yield reactTestingLibrary_1.screen.findByText('Minified version not available')).toBeInTheDocument();
                    const displayOption1 = reactTestingLibrary_1.screen.queryAllByLabelText('Display option')[1];
                    expect(displayOption1).toHaveTextContent('Full Stack Trace');
                    expect((0, reactTestingLibrary_1.within)(displayOption1).getByRole('checkbox')).toBeChecked();
                    expect((0, reactTestingLibrary_1.within)(displayOption1).getByRole('checkbox')).toHaveAttribute('aria-disabled', 'false');
                    expect(reactTestingLibrary_1.screen.getByTestId('stack-trace')).toBeInTheDocument();
                    expect(reactTestingLibrary_1.screen.queryAllByTestId('stack-trace-frame')).toHaveLength(4);
                    // Uncheck Full Stack Trace
                    reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.queryAllByLabelText('Display option')[1]);
                    expect((0, reactTestingLibrary_1.within)(reactTestingLibrary_1.screen.queryAllByLabelText('Display option')[1]).getByRole('checkbox')).not.toBeChecked();
                    // Display less frames
                    expect(reactTestingLibrary_1.screen.queryAllByTestId('stack-trace-frame')).toHaveLength(3);
                });
            });
        });
    });
    describe('native platform', function () {
        describe('cocoa', function () {
            const event = {
                id: 'bfe4379d82934b2b91d70b1167bcae8d',
                groupID: '24',
                eventID: 'bfe4379d82934b2b91d70b1167bcae8d',
                projectID: '2',
                size: 89101,
                entries: [
                    {
                        data: {
                            values: [
                                {
                                    stacktrace: {
                                        frames: [
                                            {
                                                filename: null,
                                                absPath: null,
                                                module: null,
                                                package: '/private/var/containers/Bundle/Application/575F9D39-D486-4728-B035-84923A0BE206/sentry-ios-cocoapods.app/Frameworks/Sentry.framework/Sentry',
                                                platform: null,
                                                instructionAddr: '0x1000adb08',
                                                symbolAddr: '0x1000ad5c4',
                                                function: '__44-[SentryBreadcrumbTracker swizzleSendAction]_block_invoke_2',
                                                rawFunction: null,
                                                symbol: null,
                                                context: [],
                                                lineNo: null,
                                                colNo: null,
                                                inApp: false,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                            },
                                            {
                                                filename: null,
                                                absPath: null,
                                                module: null,
                                                package: '/System/Library/Frameworks/UIKit.framework/UIKit',
                                                platform: null,
                                                instructionAddr: '0x197885c54',
                                                symbolAddr: '0x197885bf4',
                                                function: '<redacted>',
                                                rawFunction: null,
                                                symbol: null,
                                                context: [],
                                                lineNo: null,
                                                colNo: null,
                                                inApp: false,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                            },
                                            {
                                                filename: null,
                                                absPath: null,
                                                module: null,
                                                package: '/System/Library/Frameworks/UIKit.framework/UIKit',
                                                platform: null,
                                                instructionAddr: '0x197885c54',
                                                symbolAddr: '0x197885bf4',
                                                function: '<redacted>',
                                                rawFunction: null,
                                                symbol: null,
                                                context: [],
                                                lineNo: null,
                                                colNo: null,
                                                inApp: false,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                            },
                                            {
                                                filename: null,
                                                absPath: null,
                                                module: null,
                                                package: '/var/containers/Bundle/Application/575F9D39-D486-4728-B035-84923A0BE206/sentry-ios-cocoapods.app/sentry-ios-cocoapods',
                                                platform: null,
                                                instructionAddr: '0x10008c5ac',
                                                symbolAddr: '0x10008c500',
                                                function: 'ViewController.causeCrash',
                                                rawFunction: 'ViewController.causeCrash(Any) -> ()',
                                                symbol: null,
                                                context: [],
                                                lineNo: null,
                                                colNo: null,
                                                inApp: true,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                            },
                                            {
                                                filename: null,
                                                absPath: null,
                                                module: null,
                                                package: '/private/var/containers/Bundle/Application/575F9D39-D486-4728-B035-84923A0BE206/sentry-ios-cocoapods.app/Frameworks/Sentry.framework/Sentry',
                                                platform: null,
                                                instructionAddr: '0x1000b0bfc',
                                                symbolAddr: '0x1000b0be4',
                                                function: '-[SentryClient crash]',
                                                rawFunction: null,
                                                symbol: null,
                                                context: [],
                                                lineNo: null,
                                                colNo: null,
                                                inApp: false,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                            },
                                        ],
                                        framesOmitted: null,
                                        hasSystemFrames: true,
                                        registers: {
                                            cpsr: '0x60000000',
                                            fp: '0x16fd79870',
                                            lr: '0x10008c5ac',
                                            pc: '0x1000b0bfc',
                                            sp: '0x16fd79810',
                                            x0: '0x1700eee80',
                                            x1: '0x10008e49c',
                                            x10: '0x1b7886ff0',
                                            x11: '0x59160100591680',
                                            x12: '0x0',
                                            x13: '0x591600',
                                            x14: '0x591700',
                                            x15: '0x5916c0',
                                            x16: '0x591601',
                                            x17: '0x1000b0be4',
                                            x18: '0x0',
                                            x19: '0x1740eb200',
                                            x2: '0x0',
                                            x20: '0x10fd08db0',
                                            x21: '0x10008e4de',
                                            x22: '0x10fe0a470',
                                            x23: '0x10fe0a470',
                                            x24: '0x174008ba0',
                                            x25: '0x0',
                                            x26: '0x19838eb61',
                                            x27: '0x1',
                                            x28: '0x170046c60',
                                            x29: '0x16fd79870',
                                            x3: '0x1740eb200',
                                            x4: '0x1740eb200',
                                            x5: '0x1740eb200',
                                            x6: '0x0',
                                            x7: '0x2',
                                            x8: '0x0',
                                            x9: '0x1b7886fec',
                                        },
                                    },
                                    threadId: 0,
                                    module: null,
                                    mechanism: null,
                                    rawStacktrace: null,
                                    value: 'Attempted to dereference null pointer.\nOriginated at or in a subcall of ViewController.causeCrash(Any) -> ()',
                                    type: 'EXC_BAD_ACCESS',
                                },
                            ],
                            hasSystemFrames: true,
                            excOmitted: null,
                        },
                        type: event_1.EntryType.EXCEPTION,
                    },
                    {
                        data: {
                            values: [
                                {
                                    id: 0,
                                    current: false,
                                    crashed: true,
                                    name: null,
                                    stacktrace: {
                                        frames: [
                                            {
                                                filename: null,
                                                absPath: null,
                                                module: null,
                                                package: '/System/Library/Frameworks/UIKit.framework/UIKit',
                                                platform: null,
                                                instructionAddr: '0x197885c54',
                                                symbolAddr: '0x197885bf4',
                                                function: '<redacted>',
                                                rawFunction: null,
                                                symbol: null,
                                                context: [],
                                                lineNo: null,
                                                colNo: null,
                                                inApp: false,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                            },
                                            {
                                                filename: null,
                                                absPath: null,
                                                module: null,
                                                package: '/System/Library/Frameworks/UIKit.framework/UIKit',
                                                platform: null,
                                                instructionAddr: '0x197885c54',
                                                symbolAddr: '0x197885bf4',
                                                function: '<redacted>',
                                                rawFunction: null,
                                                symbol: null,
                                                context: [],
                                                lineNo: null,
                                                colNo: null,
                                                inApp: false,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                            },
                                            {
                                                filename: null,
                                                absPath: null,
                                                module: null,
                                                package: '/var/containers/Bundle/Application/575F9D39-D486-4728-B035-84923A0BE206/sentry-ios-cocoapods.app/sentry-ios-cocoapods',
                                                platform: null,
                                                instructionAddr: '0x10008c630',
                                                symbolAddr: '0x10008c5e8',
                                                function: 'ViewController.causeCrash',
                                                rawFunction: '@objc ViewController.causeCrash(Any) -> ()',
                                                symbol: null,
                                                context: [],
                                                lineNo: null,
                                                colNo: null,
                                                inApp: true,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                            },
                                            {
                                                filename: null,
                                                absPath: null,
                                                module: null,
                                                package: '/var/containers/Bundle/Application/575F9D39-D486-4728-B035-84923A0BE206/sentry-ios-cocoapods.app/sentry-ios-cocoapods',
                                                platform: null,
                                                instructionAddr: '0x10008c5ac',
                                                symbolAddr: '0x10008c500',
                                                function: 'ViewController.causeCrash',
                                                rawFunction: 'ViewController.causeCrash(Any) -> ()',
                                                symbol: null,
                                                context: [],
                                                lineNo: null,
                                                colNo: null,
                                                inApp: true,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                            },
                                            {
                                                filename: null,
                                                absPath: null,
                                                module: null,
                                                package: '/private/var/containers/Bundle/Application/575F9D39-D486-4728-B035-84923A0BE206/sentry-ios-cocoapods.app/Frameworks/Sentry.framework/Sentry',
                                                platform: null,
                                                instructionAddr: '0x1000b0bfc',
                                                symbolAddr: '0x1000b0be4',
                                                function: '-[SentryClient crash]',
                                                rawFunction: null,
                                                symbol: null,
                                                context: [],
                                                lineNo: null,
                                                colNo: null,
                                                inApp: false,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                            },
                                        ],
                                        framesOmitted: null,
                                        registers: {
                                            cpsr: '0x60000000',
                                            fp: '0x16fd79870',
                                            lr: '0x10008c5ac',
                                            pc: '0x1000b0bfc',
                                            sp: '0x16fd79810',
                                            x0: '0x1700eee80',
                                            x1: '0x10008e49c',
                                            x10: '0x1b7886ff0',
                                            x11: '0x59160100591680',
                                            x12: '0x0',
                                            x13: '0x591600',
                                            x14: '0x591700',
                                            x15: '0x5916c0',
                                            x16: '0x591601',
                                            x17: '0x1000b0be4',
                                            x18: '0x0',
                                            x19: '0x1740eb200',
                                            x2: '0x0',
                                            x20: '0x10fd08db0',
                                            x21: '0x10008e4de',
                                            x22: '0x10fe0a470',
                                            x23: '0x10fe0a470',
                                            x24: '0x174008ba0',
                                            x25: '0x0',
                                            x26: '0x19838eb61',
                                            x27: '0x1',
                                            x28: '0x170046c60',
                                            x29: '0x16fd79870',
                                            x3: '0x1740eb200',
                                            x4: '0x1740eb200',
                                            x5: '0x1740eb200',
                                            x6: '0x0',
                                            x7: '0x2',
                                            x8: '0x0',
                                            x9: '0x1b7886fec',
                                        },
                                        hasSystemFrames: true,
                                    },
                                    rawStacktrace: null,
                                },
                                {
                                    id: 1,
                                    current: false,
                                    crashed: false,
                                    name: null,
                                    stacktrace: {
                                        frames: [
                                            {
                                                filename: null,
                                                absPath: null,
                                                module: null,
                                                package: '/usr/lib/system/libsystem_pthread.dylib',
                                                platform: null,
                                                instructionAddr: '0x1907df1a4',
                                                symbolAddr: '0x1907decb8',
                                                function: '_pthread_wqthread',
                                                rawFunction: null,
                                                symbol: null,
                                                context: [],
                                                lineNo: null,
                                                colNo: null,
                                                inApp: false,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                            },
                                            {
                                                filename: null,
                                                absPath: null,
                                                module: null,
                                                package: '/usr/lib/system/libsystem_kernel.dylib',
                                                platform: null,
                                                instructionAddr: '0x190719a88',
                                                symbolAddr: '0x190719a80',
                                                function: '__workq_kernreturn',
                                                rawFunction: null,
                                                symbol: null,
                                                context: [],
                                                lineNo: null,
                                                colNo: null,
                                                inApp: false,
                                                trust: null,
                                                errors: null,
                                                vars: null,
                                            },
                                        ],
                                        framesOmitted: null,
                                        registers: {
                                            cpsr: '0x0',
                                            fp: '0x16dfcaf70',
                                            lr: '0x1907df1a4',
                                            pc: '0x190719a88',
                                            sp: '0x16dfcaef0',
                                            x0: '0x4',
                                            x1: '0x0',
                                            x10: '0x1',
                                            x11: '0x0',
                                            x12: '0x30000400000d03',
                                            x13: '0x0',
                                            x14: '0x1740e9edc',
                                            x15: '0xfffffff100000000',
                                            x16: '0x170',
                                            x17: '0x191619c10',
                                            x18: '0x0',
                                            x19: '0x16dfcb000',
                                            x2: '0x0',
                                            x20: '0x19',
                                            x21: '0x270019',
                                            x22: '0x0',
                                            x23: '0xd03',
                                            x24: '0x1b788d000',
                                            x25: '0x1b788d000',
                                            x26: '0x0',
                                            x27: '0x80000000',
                                            x28: '0x800010ff',
                                            x29: '0x16dfcaf70',
                                            x3: '0x0',
                                            x4: '0x80010ff',
                                            x5: '0x0',
                                            x6: '0x0',
                                            x7: '0x0',
                                            x8: '0x2',
                                            x9: '0x17409b4ec',
                                        },
                                        hasSystemFrames: false,
                                    },
                                    rawStacktrace: null,
                                },
                            ],
                        },
                        type: event_1.EntryType.THREADS,
                    },
                    {
                        data: {
                            images: [
                                {
                                    code_file: '/var/containers/Bundle/Application/575F9D39-D486-4728-B035-84923A0BE206/sentry-ios-cocoapods.app/sentry-ios-cocoapods',
                                    debug_id: '6b77ffb6-5aba-3b5f-9171-434f9660f738',
                                    image_addr: '0x100084000',
                                    image_size: 49152,
                                    image_vmaddr: '0x100000000',
                                    type: 'macho',
                                },
                                {
                                    code_file: '/System/Library/Frameworks/UIKit.framework/UIKit',
                                    debug_id: '314063bd-f85f-321d-88d6-e24a0de464a2',
                                    image_addr: '0x197841000',
                                    image_size: 14315520,
                                    image_vmaddr: '0x187769000',
                                    type: 'macho',
                                },
                                {
                                    code_file: '/private/var/containers/Bundle/Application/575F9D39-D486-4728-B035-84923A0BE206/sentry-ios-cocoapods.app/Frameworks/Sentry.framework/Sentry',
                                    debug_id: '141a9203-b953-3cd6-b9fd-7ba60191a36d',
                                    image_addr: '0x1000a4000',
                                    image_size: 163840,
                                    image_vmaddr: '0x0',
                                    type: 'macho',
                                },
                                {
                                    code_file: '/private/var/containers/Bundle/Application/575F9D39-D486-4728-B035-84923A0BE206/sentry-ios-cocoapods.app/Frameworks/Sentry.framework/Sentry',
                                    debug_id: '141a9203-b953-3cd6-b9fd-7ba60191a36d',
                                    image_addr: '0x1000a4000',
                                    image_size: 163840,
                                    image_vmaddr: '0x0',
                                    type: 'macho',
                                },
                            ],
                        },
                        type: event_1.EntryType.DEBUGMETA,
                    },
                ],
                dist: '1',
                message: '',
                title: 'ViewController.causeCrash | main',
                location: null,
                user: {
                    id: '1234',
                    email: 'hello@sentry.io',
                    username: null,
                    ip_address: '172.18.0.1',
                    name: null,
                    data: null,
                },
                type: types_1.EventOrGroupType.ERROR,
                metadata: {
                    display_title_with_tree_label: true,
                    finest_tree_label: [
                        {
                            function: 'ViewController.causeCrash',
                        },
                        {
                            function: 'main',
                        },
                    ],
                    function: 'ViewController.causeCrash',
                    value: 'Attempted to dereference null pointer.\nOriginated at or in a subcall of ViewController.causeCrash(Any) -> ()',
                },
                platform: 'cocoa',
                dateReceived: '2021-11-02T07:33:38.831104Z',
                errors: [
                    {
                        type: 'invalid_data',
                        message: 'Discarded invalid value',
                        data: {
                            name: 'threads.values.9.stacktrace.frames',
                            reason: 'expected a non-empty value',
                        },
                    },
                ],
                crashFile: null,
                culprit: '',
                dateCreated: '2021-11-02T07:33:38.831104Z',
                fingerprints: ['852f6cf1ed76d284b95e7d62275088ca'],
                groupingConfig: {
                    enhancements: 'eJybzDRxY25-UmZOqpWRgZGhroGJroHRBABbUQb_',
                    id: 'mobile:2021-02-12',
                },
                tags: [],
                contexts: {},
                userReport: null,
                sdkUpdates: [],
                nextEventID: null,
                previousEventID: null,
            };
            const props = {
                type: event_1.EntryType.THREADS,
                data: event.entries[1].data,
                event,
                groupingCurrentLevel: 0,
                hasHierarchicalGrouping: true,
                projectId: project.id,
            };
            it('renders', function () {
                const { container } = (0, reactTestingLibrary_1.mountWithTheme)(<threadsV2_1.default {...props}/>, { organization: org });
                // Title
                expect(reactTestingLibrary_1.screen.getByTestId('thread-selector')).toBeInTheDocument();
                // Actions
                expect(reactTestingLibrary_1.screen.getByRole('checkbox', { name: 'Raw' })).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByRole('checkbox', { name: 'Raw' })).not.toBeChecked();
                expect(reactTestingLibrary_1.screen.getByRole('button', { name: 'Options 1 Active' })).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByRole('button', { name: 'Sort By Recent first' })).toBeInTheDocument();
                // Stack Trace
                expect(reactTestingLibrary_1.screen.getByRole('heading', { name: 'EXC_BAD_ACCESS' })).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByText('Attempted to dereference null pointer. Originated at or in a subcall of ViewController.causeCrash(Any) -> ()')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByTestId('stack-trace')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.queryAllByTestId('stack-trace-frame')).toHaveLength(4);
                expect(container).toSnapshot();
            });
            it('toggle raw button', function () {
                (0, reactTestingLibrary_1.mountWithTheme)(<threadsV2_1.default {...props}/>, { organization: org });
                expect(reactTestingLibrary_1.screen.getByRole('checkbox', { name: 'Raw' })).not.toBeChecked();
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByRole('checkbox', { name: 'Raw' }));
                expect(reactTestingLibrary_1.screen.getByRole('checkbox', { name: 'Raw' })).toBeChecked();
                // Actions must not be rendered
                expect(reactTestingLibrary_1.screen.queryByRole('button', { name: 'Options 1 Active' })).not.toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.queryByRole('button', { name: 'Sort By Recent first' })).not.toBeInTheDocument();
                // Raw content is displayed
                expect(reactTestingLibrary_1.screen.queryByTestId('stack-trace')).not.toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.getByTestId('raw-stack-trace')).toBeInTheDocument();
            });
            it('toggle sort by', function () {
                (0, reactTestingLibrary_1.mountWithTheme)(<threadsV2_1.default {...props}/>, { organization: org });
                expect((0, reactTestingLibrary_1.within)(reactTestingLibrary_1.screen.queryAllByTestId('stack-trace-frame')[0]).getByText('-[SentryClient crash]')).toBeInTheDocument();
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByRole('button', { name: 'Sort By Recent first' }));
                expect(reactTestingLibrary_1.screen.queryAllByLabelText('Sort option')).toHaveLength(2);
                expect(reactTestingLibrary_1.screen.queryAllByLabelText('Sort option')[0]).toHaveTextContent('Recent first');
                expect(reactTestingLibrary_1.screen.queryAllByLabelText('Sort option')[1]).toHaveTextContent('Recent last');
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByText('Recent last'));
                expect(reactTestingLibrary_1.screen.getByRole('button', { name: 'Sort By Recent last' })).toBeInTheDocument();
                expect((0, reactTestingLibrary_1.within)(reactTestingLibrary_1.screen.queryAllByTestId('stack-trace-frame')[0]).getByText('__44-[SentryBreadcrumbTracker swizzleSendAction]_block_invoke_2')).toBeInTheDocument();
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByRole('button', { name: 'Sort By Recent last' }));
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByText('Recent first'));
                expect(reactTestingLibrary_1.screen.getByRole('button', { name: 'Sort By Recent first' })).toBeInTheDocument();
            });
            it('check options', function () {
                (0, reactTestingLibrary_1.mountWithTheme)(<threadsV2_1.default {...props}/>, { organization: org });
                expect(reactTestingLibrary_1.screen.getByRole('button', { name: 'Options 1 Active' })).toBeInTheDocument();
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.getByRole('button', { name: 'Options 1 Active' }));
                expect(reactTestingLibrary_1.screen.queryAllByLabelText('Display option')).toHaveLength(5);
                const displayOption0 = reactTestingLibrary_1.screen.queryAllByLabelText('Display option')[0];
                expect(displayOption0).toHaveTextContent('Unsymbolicated');
                expect((0, reactTestingLibrary_1.within)(displayOption0).getByRole('checkbox')).not.toBeChecked();
                expect((0, reactTestingLibrary_1.within)(displayOption0).getByRole('checkbox')).toHaveAttribute('aria-disabled', 'true');
                const displayOption1 = reactTestingLibrary_1.screen.queryAllByLabelText('Display option')[1];
                expect(displayOption1).toHaveTextContent('Absolute Addresses');
                expect((0, reactTestingLibrary_1.within)(displayOption1).getByRole('checkbox')).not.toBeChecked();
                expect((0, reactTestingLibrary_1.within)(displayOption1).getByRole('checkbox')).toHaveAttribute('aria-disabled', 'false');
                const displayOption2 = reactTestingLibrary_1.screen.queryAllByLabelText('Display option')[2];
                expect(displayOption2).toHaveTextContent('Absolute File Paths');
                expect((0, reactTestingLibrary_1.within)(displayOption2).getByRole('checkbox')).not.toBeChecked();
                expect((0, reactTestingLibrary_1.within)(displayOption2).getByRole('checkbox')).toHaveAttribute('aria-disabled', 'true');
                const displayOption3 = reactTestingLibrary_1.screen.queryAllByLabelText('Display option')[3];
                expect(displayOption3).toHaveTextContent('Verbose Function Names');
                expect((0, reactTestingLibrary_1.within)(displayOption3).getByRole('checkbox')).not.toBeChecked();
                expect((0, reactTestingLibrary_1.within)(displayOption3).getByRole('checkbox')).toHaveAttribute('aria-disabled', 'false');
                const displayOption4 = reactTestingLibrary_1.screen.queryAllByLabelText('Display option')[4];
                expect(displayOption4).toHaveTextContent('Full Stack Trace');
                expect((0, reactTestingLibrary_1.within)(displayOption4).getByRole('checkbox')).toBeChecked();
                expect((0, reactTestingLibrary_1.within)(displayOption4).getByRole('checkbox')).toHaveAttribute('aria-disabled', 'false');
                expect(reactTestingLibrary_1.screen.getByTestId('stack-trace')).toBeInTheDocument();
                expect(reactTestingLibrary_1.screen.queryAllByTestId('stack-trace-frame')).toHaveLength(4);
                // Check Verbose Function Names
                expect((0, reactTestingLibrary_1.within)(reactTestingLibrary_1.screen.queryAllByTestId('stack-trace-frame')[1]).getByText('ViewController.causeCrash')).toBeInTheDocument();
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.queryAllByLabelText('Display option')[3]);
                expect((0, reactTestingLibrary_1.within)(displayOption3).getByRole('checkbox')).toBeChecked();
                expect((0, reactTestingLibrary_1.within)(reactTestingLibrary_1.screen.queryAllByTestId('stack-trace-frame')[1]).getByText('ViewController.causeCrash(Any) -> ()')).toBeInTheDocument();
                // Check Absolute Path Names
                expect((0, reactTestingLibrary_1.within)(reactTestingLibrary_1.screen.queryAllByTestId('stack-trace-frame')[1]).getByText('+0x085ac')).toBeInTheDocument();
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.queryAllByLabelText('Display option')[1]);
                expect((0, reactTestingLibrary_1.within)(reactTestingLibrary_1.screen.queryAllByLabelText('Display option')[1]).getByRole('checkbox')).toBeChecked();
                expect((0, reactTestingLibrary_1.within)(reactTestingLibrary_1.screen.queryAllByTestId('stack-trace-frame')[1]).getByText('0x10008c5ac')).toBeInTheDocument();
                // Uncheck Full Stack Trace
                reactTestingLibrary_1.userEvent.click(reactTestingLibrary_1.screen.queryAllByLabelText('Display option')[4]);
                expect((0, reactTestingLibrary_1.within)(reactTestingLibrary_1.screen.queryAllByLabelText('Display option')[4]).getByRole('checkbox')).not.toBeChecked();
                // Display less frames
                expect(reactTestingLibrary_1.screen.queryAllByTestId('stack-trace-frame')).toHaveLength(3);
            });
        });
    });
});
//# sourceMappingURL=threadsV2.spec.jsx.map