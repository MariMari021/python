#Crie um programa que verifica se uma pessoa pode ser doadora de sangue,
# considerando a idade e os critérios de saúde.

print('----- Saiba se você possui os requisitos para doar sangue! -----')

try:
    idade = int(input('Qual sua idade? '))
    peso = float(input('Qual é o seu peso? '))
    sono = int(input('Quantas horas de sono por dia?'))

    if (idade >= 16) and (peso >= 50) and (peso <= 140) and (sono >= 6):
        print(f'Você pode se tornar um doador!')
    else:
        print(f'Você não pode se tornar um doador!')

except ValueError:
    print(
        "Erro: Insira apenas valores númericos inteiros.")