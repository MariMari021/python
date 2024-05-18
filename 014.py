#Escreva um programa que peça ao usuário um número e
# imprima se é positivo ou negativo.

print('----- Saiba se o número é positivo ou negativo -----')

try:
    user = int(input('Digite um número: '))

    if user > 0:
        print(f'O número é positivo!')
    elif user < 0:
        print(f'O número é negativo!')
    else:
        print(f'O número é zero!')

except ValueError:
    print("Erro: Insira apenas valores numéricos inteiros.")
