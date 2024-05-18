#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

print('----- Descobra se a letra é consoante ou vogal! -----')

usuario = input('Digite uma letra: ')

if not usuario.isalpha():
    print('Insira apenas letras.')

elif len(usuario) == 0:
    print('O campo de entrada está vazio.')
else:
    if usuario == 'a' or usuario == 'A':
        print(f'A letra é vogal!')
    elif usuario == 'e' or usuario == 'E':
        print(f'A letra é vogal!')
    elif usuario == 'i' or usuario == 'I':
        print(f'A letra é vogal!')
    elif usuario == 'o' or usuario == 'O':
        print(f'A letra é vogal!')
    elif usuario == 'u' or usuario == 'U':
        print(f'A letra é vogal!')
    else:
        print(f'A letra é consoante!')

