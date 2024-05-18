#Escreva um programa que peça ao usuário um número e imprima se
# está entre 0 e 10, entre 10 e 20 ou maior que 20.

print('----- Saiba o intervalo númerico de qualquer número! -----')

try:
    usuario = float(input('Insira um número: '))

    if usuario <= 10:
        print(f'O número está entre 0 e 10!')
    elif usuario <= 20:
        print(f'O número está entre 10 e 20!')
    else:
        print(f'O número é maior que 20!')

except ValueError:
    print("Erro: Insira apenas números!")
    