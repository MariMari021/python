#Escreva um programa que leia diversos alunos, crie um dicionário com as notas de dele
# em três disciplinas: matemática, português e história. Em seguida, exiba a média das notas do aluno.
'''
carro = dict ()
concessionaria = list ()


for c in range(0, 3):
    carro['nome'] = str(input('Nome do Carro '))
    carro['ano'] = int(input('Ano do Carro '))
    concessionaria.append(carro.copy())

print(concessionaria)
print(carro)'''


alunos =dict()


for i in range(0, 4):
    nome = input('Nome do aluno: ')
    matematica = int(input('Nota de matemática: ').lower())
    historia = int(input('Nota de história: ').lower())
    portugues = int(input('Nota de português: ').lower())
    media = (matematica + historia + portugues) / 3
    alunos[nome] = {'matemática': matematica, 'história': historia, 'portugues': portugues, 'média': media}

    print(alunos)
