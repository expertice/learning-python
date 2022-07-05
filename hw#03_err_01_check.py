# 1. Пользователь вводит число, если оно четное - выбрасываем исключение ValueError,
#     если оно меньше 0 - TypeError, если оно больше 10 - IndexError.
#     Обрабатываем ошибку, говорим пользователю, в чем его ошибка

def check_it(arg):
    try:
        if int(arg) < 0:
            raise TypeError(f'{arg} is less than zero')
        elif int(arg) > 10:
            raise IndexError(f'{arg} is larger than 10')
        elif int(arg) % 2 == 0:
            raise ValueError(f'{arg} is an even value')
        else:
            print("I have no condition for this value")
    except Exception as e:
        print('Value that you entered is not a figure ', e)


check_it(input('Enter a value: '))
