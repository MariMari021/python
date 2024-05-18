

#Escreva um programa que leia o nome, e o sobrenome, CONCATENE em uma nova variável nome completo, e retorne para o usuáriotry:

print('---- Saiba seu nome completo! -----')

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
if not nome.isalpha():
    print('Insira apenas letras.')
elif not sobrenome.isalpha():
    print('Insira apenas letras.')
elif nome.strip() == '' or sobrenome.strip() == '':
    print("O nome e sobrenome não podem estar em branco.")
else:
    nome_completo = nome + ' ' + sobrenome
    print(f'Seu nome completo é: {nome_completo}')
