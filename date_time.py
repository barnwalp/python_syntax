from datetime import date, timedelta

# print today's date in YYYY-MM-DD format
print(date.today())
my_bdy = date(date.today().year, 6, 24)
print(my_bdy)

# get day of today
print(date.today().day)

# subtract or add from a date using timedelta

previous_day = date.today() - timedelta(2)
print(previous_day)
