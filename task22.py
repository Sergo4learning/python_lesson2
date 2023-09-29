# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

first_len=int(input("Введите количество элементов первого множества:"))
second_len=int(input("Введите количество элементов второго множества:"))
first_list=[""]*first_len
second_list=[""]*second_len
res_list=[]
for i in range(first_len):
    first_list[i]=input("Введите "+str(i+1)+" элемент первого множества:")
for i in range(second_len):
    second_list[i]=input("Введите "+str(i+1)+" элемент второго множества:")
if first_len>second_len:
    for i in range(first_len):
        if first_list[i] in second_list and first_list[i] not in res_list:
           res_list.append(first_list[i])
else: 
    for i in range(first_len):
        if second_list[i] in first_list and second_list[i] not in res_list:
           res_list.append(second_list[i])
for i in range(len(res_list)):
    for j in range(len(res_list)-1):
        if res_list[j]>res_list[j+1]:
            temp=res_list[j]
            res_list[j]=res_list[j+1]
            res_list[j+1]=temp
for i in range(len(res_list)):
    print(res_list[i])
    