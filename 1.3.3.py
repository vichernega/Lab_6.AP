#Чернеги Вікторії   Б19_д/122Б
#Програма за вказаним місяцем виводить сезоню

from enum import Enum
class month(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12
class season(Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4
while True:
    while True:
        try:
            s = month[input('month: ')]
            break
        except (KeyError, ValueError):
            print('Only letters')

    n = s.value
    if 0 < n < 3 or n == 12:
        print(f'{s.name} is {season(1).name}')
    elif 2 < n < 6:
        print(f'{s.name} is {season(2).name}')
    elif 5 < n < 9:
        print(f'{s.name} is {season(3).name}')
    elif 8 < n < 12:
        print(f'{s.name} is {season(4).name}')

    answer = input('Restart? Yes - 1. No - other.')
    if answer == '1':
        continue
    else:
        break