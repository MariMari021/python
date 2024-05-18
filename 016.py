#Escreva um programa que peça ao usuário dois números e imprima se eles são iguais ou diferentes.

print('----- Saiba se os números são iguais ou não! -----')

try:
    valorUm = int(input('Digite um número: '))
    valorDois = int(input('Digite outro número: '))

    if valorUm == valorDois:
        print(f'Os valores são iguais!')
    else:
        print(f'Os valores são diferentes!')

except ValueError:
    print("Erro: Insira apenas valores numéricos inteiros.")