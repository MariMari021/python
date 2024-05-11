#Crie um programa que leia o nome, sexo e idade de vários Alunos, guardando os dados de
# cada aluno em um dicionário e todos os dicionários em uma lista. No final mostre:

#Quantas pessoas foram cadastradas
#A média de idade do grupo
#Uma lista com todas as mulheres
#Uma lista com todas as pessoas com idade acima da média


alunos = []
alunoIndividual = {}
mulheres = []
acimaMedia = []
somaIdades = 0


while True:
    try:
        nome = (input('Digite o seu nome [sair para acabar]: '))
        if nome == 'sair':
            break
        sexo = (input('Digite o seu sexo: ')).strip().upper()
        idade = (int(input('Digite sua idade: ')))

        somaIdades += idade
        alunoIndividual[nome] = {'Sexo': sexo, 'Idade': idade}
        alunos.append(alunoIndividual.copy())
        media = somaIdades / len(alunos)

        if idade > media:
            acimaMedia.append(alunoIndividual.copy())
        if sexo == 'FEMININO':
            mulheres.append(alunoIndividual.copy())
        alunoIndividual.clear()
    except ValueError:
        print('Digite apenas números!')


print(f'Quantidade de alunos cadastrados: {len(alunos)}'
      f'\nMédia de idade: {media}'
      f'\nLista de alunas: {mulheres}'
      f'\nAlunos acima da média de idades: {acimaMedia}')


'''

alunos = []

while True:
    nome = input('Digite o nome [sair para parar]: ')
    if nome == 'sair':
        break

    sexo = input('Sexo [M/F]: ').strip().upper()
    idade = int(input('Digite sua idade: '))
    alunos.append({'nome': nome,
                   'sexo': sexo,
                   'idade': idade})

# N de cadastros

num_cadastrados = len(alunos)
#calculo de media de idade do grupo
soma_idades = sum(aluno['idade'] for aluno in alunos)
media_idade = soma_idades / num_cadastrados

#criar lista com todas as mulheres
mulheres = [aluno["nome"] for aluno in alunos if aluno ['sexo'] == 'F']

#lista acima da média
acima_media = [aluno['nome'] for aluno in alunos if aluno ['idade'] > media_idade ]

#exibir
print(f'N de pessoas: {num_cadastrados}'
        f'\nMedia de idades: {media_idade}'
        f'\nLista de mulheres: {mulheres}'
        f'\nLista de pessoas com a idade acima da média: {acima_media}')
'''