#Crie um programa que leia uma frase e mostre:
#Quantas vezes aparece a letra “a”
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece na última vez


frase = input('Digite uma frase: ')

print(f'A letra (a) aparece {frase.count("a")}')
print(f'A primeira posição é {frase.find("a")}')
print(f'A última posição é {frase.rfind("a")}')


