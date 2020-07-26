export const state = {
  calendarView: 'day',
  selectedDate: '2020-07-01',
  locale: 'en-us',
  maxDays: 1,
  bordered: false,
  fiveDayWorkWeek: false,
  firstDayMonday: false,
  shortMonthLabel: false,
  showDayOfYearLabel: false,
  shortWeekdayLabel: false,
  shortIntervalLabel: false,
  hour24Format: false,
  hideHeader: false,
  noScroll: false,
  showMonthLabel: true,
  showWorkWeeks: false,
  noDefaultHeaderBtn: false,
  noDefaultHeaderText: false,
  intervalRange: {
    min: 0,
    max: 24
  },
  intervalRangeStep: 1,
  intervalHeight: 60,
  resourceHeight: 60,
  resourceWidth: 100,
  dayHeight: 100,
  enableTheme: false,
  theme: {
    name: 'default'
  }
}

export const getters = {
  calendarView: state => state.calendarView,
  selectedDate: state => state.selectedDate,
  locale: state => state.locale,
  maxDays: state => state.maxDays,
  bordered: state => state.bordered,
  fiveDayWorkWeek: state => state.fiveDayWorkWeek,
  firstDayMonday: state => state.firstDayMonday,
  shortMonthLabel: state => state.shortMonthLabel,
  showDayOfYearLabel: state => state.showDayOfYearLabel,
  shortWeekdayLabel: state => state.shortWeekdayLabel,
  shortIntervalLabel: state => state.shortIntervalLabel,
  hour24Format: state => state.hour24Format,
  hideHeader: state => state.hideHeader,
  noScroll: state => state.noScroll,
  showMonthLabel: state => state.showMonthLabel,
  showWorkWeeks: state => state.showWorkWeeks,
  noDefaultHeaderBtn: state => state.noDefaultHeaderBtn,
  noDefaultHeaderText: state => state.noDefaultHeaderText,
  intervalRange: state => state.intervalRange,
  intervalRangeStep: state => state.intervalRangeStep,
  intervalHeight: state => state.intervalHeight,
  resourceHeight: state => state.resourceHeight,
  resourceWidth: state => state.resourceWidth,
  dayHeight: state => state.dayHeight,
  enableTheme: state => state.enableTheme,
  theme: state => state.theme
}

export const mutations = {
  calendarView (state, view) {
    state.calendarView = view
  },
  selectedDate (state, date) {
    state.selectedDate = date
  },
  locale (state, locale) {
    state.locale = locale
  },
  maxDays (state, days) {
    state.maxDays = parseInt(days, 10)
  },
  bordered (state, b) {
    state.bordered = b
  },
  fiveDayWorkWeek (state, b) {
    state.fiveDayWorkWeek = b
  },
  firstDayMonday (state, b) {
    state.firstDayMonday = b
  },
  shortMonthLabel (state, b) {
    state.shortMonthLabel = b
  },
  showDayOfYearLabel (state, b) {
    state.showDayOfYearLabel = b
  },
  shortWeekdayLabel (state, b) {
    state.shortWeekdayLabel = b
  },
  shortIntervalLabel (state, b) {
    state.shortIntervalLabel = b
  },
  hour24Format (state, b) {
    state.hour24Format = b
  },
  hideHeader (state, b) {
    state.hideHeader = b
  },
  noScroll (state, b) {
    state.noScroll = b
  },
  showMonthLabel (state, b) {
    state.showMonthLabel = b
  },
  showWorkWeeks (state, b) {
    state.showWorkWeeks = b
  },
  noDefaultHeaderBtn (state, b) {
    state.noDefaultHeaderBtn = b
  },
  noDefaultHeaderText (state, b) {
    state.noDefaultHeaderText = b
  },
  intervalRange (state, r) {
    state.intervalRange = r
  },
  intervalRangeStep (state, step) {
    state.intervalRangeStep = step
  },
  intervalHeight (state, height) {
    state.intervalHeight = height
  },
  resourceHeight (state, height) {
    state.resourceHeight = height
  },
  resourceWidth (state, width) {
    state.resourceWidth = width
  },
  dayHeight (state, height) {
    state.dayHeight = height
  },
  enableTheme (state, b) {
    state.enableTheme = b
  },
  theme (state, theme) {
    state.theme = {
      ...theme
    }
  }
}
