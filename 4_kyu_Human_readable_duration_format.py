def format_duration(seconds):
    one_minute = 60
    one_hour = 60 * 60
    one_day = 24 * 60 * 60
    one_year = 365 * 24 * 60 * 60
    minutes = 0
    hours = 0
    days = 0
    years = 0
    res_str = ''
    arr = []
    if seconds == 0 or '':
        return 'now'
    while True:
        if seconds >= one_year:
            years = int(seconds // one_year)
            seconds = seconds - years * one_year
            txt_years = 'years' if years > 1 else 'year'
            arr.append("{} {}".format(years, txt_years))
        elif seconds >= one_day:
            days = int(seconds // one_day)
            seconds = seconds - days * one_day
            txt_days = 'days' if days > 1 else 'day'
            arr.append("{} {}".format(days, txt_days))
        elif seconds >= one_hour:
            hours = int(seconds // one_hour)
            seconds = seconds - hours * one_hour
            txt_hours = 'hours' if hours > 1 else 'hour'
            arr.append("{} {}".format(hours, txt_hours))
        elif seconds >= one_minute:
            minutes = int(seconds // one_minute)
            seconds = seconds-minutes*one_minute
            txt_minutes = 'minutes' if minutes > 1 else 'minute'
            arr.append("{} {}".format(minutes, txt_minutes))
        else:
            if seconds == 0:
                break
            txt_seconds = 'seconds' if seconds > 1 else 'second'
            arr.append("{} {}".format(seconds, txt_seconds))
            break
    if len(arr) == 1:
        return arr[0]
    else:
        for i in arr:
            # print(i)
            # print(arr[-1])
            if i == arr[-1]:
                res_str += " and {}".format(i)
            elif i == arr[0]:
                res_str += "{}".format(i)
            elif i is not None:
                res_str += ", {}".format(i)

    return res_str
  
format_duration(3662)
# * For seconds = 62, your function should return 
#     "1 minute and 2 seconds"
# * For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"
