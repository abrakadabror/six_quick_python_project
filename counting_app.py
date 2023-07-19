import time #biblioteka odpowiada za czas w pythonie sec/min dni, miesiace itp

def countdown(t): #definujemy nowa funkcje o nawie countdown z parametrem t = to ilosc sekund
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs) #nadajemy format timera
        print(timer, end='\r') #drukujemy nasz licznik i konczymy backshlas r
        time.sleep(1)
        t -= 1

    print('Timer completed')
t = input('Enter the time in seconds: ')

countdown(int(t))


# import pprint
# import pytz
# from datetime import datetime

# time_current = time.time()
# utc_time = time.gmtime(time_current)

# time_dict = {
#      'year': utc_time.tm_year,
#      'month': utc_time.tm_mon,
#      'day': utc_time.tm_mday,
#      'hour': utc_time.tm_hour,
#      'minutes': utc_time.tm_min,
#      'sec': utc_time.tm_sec,
#      'wday': utc_time.tm_wday,
#      'tm_yday': utc_time.tm_yday,
#      'tm_isdst': utc_time.tm_isdst

#  }
# pprint.pprint(time_dict)

# warsaw_timezone = pytz.timezone('Europe/Warsaw')
# dt = datetime.fromtimestamp(time_current, warsaw_timezone)

# print(dt)
