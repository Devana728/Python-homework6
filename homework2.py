#Напишите программу, которая принимает на вход число N и выдает
#  набор произведений чисел от 1 до N.
#*Пример:*
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] 
# (1, 1*2, 1*2*3, 1*2*3*4)
import math
num = int(input("Введите число: "))
li = [x for x in range(1,num+1)]
mass = list( map(lambda i : i* math.factorial(i-1), li))
print(f"Произведения чисел от 1 до {num}:  {mass}")