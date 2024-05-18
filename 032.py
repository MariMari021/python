#Escreva um programa que imprima todos os números pares entre dois números
# fornecidos pelo usuário.

print('----- Saiba todos os números pares entre dois números -----')

try:
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))

    for i in range(num1, num2):
        if i % 2 == 0:
            print(i)
except ValueError:
    print('Digite apenas números.')