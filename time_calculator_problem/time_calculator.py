# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

"""
  - EL TIEMPO SIEMPRE SE MANEJA EN 12 HORAS, AM O PM
  - SE DEBE SUMAR EL TIEMPO Y DETERMINAR SI NOS ENCONTRAMOS EN HORA PM O AM
  - SI EL RESULTADO DE LA SUMA DE HORAS PASA DE UN DIA AL OTRO, DEBO PONER, NEXT DAY
  - SI SON MAS DE UN DIA, DEBO PONER CUANTOS
  - SI EL TERCER PARAMETRO ES INTRODUCIDO, DEBO CAMBIAR LOS DIAS, ES DECIR SI PASA DE MARTES, DEBO DEVOLVER MIERCOLES Y CONSECUTIVOS
  - LOS MINUTOS SIEMPRE SERAN MENOS DE 60 PERO LAS HORAS PUEDEN SER CUALQUIER NUMERO

  add_time("3:00 PM", "25:10")

  # Returns: 6:10 PM

"""

def add_time(star_time, duration_time, day = ''):


  # estableciendo variables fijas

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

  # calculo de horas y minutos

    hrs= start_h + duration_h
    mins = start_m + duration_m

    if period == 'PM':
        hrs += 12

    total_h, total_m = (hrs + 0, mins) if mins < 60 else (hrs + 1, mins - 60)

  # estableciendo nuevo formato

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

        for k,v in days.items():
            if v == final_d:
                final_d = k

        if count_day == 0:
            return f'{final_date} {final_d}'

        if count_day == 1:
            return f'{final_date} {final_d} (next day)'

        return f'{final_date} {final_d} ({count_day} days later)'

test = add_time("11:43 PM", "24:20", "tueSday")

print(test)
