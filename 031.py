#Escreva um programa que verifique se uma frase é um palíndromo.

print('----- Saiba se a palavra é um palíndromo! -----')

palavra = input('Digite um palíndromo: ').strip().lower()
compatibilidade = 0

if not palavra.isalpha():
    print('Digite um dado válido.')
else:
    for i in range(0, len(palavra)):
        if palavra[i] == palavra[-i-1]:
            compatibilidade += 1

        if compatibilidade == len(palavra):
            print('É palíndromo!')
        else:
            print('Não é palíndromo!')


#2











