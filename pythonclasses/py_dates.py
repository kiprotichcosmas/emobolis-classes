from datetime import date, datetime, timedelta

today = date.today()
dt = datetime.now()
print(today)
print(dt)

formatted_date = today.strftime("%a, %d %B %Y ")  # Thurs, 25 Nov 2018  10:53PM
print(formatted_date)

ten_days_ago = today - timedelta(days=10)  # Getting pastime\
print(ten_days_ago)


# "2012-09-01" How to convert a date string to date
# "1999-01-31" "2005-11-13" find how many days are in between the two dates

