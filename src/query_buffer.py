from time import sleep, strftime
from datetime import datetime, timedelta


while True:
    # get the date and time for now
    now = datetime.now()

    # get the current day at midnight
    today = now.replace(hour=0, minute=0, second=0, microsecond=0)

    # get now plus 10 seconds
    today_plus_delta = today + timedelta(seconds=10)

    # get the seconds from now until Tuesday at midnight
    seconds_to_new_query = (today_plus_delta - now).total_seconds()

    print(seconds_to_new_query)
