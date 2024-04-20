#Crie um programa que verifica se uma pessoa pode ser doadora de sangue,
# considerando a idade e os critérios de saúde.

idade = int(input('Qual sua idade? '))
peso = float(input('Qual é o seu peso? '))
sono = int(input('Quantas horas de sono por dia?'))

if (idade >= 16) & (peso >= 50) & (peso <= 140) & (sono >= 6):
    print(f'Você pode se tornar um doador!')
else:
    print(f'Você não pode se tornar um doador!')