# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"


def location(name, age, city):
    return name + age + "проживает в городе " + city


answer = location("Кирилл, ", "29 лет, ", "Мытищи.")

print(answer)


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def number(long):
    return max(long)


a = 9, 76, 34
b = number(a)

print(b)

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def func(longest_word):
    return max(longest_word)


my_list = "стол", "стул", "кровать", "тренажер"
result = func(my_list)

print(result)
