import datetime


def get_time():

    time_now = str(datetime.datetime.now().time())
    hours, minutes, seconds = time_now.split(":")
    total_seconds = (float(hours)*60*60)+(float(minutes)*60)+float(seconds)
    return total_seconds


start = get_time()
for n in range(1, 2000000):
    print(n)

end = get_time()
print(f"start-{start}")
print(f"end-{end}")
miliseconds_time_duration = (end-start)*1000
print(miliseconds_time_duration)
