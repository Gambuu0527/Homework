# string replace to datetime

import datetime as dt

d = dt.date(2024, 12, 15)
type(d)
dt.date.today()

mydate = '2024/12/15'
dt.datetime.strptime(mydate,'%Y/%m/%d')

# timedelta

date = dt.date(2025, 12, 15)
New_date = date + dt.timedelta(days=7)
print(New_date)

# strptime

dt.datetime.strptime("December 22, 2024" ,"%B %d, %Y")