#Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a
# média, é insuficiente (menor que 6), suficiente (entre 6 e 7), bom
# (entre 7 e 9) ou excelente (9 ou maior).

nota1 = int(input('Digite a nota1:'))
nota2 = int(input('Digite a nota2:'))
nota3 = int(input('Digite a nota3:'))
nota4 = int(input('Digite a nota4:'))
nota5 = int(input('Digite a nota5:'))

media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

if media < 6:
    print(f'Média insuficiente!')
elif media <= 7:
    print(f'Média suficiente!')
elif media <= 9:
    print(f'Média está boa!')
elif media <= 10:
    print(f'Média excelente!')