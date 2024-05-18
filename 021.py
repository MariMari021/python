#Escreva um programa que peça ao usuário um número de 1 a 7 e imprima o dia da
# semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).

print('----- Veja qual número corresponde aos dias da semana! -----')

try:
    usuario = int(input('Digite um número de 1 a 7: '))

    if usuario == 1:
        print(f'1 é Segunda-Feira. ')
    elif usuario == 2:
        print(f'2 é Terça-Feira. ')
    elif usuario == 3:
        print(f'3 é Quarta-Feira. ')
    elif usuario == 4:
        print(f'4 é Quinta-Feira. ')
    elif usuario == 5:
        print(f'5 é Sexta-Feira. ')
    elif usuario == 6:
        print(f'6 é Sábado. ')
    elif usuario == 7:
        print(f'7 é Domingo. ')
    else:
        print(f'O valor digitado não é de 1 a 7!')

except ValueError:
    print("Erro: Digite apenas números inteiros.")