# download your FB birthday calendar from
# https://www.facebook.com/events/upcoming
#
# = Birthday link under "You can add your events to Microsoft Outlook, Google Calendar or Apple Calendar..."
#
# This gets you a link like: 
# http://facebook.com/ical/b.php?uid=123&key=XYZ
#
# using icalendar, found via:
# http://stackoverflow.com/questions/3408097/parsing-files-ics-icalendar-using-python

from collections import namedtuple
import sys

from icalendar import Calendar

DEFAULT_CAL = 'cal.ics'

Bday = namedtuple('Bday', 'name month day')


def get_birthdays(cal):
    with open(cal, 'rb') as g:
        gcal = Calendar.from_ical(g.read())
        for component in gcal.walk():
            if component.name == "VEVENT":
                name = component.get('SUMMARY')
                if not name:
                    continue
                name = name.replace("'s birthday", "")
                bday = component.get('DTSTART').dt
                yield Bday(name=name, month=bday.month, day=bday.day)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        cal = DEFAULT_CAL
    else:
        cal = sys.argv[1]

    for bday in get_birthdays(cal):
        print(bday)
