$(document).ready(function() {

    $('#calendar').fullCalendar({
        events: 'http://www.google.com/calendar/feeds/en.usa%23holiday%40group.v.calendar.google.com/public/basic',
        header: {
            left: 'title',
            right: 'prev, next'
        },


    });



});


// Flags Leave,Holiday,Absent,Present,Weekend..
$(document).ready(function() {

    $("td.fc-day-tue  > div").append(" <b class='flag'>L</b>");
    $("td.fc-day-wed  > div").append(" <b class='flag'>P</b>");
    $("td.fc-day-sun  > div").append(" <b class='flag'>W</b>");
    $("td.fc-day-sat  > div").append(" <b class='flag'>W</b>");
    $("td.fc-day-mon  > div").append(" <b class='flag'>H</b>");
    $("td.fc-day-fri  > div").append(" <b class='flag'>A</b>");


});


document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        headerToolbar: {
            left: 'title',
            right: 'prev, next',

        },

    });

    calendar.render();

    calendar.on('dateClick', function(info) {
        console.log('clicked on ' + info.dateStr);
    });
});