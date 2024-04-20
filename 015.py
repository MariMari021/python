#Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

usuario = int(input('Digite um número: '))

if usuario % 2 == 0:
    print(f'O número é par!')
else:
    print(f'O número é ímpar!')