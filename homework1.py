#Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих 
# на нечётной позиции.
from random import randint


mass = list(map(int,input("введите числа через пробел =>").split()))
print (mass)
print(f'cумма элементов списка на нечетных позициях: {sum(mass[i] for i in range(len(mass)) if i%2!=0)}')
