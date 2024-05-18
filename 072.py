#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário,
# se por acaso a Carteira de trabalho for diferente de zero. O Dicionário receberá também o ano de contratação e o saláro.
# Calcule e apresente, além da idade, com quantos anos a pessoa vai se aposentar

carteira = dict()

try:
    while True:
        nome = input('Insira seu nome, [parar para sair]: ')
        if nome == 'parar':
            print('Sistema finalizado!')
            break
        nascimento = int(input('Insira seu ano de nascimento: '))
        pergunta = input('Possui carteira de trabalho? ("Sim" para sim, "Não" para não)').upper()
        idade = 2024 - nascimento

        if pergunta == 'NÃO':
            print('Você não possui carteira de trabalho, então é possível calcular com quantos anos irá se aposentar!')
            break
        if pergunta == 'SIM':
            contratacao = int(input('Ano de contratação: '))
            salario = float(input('Valor do seu salário: '))
            contribuicao = 2024 - contratacao
            totalFinal = contratacao + 35 - nascimento
            carteira[nome] = {'Nome': nome, 'Idade': idade, 'Nascimento': nascimento, 'Possui carteira de trabalho': pergunta,
                              'Contribuição': contribuicao, 'Idade que irá se '
                                                            'aposentar': totalFinal, 'Salário': salario}
            break

except ValueError:
    print(f"Você digitou algo errado!")

for nome, dados in carteira.items():
    print('-' * 30)
    print(f'Nome: {dados["Nome"]}'
          f'\nIdade: {dados["Idade"]}')
    if dados['Possui carteira de trabalho']:
        print(
              f'Contribuição: {dados["Contribuição"]}'
              f'\nSalário: R$ {dados["Salário"]}'
              f'\nVocê ira se aposentar com: {dados["Idade que irá se aposentar"]} anos')
        print('-' * 30)


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
    '''