hello = "Hello World"
name = "Maxim"
lastname = "<Bortnik"
age = 16

print(hello)
print(name)
print(lastname)
print(age)

print(type(hello))
print(type(name))
print(type(lastname))
print(type(age))

count_int = 0 #лічильники
count_str = 0
count_bool = 0
count_set = 0
count_list = 0
count_tuple = 0
count_float = 0
lst_notnull = []
max_value = -1
types_count = {str, int, bool, set, list, tuple, float}#список зміних
lst_count_types = [count_set, count_float, count_tuple, count_list, count_bool, count_str, count_int]#список лічильників
lst_name_type = ['set', 'float', 'tuple', 'list', 'bool', str, int]#список назв
lst = [name, lastname, age]
for item in lst: #цикл що рахує  кількість типів
    if type(item) == int:
        lst_count_types[-1] += 1
    elif type(item) == str:
        lst_count_types[-2] += 1

for item in lst_count_types:
    if item != 0:#цикл кий перевіряє чи не є значення нульовим
        lst_notnull.append(item) #це метод списку, який додає новий елемент у кінець списку.
    if len(lst_notnull) == 0: #перевіряє чи є список порожній
        print('Good')
    else:
        if item == max_value:
            print('Not')
            break #якщо значення item дорівнює макс.значення то виведе not

        elif item > max_value:
            max_value = item # код виконує перевірку і, якщо вона проходить, оновлює значення змінної max_value

inn = lst_count_types.index(max_value)#в цю заганяємо індекс макс. значення

print(lst_name_type[inn])#Виводить значення елемента з індексом або ключем inn із колекції lst_name_type

for item in lst:
    if type(item) != lst_name_type[inn]:
        lst.remove(item)#прибирає тип який найменше зустрічається в списку

# if count_str==count_int:
#     print("good")
# if count_str>count_int:
#     remove: type(int) from lst:
#if else = якщо або
#for break = початок кінець циклу