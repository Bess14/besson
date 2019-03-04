# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.


name = ['Алексей', 'Василий', 'Степан', 'Александр', 'Виктор']
salary = [200000, 65000, 300000, 350000, 700000]
salary_list = list(zip(name, salary))


with open("salary.txt", 'w', encoding='UTF-8') as file_write:
    for salary_long in salary_list:
        file_write.write('{} - {}\n'.format(salary_long[0], salary_long[1]))


with open("salary.txt", 'r', encoding='UTF-8') as file_read:
    read_file = file_read.read()
    strings_from_file = read_file.split('\n')
    salary_length = []
    for salary_from_file in strings_from_file:
        if salary_from_file == '':
            continue
        salary_length.append(salary_from_file.split(' - '))

    for salary_line in salary_length:
        salary_line[0] = str(salary_line[0]).upper()
        salary_number = int(salary_line[1])
        if salary_number > 500000:
            salary_length.remove(salary_line)
            continue
        salary_number = salary_number - int((salary_number / 100) * 13)
        salary_line[1] = salary_number
    print(salary_length)
