# Функция GETCWD -> Модуль GETCWD -> Часть библиотеки OS
import os
from os import getcwd  # при вызове возвращает текущий рабочий каталог

where_am_I = getcwd()
print(where_am_I)

# Больше узнать об операционной системе -> SYS

import sys  # module sys

print(sys.platform)  # return platform name = win32
print(sys.version)  # return python version = 3.6.8

# OS environ -> SYSTEM ENVIRONMENT VARIABLES

print(os.environ)  # получение переменных окружения
print(os.getenv("HOME"))  # получение конкретного атрибута для переменной

# DATETIME

import datetime  # importing datetime module

print(datetime.date.today())  # return current date
print(datetime.date.today().day)  # return current day
print(datetime.date.today().month)  # return current month
print(datetime.date.today().year)  # return current year

print(datetime.date.isoformat(datetime.date.today()))  # return current date in string format

# module TIME

import time

print(time.strftime("%I:%M"))  # print current time in 12-h format <HOUR:MINUTE>
print(time.strftime("%A %p"))  # print current DAY name and period of the day (AM/PM)

# module HTML

import html

# функция escape - позволяет экранировать потенциально опасные угловые скобки
print(
    html.escape("This HTML fragment contains a <script>script</script> tag."))  # происходит экранирование опасных тегов
# функция unescape - позволяет вернуть документ в оригинальное представление
print(html.unescape("I &hearts; Python's &lt;standard library&gt;."))  # возвращает на место все что было экранировано