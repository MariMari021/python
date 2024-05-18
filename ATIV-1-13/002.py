#Escreva um programa que leia, o nome, idade, e cidade de nascimento e retorne para o usuário
print("----- Agrupe suas informações pessoais! -----")

try:
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    cidade = input('Digite sua cidade natal: ')
    if not nome.isalpha():
        print('Insira apenas letras.')
    elif not cidade.isalpha():
        print('Insira apenas letras.')
    else:
        print(f'Meu nome é {nome}, tenho {idade} anos e nasci em {cidade}')
except ValueError:
    print("Por favor, insira um valor numérico válido para a idade.")
