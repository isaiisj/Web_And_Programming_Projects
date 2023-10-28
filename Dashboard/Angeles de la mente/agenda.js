mobiscroll.setOptions({
    locale: mobiscroll.localeEs,
    theme: 'ios',
    themeVariant: 'light'
});

var timer;

var list = mobiscroll.eventcalendar('#demo-search-list', {
    view: {
        agenda: {
            type: 'year',
            size: 5
        }
    },
    showControls: false,
    onEventClick: function (args) {
        calendar.navigate(args.event.start);
        calendar.setSelectedEvents([args.event]);
        popup.close();
    }
});

var calendar = mobiscroll.eventcalendar('#demo-search-events', {
    clickToCreate: false,
    dragToCreate: false,
    dragToMove: false,
    dragToResize: false,
    selectMultipleEvents: true,
    view: {
        calendar: {
            labels: true
        }
    },
    renderHeader: function () {
        return '<div mbsc-calendar-nav></div>' +
            '<div class="md-seach-header-bar mbsc-flex-1-0">' +
            '<label><input id="md-search-demo-input" mbsc-input data-start-icon="material-search" data-input-style="box" placeholder="Search events"></input></label>' +
            '</div>' +
            '<div mbsc-calendar-prev></div>' +
            '<div mbsc-calendar-today></div>' +
            '<div mbsc-calendar-next></div>';
    },
    onPageLoading: function (args, inst) {
        var start = mobiscroll.formatDate('YYYY-MM-DD', args.viewStart);
        var end = mobiscroll.formatDate('YYYY-MM-DD', args.viewEnd);

        mobiscroll.util.http.getJson('https://trial.mobiscroll.com/searchevents/?start=' + start + '&end=' + end, function (data) {
            calendar.setEvents(data);
        }, 'jsonp');
    }
});

var searchInput = document.getElementById('md-search-demo-input');

var popup = mobiscroll.popup('#demo-search-popup', {
    display: 'anchored',
    showArrow: false,
    showOverlay: false,
    scrollLock: false,
    contentPadding: false,
    focusOnOpen: false,
    focusOnClose: false,
    focusElm: searchInput,
    anchor: searchInput
});

searchInput.addEventListener('input', function (ev) {
    var text = ev.target.value;
    clearTimeout(timer);
    timer = setTimeout(function () {
        if (text.length > 0) {
            mobiscroll.util.http.getJson('https://trial.mobiscroll.com/searchevents/?text=' + text, function (data) {
                list.setEvents(data);
                popup.open();
            }, 'jsonp');
        } else {
            popup.close();
        }
    }, 200);
});


searchInput.addEventListener('focus', function (ev) {
    if (ev.target.value.length > 0) {
        popup.open();
    }
});