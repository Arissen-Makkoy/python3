# .format(arg, arg1)
def byte_format():
    age = 18;
    name = 'Sasha';
    print('Age: {0} Name: {1}'.format(age, name))

# Expression 
def byte_expression():
    length = 5
    breadth = 4
    area = length * breadth
    print('Площадь равна: ', area)
    print('Периметр плоази равен: ', 2 * (length + breadth))

# if
def byte_if():
    number = 23;
    guess = int(input('Введите целое число: '))

    if guess == number:
        print('Поздравляю, вы угадали,') # Начало нового блока
        print('(хотя и не выиграли никакого приза!)') # Конец нового блока
    elif guess < number:
        print('Нет, загаданное число немного больше этого.') # Ещё один блок
        # Внутри блока вы можете выполнять всё, что угодно ...
    else:
        print('Нет, загаданное число немного меньше этого.')
        # чтобы попасть сюда, guess должно быть больше, чем number

# while
def byte_while():
    number = 23
    running = True
    
    while running:
        guess = int(input("Введите число: "))

        if number == guess:
            print('Поздравляю, вы угадали.')
            running = False # это останавливает цикл while
        elif number > guess:
            print('Ваше число меньше')
        else:
            print('Ваше число больше')
    else:
        print('Цикл While закончен')
        # Здесь можно выполнить что-то ещё
    print('Завершение')

# For
def byte_for():
    num = 10
    i = 1;
    for i in range(i, num):
        print(i)
    else:
        print('Цикл for закончился')

# Break
def byte_break():
    while True:
        s = input("Введите что-нибудь: ")
        if s == 'Выход':
            break
        print("Длина строки: ", len(s))
    print('Завершение')

# Continue
def byte_continue():
    while True:
        s = input('Введите что-нибудь: ')
        if s == 'Выход':
            break
        if len(s) < 3:
            print('Слишком мало')
            continue
        print('Введёная строка достаточной длины')

# Paramentr function(a, b)
def byte_param(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'равно', b)
    else:
        print(b, 'максимально')

# Default parametr function(a, b = 1)
def byte_default_param(message, times = 1):
    print(message * times)

# Key function()
def byte_key_param(a, b=5, c=10):
    print('a = ', a, 'b = ', b, 'c = ', c)

# Varags function(*a, **b)
def byte_varags_func(*numbers, **phonebook):
    for single_item in numbers:
        print('single_items', single_item)
    
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)
    # print(byte_varags_func(1, 2, 3, Jack=1123, John=2231, Igne=1150))

# Return
def byte_return(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны'
    else:
        return y

# doc
def byte_doc(x, y):
    '''
    Выводит максимальное двух чисел.
    
    Оба значения должны быть целыми числами.
    '''
    x = int(x) # конвертация в целое число, если возможно
    y = int(y)

    if x > y:
        print(x, 'Наибольшее')
    else:
        print(y, 'Наибольшее')
    print(byte_doc.__doc__) # Вызов документации


# nonlocal
def byte_func_local():
    x = 2
    print('x = ', x)

    def func_local():
        nonlocal x
        x = 5

    func_local()
    print('Локальная х переменная изменилась на', x)

# Работа с модулями
# module.byte_my_module()
# import module
# print(module.__version__)

def new_func():
    print(' ')
