#!python3
#date_compare.py is a quick script to calculate how many days fall between two dates

from dateutil.parser import parse


def date_entry():
    date1 = parse(input("Please enter the first date in format mm/dd/year:"))
    date2 = parse(input("Please enter the second date in format mm/dd/year:"))
    
    date1_date = date1.date()
    date2_date = date2.date()
    
    days = date_calc(date1_date, date2_date)
    return days

     
def date_calc(d1, d2):
    if d1 > d2:
        days = d1 - d2
    else:
        days = d2 - d1
    return days  


if __name__ == "__main__":
    days = date_entry()
    print("\n %s day(s) between these two dates." % (days.days))