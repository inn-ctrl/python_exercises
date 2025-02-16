import calendar

def print_calendar(year, month): 
    cal= calendar.month(year, month)

    return cal

year = int(input('input any year (e.g: 2025):')); 
month = int(input('input any month (1 - 12)')); 

print(print_calendar(year, month))