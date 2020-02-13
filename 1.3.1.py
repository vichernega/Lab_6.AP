#Чернеги Вікторії   Б19_д/122Б
#Програма обчислює попереній і наступний дні від дати, що вказує користувач. Високосні роки враховані.

while True:
    while True:
        try:
            d = int(input('Day = '))
            break
        except ValueError:
            print('Only numbers')
    while True:
        try:
            m = int(input('Month = '))
            break
        except ValueError:
            print('Only numbers')
    while True:
        try:
            y = int(input('Year = '))
            break
        except ValueError:
            print('Only numbers')

    if y % 4 == 0:
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            if d == 1 and m == 1:
                print(f'Last day is 31.12.{y - 1}; Next day is {d + 1}.{m}.{y}')
            elif d == 31 and m == 12:
                print(f'Last day is {d - 1}.{m}.{y}; Next day is 1.1.{y + 1}')
            elif d == 1 and m == 3:
                print(f'Last day is 29.2.{y}; Next day is {d + 1}.{m}.{y}')
            elif d == 1:
                print(f'Last day is 30.{m - 1}.{y}; Next day is {d + 1}.{m}.{y}')
            elif d == 31:
                print(f'Last day is 30.{m}.{y}; Next day is 1.{m + 1}.{y}')
            elif 1 < d < 31:
                print(f'Last day is {d - 1}.{m}.{y}; Next day is {d + 1}.{m}.{y}')
            else:
                print('Wrong date')

        elif m == 2:
            if d == 1:
                print(f'Last day is 31.1.{y}; Next day is 2.2.{y}')
            elif 1 < d < 29:
                print(f'Last day is {d - 1}.{m}.{y}; Next day is {d + 1}.{m}.{y}')
            elif d == 29:
                print(f'Last day is 28.2.{y}; Next day is 1.3.{y}')
            else:
                print('Wrong date')

        elif m == 4 or m == 6 or m == 9 or m == 11:
            if d == 1:
                print(f'Last day is 31.{m}.{y}; Next day is 2.{m}.{y}')
            elif 1 < d < 30:
                print(f'Last day is {d - 1}.{m}.{y}; Next day is {d + 1}.{m}.{y}')
            elif d == 30:
                print(f'Last day is 29.{m}.{y}; Next day is 1.{m}.{y}')
            else:
                print('Wrong date')

    else:
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            if d == 1 and m == 1:
                print(f'Last day is 31.12.{y - 1}; Next day is {d + 1}.{m}.{y}')
            elif d == 31 and m == 12:
                print(f'Last day is {d - 1}.{m}.{y}; Next day is 1.1.{y + 1}')
            elif d == 1 and m == 3:
                print(f'Last day is 28.2.{y}; Next day is {d + 1}.{m}.{y}')
            elif d == 1:
                print(f'Last day is 30.{m - 1}.{y}; Next day is {d + 1}.{m}.{y}')
            elif d == 31:
                print(f'Last day is 30.{m}.{y}; Next day is 1.{m + 1}.{y}')
            elif 1 < d < 31:
                print(f'Last day is {d - 1}.{m}.{y}; Next day is {d + 1}.{m}.{y}')
            else:
                print('Wrong date')

        elif m == 2:
            if d == 1:
                print(f'Last day is 31.1.{y}; Next day is 2.2.{y}')
            elif 1 < d < 28:
                print(f'Last day is {d - 1}.{m}.{y}; Next day is {d + 1}.{m}.{y}')
            elif d == 28:
                print(f'Last day is 27.2.{y}; Next day is 1.3.{y}')
            else:
                print('Wrong date')

        elif m == 4 or m == 6 or m == 9 or m == 11:
            if d == 1:
                print(f'Last day is 31.{m}.{y}; Next day is 2.{m}.{y}')
            elif 1 < d < 30:
                print(f'Last day is {d - 1}.{m}.{y}; Next day is {d + 1}.{m}.{y}')
            elif d == 30:
                print(f'Last day is 29.{m}.{y}; Next day is 1.{m}.{y}')
            else:
                print('Wrong date')
        else:
            print('Wrong date')


    answer = input('Restart? Yes - 1. No - other.')
    if answer == 1:
        continue
    else:
        break