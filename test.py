import datetime

unix_timestamp = 1628588167  # Przykładowy czas wschodu słońca w formacie UNIX
utc_time = datetime.datetime.utcfromtimestamp(unix_timestamp)
local_time = utc_time.strftime('%Y-%m-%d %H:%M:%S')

print("Czas wschodu słońca (lokalny czas):", local_time)