#Чернеги Вікторії   Б19_д/122Б
#Програма обчислює за даними користувача колір світлофора.

while True:
    while True:
        try:
            t = int(input('Time = '))
            break
        except ValueError:
            print('Only numbers')
    if 0<t<=60:
        if 0<t%6<=3:
            print('Green light')
        elif t%6 == 4:
               print('Yellow light')
        else:
               print('Red light')
    else:
         print('Wrong time. It must be in range from 0 to 60')

    answer = input('Restart? Yes - 1. No - other.')
    if answer == '1':
        continue
    else:
        break