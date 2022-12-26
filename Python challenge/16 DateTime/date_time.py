import datetime
#print(dir(datetime))
# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__',
#  '__doc__', '__file__', '__loader__', '__name__', '__package__', 
#  '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 
#  'timedelta', 'timezone', 'tzinfo']



#######    we will focus on date, datetime, time and timedelta #########


from datetime import datetime
now = datetime.now()
#print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
#print('timestamp', timestamp)
#print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

t = now.strftime("%H:%M:%S")
#print("time:",t)

time_one = now.strftime("%B/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
#print("time one:", time_one)



###  String to Time Using strptime
'''
date_string = "5 December, 2019"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
'''

#### Using date from datetime

from datetime import date
d = date(2020, 1, 1)
#print(d)
#print('Current date:', d.today())    # 2019-12-05
# date object of today's date
today = date.today()
#print("Current year:", today.year)   # 2019
#print("Current month:", today.month) # 12
#print("Current day:", today.day)     # 5

### Time Objects to Represent Time

from datetime import time
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
#print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
#print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
#print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
#print("d =", d)


from datetime import timedelta
t1 = timedelta(days=10, hours=4,minutes=3, seconds=40)
t2 = timedelta(days=7, hours=4, minutes=33, seconds=30)
t3 = t1 - t2
#print("t3 =", t3)

### Difference Between Two Points in Time Using ###
# con date se pasan 3 argumentos
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
#print('Time left for new year: ', time_left_for_newyear)
# Time left for new year:  27 days, 0:00:00

# con datetime se pueden pasar  6 argumentos, minimo 3
t1 = datetime(year = 2019, month = 12, day = 5)
t2 = datetime(year = 2020, month = 1, day = 5)
diff = t2 - t1
#print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00



### Difference Between Two Points in Time Using timedelta ###

from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
#print("t3 =", t3) # t3=  86 days, 22:56:50

####   Exercises: Day 16 ####

# 1 - Get the current day, month, year, hour, minute and timestamp from datetime
'''
from datetime import datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
timestamp = now.timestamp()
print("el timestamp es: ",timestamp)
print(f'{day}/{month}/{year}{hour}')
'''

# 2 - Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

'''
from datetime import datetime
# current date 
now = datetime.now()
date2 = now.strftime("%H:%M:%S")
date3 = now.strftime("%m/%d/%Y")
# mm/dd/YY H:M:S format
print("current day:", date2, date3)
'''

# 3 - Today is 5 December, 2019. Change this time string to time.
'''

from date_time import datetime
str = "5 December, 2019"
str_changed = datetime.strptime(str,"%d %B, %Y")
print(str_changed)
'''

# 4 - Calculate the time difference between now and new year.

'''
today = date(year=2022, month=12, day=21)
new_year = date(year=2023, month=1, day=1)
time_left_for_newyear = new_year - today
print(time_left_for_newyear)
'''

# 5 - Calculate the time difference between 1 January 1970 and now.
'''
date_one = datetime(year=1970, month=1, day=1)
today = datetime(year=202, month=12, day=21)
now = datetime.now()
time_today= now - date_one
print(time_today) 
#19347 days, 13:51:26.426154
'''