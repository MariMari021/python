#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário,
# se por acaso a Carteira de trabalho for diferente de zero. O Dicionário receberá também o ano de contratação e o saláro.
# Calcule e apresente, além da idade, com quantos anos a pessoa vai se aposentar
'''
carteira = dict()

while True:
    nome = input('Insira seu nome: ')
    nascimento = int(input('Insira seu ano de nascimento: '))
    pergunta = input('Possui carteira de trabalho? ("S" para sim, "N" para não)').upper()
    idade = 2024 - nascimento

    if pergunta == 'N':
        print('Você não possui carteira de trabalho, então é possível calcular com quantos anos irá se aposentar!')
        break
    if pergunta == 'S':
        contratacao = int(input('Ano de contratação: '))
        salario = float(input('Valor do seu salário: '))
        contribuicao = 2024 - contratacao
        if idade >= 62 and contribuicao >= 15:
            print(f'Você já pode se aposentar! ')
            break
        else:
            total = 62 - idade
            totalFinal = idade + total
            print(f'Você tem {idade} anos e irá se aposentar com {totalFinal} anos.')
            carteira[nome] = {'Nome': nome, 'Nascimento': nascimento, 'Contribuição': contribuicao, 'Idade que irá se aposentar': totalFinal}
            print(carteira[nome])
            break

'''


from datetime import datetime

funcionarios = []

while True:
    try:
        nome = input('Digite o nome [sair para parar]: ')
        if nome == 'sair':
            break
        ano_nascimento = int(input('Digite o ano de nascimento: '))
        carteira_trabalho = int(input('Digite a carteira de (0 se não tiver): '))
        if carteira_trabalho != 0:
            ano_contratacao = int(input('Digite o ano de contratação: '))
            salario = float(input('Digite o salário do funcionário: '))
            idade = datetime.now().year - ano_nascimento
            aposentadoria = ano_contratacao + 35 - ano_nascimento
            funcionarios.append({'nome': nome,
                                 'idade': idade,
                                 'carteira_trabalho': carteira_trabalho,
                                 'ano_contratacao': ano_contratacao,
                                 'salario': salario,
                                 'aposentadoria': aposentadoria})
        else:
            idade = datetime.now().year - ano_nascimento
            funcionarios.append({'nome': nome,
                                 'idade': idade,
                                 'carteira_trabalho': carteira_trabalho})

    except ValueError:
        print('Cuidado, você digitou alguma coisa errada.')

for i in funcionarios:
    print(f'Nome: {i["nome"]}'
          f'\nIdade: {i["idade"]}')
    if i['carteira_trabalho']:
        print(f'Carteira trabalho: {i["carteira_trabalho"]}'
              f'\nAno de Contratação: {i["ano_contratacao"]}'
              f'\nSalário: R$ {i["salario"]}'
              f'\nAno de aposentadoria: {i["aposentadoria"]}' )
        print('-'*30)