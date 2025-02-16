from datetime import datetime as dt

start_date = dt(2023, 2, 2); 
current_date = dt.now()

n_days = (current_date - start_date).days
print(f'Number of days are: {n_days} days')