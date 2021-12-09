$(document).ready(function() {

    $('#calendar').fullCalendar({
      header: {
        left: 'prev,next today',
        center: 'title',
        right: 'month,agendaWeek,agendaDay'
      },
      defaultDate: '2019-11-29',
      navLinks: true, // can click day/week names to navigate views
      selectable: true,
      selectHelper: true,
      select: function(start, end) {
        var title = prompt('Titre de l\'événement:');
        var eventData;
        if (title) {
          eventData = {
            title: title,
            start: start,
            end: end
          };
          $('#calendar').fullCalendar('renderEvent', eventData, true); // stick? = true
        }
        $('#calendar').fullCalendar('unselect');
      },
      editable: true,
      eventLimit: true, // allow "more" link when too many events
      events: [
        {
          title: 'Formation',
          start: '2019-11-26'
        },
        {
          title: 'Présentation LiSa',
          start: '2019-11-25',
          end: '2018-03-10'
        },
        {
          id: 999,
          title: 'Présentation LiSa',
          start: '2019-11-22T16:00:00'
        },
        {
          id: 999,
          title: 'Présentation LiSa',
          start: '2019-11-29T16:00:00'
        },
        {
          title: 'Conférence',
          start: '2019-11-10',
          end: '2019-11-12'
        },
        {
          title: 'Meeting',
          start: '2019-11-12T10:30:00',
          end: '2019-11-12T12:30:00'
        },
        {
          title: 'Resto',
          start: '2019-11-12T12:00:00'
        },
        {
          title: 'Meeting',
          start: '2019-11-12T14:30:00'
        },
        {
          title: 'Happy Hour',
          start: '2019-11-12T17:30:00'
        },
        {
          title: 'Dîner',
          start: '2019-11-12T20:00:00'
        },
        {
          title: 'Anniversaire',
          start: '2019-11-13T07:00:00'
        },
        {
          title: 'Google Map',
          url: 'http://google.com/',
          start: '2019-11-28'
        }
      ]
    });

  });