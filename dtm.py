from datetime import datetime, date, timedelta
import locale
locale.setlocale(locale.LC_TIME, "ru_RU")

dt_now = datetime.now()
print('Сегодня:', dt_now.strftime('%d %B %Y'))
delta_yesterday = timedelta(days=1)
dt_yesterday = dt_now - delta_yesterday
print('Вчера было:', dt_yesterday.strftime('%d %B %Y'))
delta_month = timedelta(days=30)
dt_month = dt_now - delta_month
print('Месяц назад было:', dt_month.strftime('%d %m %Y, %A').title())

dt_srting = "01/01/17 12:10:03.23456"
date_str = datetime.strptime(dt_srting, '%d/%m/%y %H:%M:%S.%f')
print(date_str)

"""
dt_now = datetime.now()
#print(dt_now)

dt2 = datetime(2018, 1, 20, 19, 00, 34)
#print(dt2)

delta = dt_now - dt2
#print(delta)

dt3 = dt2 + delta
#print(dt3)

dt = datetime(2001, 1, 1)
#print(dt)
delta = timedelta(days=1)
#print(delta)
ddt = dt - delta
print(ddt.strftime('%H:%M, %d %B %Y, %A').title())
ddtt = dt + delta
print(ddtt.strftime('%d %B %Y %H:%M').upper())

dt_str = '12/23/2012'
date_dt_str = datetime.strptime(dt_str, '%m/%d/%Y').strftime('%d %B %Y')
print(date_dt_str)
"""