#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário,
# se por acaso a Carteira de trabalho for diferente de zero. O Dicionário receberá também o ano de contratação e o saláro.
# Calcule e apresente, além da idade, com quantos anos a pessoa vai se aposentar

carteira = dict()

while True:
    nome = input('Insira seu nome: ')
    nascimento = int(input('Insira seu ano de nascimento: '))
    carteira[nome] = {'Ano de nascimento': nascimento}
    pergunta = input('Possui carteira de trabalho? ("S" para sim, "N" para não)')
    if pergunta == 'N':
        break
    if pergunta == 'S':
        carteira['Ano de contratação'] = int(input('Ano de contratação: '))
        carteira['Salário'] = int(input('Valor do seu salário: '))

    idade = 2024 - nascimento
    futuro = idade + 18

    print(futuro)
    print(carteira)