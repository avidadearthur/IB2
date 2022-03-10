from datetime import datetime, timedelta

today_plus_delta = datetime.now()
now = datetime.now()
seconds_to_new_query = 0

while True:
    # get the date and time for now
    if seconds_to_new_query == 0:
        now = datetime.now()
        # get now plus 10 seconds
        today_plus_delta = now + timedelta(seconds=10)

    # get the seconds from now until Tuesday at midnight
    seconds_to_new_query = (today_plus_delta - datetime.now()).total_seconds()

    print(seconds_to_new_query)
