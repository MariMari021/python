#Escreva um programa que peça ao usuário uma senha e
# verifique se ela está correta (a senha correta é "python123").

import time

print('---- Bem vindo ao Banco Senai ----')
usuario = input('Digite a senha correta: ')

print('Decodificando o código!')
time.sleep(1)
print('1...')
time.sleep(2)
print('2...')
time.sleep(3)
print('3...')

if usuario == 'python123':
    print(f'Senha correta!')
else:
    print(f'Senha incorreta!')