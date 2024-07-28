### Dates #

from datetime import datetime

def print_date(now):
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)
    print(now.timestamp())


now = datetime.now()

print_date(now)

## Creo fecha ##
year_2025 = datetime(2025, 1, 1, 18, 51, 12)

print_date(year_2025)

from datetime import time

current_time = time()

current_time

