# Вам потрібно реалізувати корисну функцію для виведення списку колег, яких потрібно привітати з днем народження на тижні.
#
# У вас є список словників users, кожен словник у ньому обов'язково має ключі name та birthday. Така структура представляє
# модель списку користувачів з їх іменами та днями народження. name — це рядок з ім'ям користувача, а birthday —
# це datetime об'єкт, в якому записаний день народження.
#
# Ваше завдання написати функцію get_birthdays_per_week, яка отримує на вхід список users і виводить у консоль
# (за допомогою print) список користувачів, яких потрібно привітати по днях.
#
# Умови приймання
# get_birthdays_per_week виводить іменинників у форматі:
# Monday: Bill, Jill
# Friday: Kim, Jan
#
# Користувачів, у яких день народження був на вихідних, потрібно привітати в понеділок.
# Для тестування зручно створити тестовий список users та заповнити його самостійно.
# Функція виводить користувачів з днями народження на тиждень вперед від поточного дня.
# Тиждень починається з понеділка.

from datetime import datetime, timedelta, date
from collections import defaultdict


users = [{'name':'Nataliia', 'birthday':'1977-08-02'},
         {'name':'Mykola', 'birthday':'1975-07-28'},
         {'name':'Olga', 'birthday':'1966-07-26'},
         {'name':'Anna', 'birthday':'1977-03-21'},
         {'name':'Ivan', 'birthday':'1993-07-31'},
         {'name':'Xenya', 'birthday':'2005-07-29'},
         {'name':'Svitlana', 'birthday':'2000-07-30'},
         {'name':'Mona', 'birthday':'1977-02-28'},
         {'name':'Sonya', 'birthday':'2000-01-01'},
         {'name':'Kira', 'birthday':'1979-01-06'},
         {'name':'Taras', 'birthday':'1999-01-03'},
         {'name':'Alex', 'birthday':'2002-01-04'}
         ]

def get_birthdays_per_week(users: list) -> None:
    date_celebrate = defaultdict(list)

    date_today = date.today()
    date_delta = timedelta(days=6)
    date_end = date_today + date_delta

    for user in users:
        user['birthday'] = datetime.strptime(user['birthday'], '%Y-%m-%d').date()  # переводимо дату народженя в datetime

        # Враховуємо перехід року
        if date_end.month == 1 and date_end.day <= 7 and user['birthday'].month == 1 and user['birthday'].day <= date_end.day:
            date_birthday = user['birthday'].replace(year=date_end.year)
        else:
            date_birthday = user['birthday'].replace(year=date_today.year)

        # Рядкове представлення поточного дня народження
        birthday_str = date_birthday.strftime('%A %d %B %Y').split(' ')

        # Вихідні переносимо на понеділок
        if birthday_str[0] == 'Sunday':
            delta_weekend = timedelta(days=1)
        elif birthday_str[0] == 'Saturday':
            delta_weekend = timedelta(days=2)
        else:
            delta_weekend = timedelta(days=0)
        date_birthday_new = date_birthday + delta_weekend
        date_celebrate_str = date_birthday_new.strftime('%A %d %B %Y').split(' ')

        if date_birthday_new >= date_today and date_birthday_new <= date_end:
            if date_celebrate_str[0] == 'Monday':
                date_celebrate['Monday'].append(user['name'])
            elif date_celebrate_str[0] == 'Tuesday':
                date_celebrate['Tuesday'].append(user['name'])
            elif date_celebrate_str[0] == 'Wednesday':
                date_celebrate['Wednesday'].append(user['name'])
            elif date_celebrate_str[0] == 'Thursday':
                date_celebrate['Thursday'].append(user['name'])
            elif date_celebrate_str[0] == 'Friday':
                date_celebrate['Friday'].append(user['name'])

    if 'Monday' in date_celebrate:
        print(f"Monday: {','.join(date_celebrate.get('Monday'))}")
    if 'Tuesday' in date_celebrate:
        print(f"Tuesday: {','.join(date_celebrate.get('Tuesday'))}")
    if 'Wednesday' in date_celebrate:
        print(f"Wednesday: {','.join(date_celebrate.get('Wednesday'))}")
    if 'Thursday' in date_celebrate:
        print(f"Thursday: {','.join(date_celebrate.get('Thursday'))}")
    if 'Friday' in date_celebrate:
        print(f"Friday: {','.join(date_celebrate.get('Friday'))}")

get_birthdays_per_week(users)