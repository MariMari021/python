#Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

print('----- Saiba se o número é ímpar ou par -----')

try:
    usuario = int(input('Digite um número: '))

    if usuario % 2 == 0:
        print(f'O número é par!')
    else:
        print(f'O número é ímpar!')

except ValueError:
    print("Erro: Insira apenas valores numéricos inteiros.")