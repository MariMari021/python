#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois, deve mostrar para cada palavra, suas vogais

print('----- Veja as vogais da tupla palavras -----')

palavras = ('mar', 'aquarela', 'mouse', 'garrafa', 'dedo')

for ele in palavras:
    print(ele + ' - ', end=' ')
    for letras in ele:
        #print(letras)
        if letras in 'aeiouAEIOU':
            print (letras, end= ' ')
    print('\n')
