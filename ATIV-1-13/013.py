#Crie um programa que leia uma frase e mostre:
#Quantas vezes aparece a letra “a”
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece na última vez


print('-----Saiba quantas vezes a letra "a" se repete! -----')

frase = input('Digite uma frase: ')

if not frase.isalpha():
    print('Insira apenas letras.')

elif len(frase) == 0:
    print("Erro: A caixa de entrada não estar vazia.")
else:
    print(f'A letra (a) aparece {frase.count("a")} vezes')
    print(f'A primeira posição é {frase.find("a")}')
    print(f'A última posição é {frase.rfind("a")}')


