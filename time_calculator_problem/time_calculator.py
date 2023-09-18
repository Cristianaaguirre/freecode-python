def add_time(star_time, duration_time, day=''):
    # setting variables

    chunks = [i.split(':') for i in (star_time[:-3], duration_time)]

    start_h, start_m, duration_h, duration_m = [int(i) for i in (chunks[0] + chunks[1])]
    period = star_time[-2:]

    days = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    # calculating hours and minutes

    hrs = start_h + duration_h
    mins = start_m + duration_m

    if period == 'PM':
        hrs += 12

    total_h, total_m = (hrs + 0, mins) if mins < 60 else (hrs + 1, mins - 60)

    # setting the base format

    count_day = total_h // 24

    final_h = (total_h % 24) % 12 or 12

    final_m = str(total_m) if total_m > 9 else '0' + str(total_m)

    final_p = 'AM' if total_h % 24 <= 11 else 'PM'

    final_date = f'{final_h}:{final_m} {final_p}'

    if not day:

        if count_day == 0:
            return final_date

        if count_day == 1:
            return f'{final_date} (next day)'

        return f'{final_date} ({count_day} days later)'

    else:

        final_d = (days[day.lower().capitalize()] + count_day) % 7

        for k, v in days.items():
            if v == final_d:
                final_d = k

        if count_day == 0:
            return f'{final_date} {final_d}'

        if count_day == 1:
            return f'{final_date} {final_d} (next day)'

        return f'{final_date} {final_d} ({count_day} days later)'


print(add_time("11:43 PM", "24:20", "tueSday"))
