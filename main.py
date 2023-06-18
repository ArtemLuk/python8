'''
with open('test.txt', 'r', encoding='utf-8') as file:
    # text = file.read()
    # for letter in text:
    #     print(letter)

    # while True:
    #     line = file.readline()
    #     if not line:
    #         break
    #     print(line[:-1])

    text = file.read().splitlines()
    print(text)with open('test.txt', 'r', encoding='utf-8') as file:
    # text = file.read()
    # for letter in text:
    #     print(letter)

    # while True:
    #     line = file.readline()
    #     if not line:
    #         break
    #     print(line[:-1])

    text = file.read().splitlines()
    print(text)
'''

'''with open('result.txt', 'w', encoding='utf-8') as file:
    some_list = ['привет', 'пока', 'как дела']
    for word in some_list:
        file.write(word + '\n')
        
with open('result.txt', 'a', encoding='utf-8') as file:
    some_list = ['привет', 'пока', 'как дела']
    for word in some_list:
        file.write(word + '\n')
'''

# Дан файл с несколькими строчками, пользователь вводит в консоль символ, нужно найти количество
# повторов этого символа во всем файле.

'''
with open("test.txt", "w", encoding="utf-8") as file:# в файл можно писать только строки
     some_list = ["привет","пока"]
     for word in some_list:
         file.write(word + "\n")

k = str(input ("Введите символ: "))
with open("test.txt", "r", encoding="utf-8") as file:
    text = file.read().splitlines()
    some_list2 = text
    count=0
    for i in range(len(some_list2)):
        for letter in some_list2[i]:
            if k == letter:
                count = count+1


    print (count)
'''

# Дан файл следующего формата: 
# Фамилия ученика: список оценок через запятую
# Сальников: 5, 5, 2, 3, 5, 5
# Нужно записать в новый файл фамилию ученика и его средний балл через :
# Сальников: 3.5

'''
with open('list.txt', 'r', encoding='utf-8') as input_file, open('2output.txt', 'w', encoding='utf-8') as output_file:
    for line in input_file:
        surname, grades = line[:-1].split(':')
        grades = list(map(int, grades.split(',')))
        average_grade = sum(grades) / len(grades)
        output_file.write(f'{surname}: {average_grade:.1f}\n')
'''

# Дан файл, нужно полностью скопировать его в другой файл

'''
 with open('result.txt', 'r', encoding='utf-8') as file:
    text = file.read().splitlines()
with open('test_1.txt', 'a', encoding='utf-8') as file:
    some_list = text
    for word in some_list:
        file.write(word + '\n')
'''

# Задача 38: Создать телефонный справочник возможностью добавления записей и чтения. Пользователь также может ввести 
# фамилию, тогда программа должны вывести на экран все записи с этой фамилий. Также пользователь может добавлять 
# новых людей в справочник в режиме экспорт.

a = int(input('Введите действие, которое хотите выполнить: 1 - поиск, 2 - добaвление, 3 -вывод справочника: '))
if a == 1:
    with open('baza.txt', 'r', encoding='utf-8') as file:
        print('search: ')
        surname = input('Введите фамилию для поиска: ')
        for line in file:
            if surname in line:
                print(line)
elif a==2:
    with open('baza.txt', 'a', encoding='utf-8') as file:
        print('add')
        surname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        tel = input('Введите телефон: ')
        new_line = surname + ' ' + name + ' ' + tel
        file.writelines(f'\n{new_line}')
elif a==3:
    with open('baza.txt', 'r', encoding='utf-8') as file:
        list = file.read()
        print(list)
else:
    print('Ошибка. До свидания.')