#Faça um programa que simule um cadastro de Aluno com,
# nome, data de nascimento, sexo, idade, organize tudo em um dicionário, e após isso em uma
# lista

#Após isso, o programa deve abrir um txt e adicionar os cadastros ao final do arquivo

alunos = []

while True:
    try:
        nome = input('Digite o seu nome [sair para parar]: ')
        if nome == 'sair':
            print('Sistema finalizado!')
            break

        sexo = input('Digite seu sexo, "M" para masculino ou "F" para feminino: ')

        if not nome.isalpha():
            print('Digite no nome apenas letras.')
        elif not sexo.isalpha():
            print('Digite no campo sexo apenas letras.')
        else:
            nascimento = input('Digite a data de seu nascimento por estenso "21 de junho de 2007": ')
            idade = int(input('Digite sua idade: '))
            alunos.append({'Nome': nome, 'Sexo': sexo, 'Data de Nascimento': nascimento, 'Idade': idade})

    except ValueError:
        print('No campo idade digite apenas números.')

arquivo = open('registroNovo.txt', 'a')

for x in alunos:
    arquivo.write('\n--------------')
    arquivo.write(f'\nNome: {x["Nome"]}'
                  f'\nData de Nascimento: {x["Data de Nascimento"]}'
                  f'\nSexo: {x["Sexo"]}'
                  f'\nIdade: {x["Idade"]}')

arquivo.close()

'''

from datetime import datetime

Alunos = []

while True:
    nome = input('Digite o nome[sair]: ')
    if nome == 'sair':
        break
    nascimento = input('Digite a data de nascimento DD/MM/AAAA: ')
    sexo = input('Digite o sexo: ')

    Alunos.append({'nome': nome,
                   'nascimento': nascimento,
                   'sexo': sexo,
                   'idade': datetime.now().year - int(nascimento.split('/')[-1])})

arquivo = open('registroNovo.txt', 'a')

for x in Alunos:
    arquivo.write('\n--------------')
    arquivo.write(f'\nNome: {x["nome"]}'
                  f'\nData de Nascimento: {x["nascimento"]}'
                  f'\nSexo: {x["sexo"]}'
                  f'\nIdade: {x["idade"]}')

arquivo.close()
'''