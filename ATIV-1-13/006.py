#Escreva um programa que leia 6 notas diferentes e faça a média do aluno

print('----- Saiba sua média final aqui! -----')

try:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota4 = float(input('Digite a quarta nota: '))
    nota5 = float(input('Digite a quinta nota: '))
    nota6 = float(input('Digite a sexta nota: '))
    media = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6) / 6
    print(f'A sua média final é: {media}')
except ValueError:
    print("Insira apenas valores numéricos para as notas.")