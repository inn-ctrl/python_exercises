from datetime import datetime

start_date = datetime(2025, 1, 1)
current_date = datetime.now()

days_difference = (current_date - start_date).days

print(f'the difference of days is {days_difference} days')