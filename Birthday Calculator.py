from datetime import date

today = date.today()
print('Current day')

month = today.strftime("%m")
print("Month:", month)

day = today.strftime("%d")
print("Day:", day)

year = today.strftime("%Y")
print("Year:", year)

print('Birthday')

user_month = int(input('Month:'))
user_day = int(input('Day:'))
user_year = int(input('Year:'))

if user_month - int(month) == 0:
    if user_month - int(month) == 0:
        print('Happy Birthday!')

age = int(year) - int(user_year)
print('You are', age, 'years old.')
