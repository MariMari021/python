#Escreva um programa que leia um tipo de dado e usando a função type(), retorne ao usuário, qual
# o tipo de dado informado

print('----- Descubra qualquer tipo de dado! ----- ')

dado = (input('Insira um dado: '))
if not dado.isalpha():
    print('Insira apenas letras.')
else:
    #O type() indica que tipo de dado é o valor lido
    print(f'O dado informado é número? {type(dado)}')


#exemplo
'''
print(f'exemplos')

a = 1
b = 'EU'
c = {1,2,3}
d ={'Nome': 'Luis Tatin'}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
'''