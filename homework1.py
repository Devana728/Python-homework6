#Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих 
# на нечётной позиции.
from random import randint
mass = []
N = int(input("Введите число N: "))
mass = []

for i in range(N):
    mass.append(randint(0, N))
print(mass)
sum=0
for  i  in range(1, N, 2) :   
    sum += mass [i]
print(f'cумма элементов списка на нечетных позициях: {sum}')
