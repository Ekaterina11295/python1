#задача 1
def my_func (a, b):
     try:
         c = a / b
         return c
     except ZeroDivisionError:
         return "Делить на 0 нельзя!"

print (my_func(int(input("Введите 1ое значение: ")), int(input("Введите 2ое значение: "))))

#задача 2
def my_func (name, surname, birth_year, city, email, phone_number):
    print (name, surname, birth_year, city, email, phone_number)

my_func (name ='Ekaterina', surname = 'Nikitina', birth_year = '1995', city = 'Moscow', email = 'katya011295@inbox.ru', phone_number = '89035456596')


#задача 3
def my_func(x, y, z):
    arguments = [x, y, z]
    max_arguments = []
    m_1 = max(arguments)
    max_arguments.append(m_1)
    arguments.remove(m_1)
    m_2 = max(arguments)
    max_arguments.append(m_2)
    print(sum(max_arguments))

my_func(-1,-2,-5)

#задача 4

#x - действительное положительное, y - целое отрицаетельное
#1способ:
def my_func(x, y):
    return x ** y
print(my_func(2, -1))

#2способ:
def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result
print(my_func(2, -1))

#задача 6 

def int_func(a):
    print(a.title())

print(int_func(input('введите словa: ')))

#задача 5

def my_func(*args):
    print(sum(args))

print(my_func(1,3,5))