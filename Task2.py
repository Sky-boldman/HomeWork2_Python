# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


n = int(input("Введите число N:"))

factorial = 1
print(factorial, end=" ")
for i in range(2, n+1):
    factorial *= i
    print(factorial, end=' ')
print('Факториал числа', n, 'равняется', factorial)
