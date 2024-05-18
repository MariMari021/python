#Escreva um programa que leia diversos alunos, crie um dicionário com as notas de dele
# em três disciplinas: matemática, português e história. Em seguida, exiba a média das notas do aluno.


alunos =dict()

try:
    for i in range(0, 4):
        nome = input('Nome do aluno: ')
        matematica = float(input('Nota de matemática: ').lower())
        historia = float(input('Nota de história: ').lower())
        portugues = float(input('Nota de português: ').lower())
        media = (matematica + historia + portugues) / 3
        alunos[nome] = {'matemática': matematica, 'história': historia, 'portugues': portugues,
                        'média': media}

    print("\nNotas dos alunos:")
    for nome, notas in alunos.items():
        print(f"Notas de {nome}:")
        print(f"Matemática: {notas['matemática']}")
        print(f"História: {notas['história']}")
        print(f"Português: {notas['portugues']}")
        print(f"Média Final: {notas['média']}\n")

except ValueError:
    print('Insira apenas números nas notas.')
'''

#resolução professor

alunos = {}

while True:
    try:
        nome = input('Digite o nome do aluno [sair para acabar]:')
        if nome == 'sair':
            break

        matematica = float(input('Digite sua nota em matemática: '))
        portugues = float(input('Digite sua nota em português: '))
        historia = float(input('Digite sua nota em história: '))

        alunos[nome] = {'Matemática': matematica, 'Português': portugues, 'História': historia}

    except ValueError:
        print('Só aceitamos números.')

    for nome, notas in alunos.items():
        media_aritmerica = sum(notas.values()) / len(notas)
        print(f'A média de {nome} é de {media_aritmerica}')
'''