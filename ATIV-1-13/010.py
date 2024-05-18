#Escreva um programa que leia um tipo de dado e usando o método
# .isnumeric(), retorne ao usuário

print('----- Descubra se o dado é numérico ou não! ----- ')

dado = input('Insira um dado: ')
if not dado.isalpha():
    print('Insira apenas letras.')
else:
    #O isnumeric indica que o dado é um número (true) ou não (false).
    print(f'O dado é: {dado.isnumeric()}')