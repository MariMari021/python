#Escreva um programa que peça ao usuário uma idade e imprima se é maior
# ou menor de idade (18 anos).

print('----- Veja se você é maior ou menor de idade! -----')

try:
    usuario = int(input(f'Qual é a sua idade? '))

    if usuario >= 18:
        print(f'Você é maior de idade!')
    else:
        print(f'Você é menor de idade!')

except ValueError:
    print("Erro: Insira apenas valores númericos inteiros.")