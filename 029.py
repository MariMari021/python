#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.
multi = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero = int(input('Digite um número: '))
for multi in range (1, 11):
    multi = numero * multi
    print(multi)


'''
numero = int(input('Digite um número: '))

for ele in range(1, 11):
print(f'{numero} X {ele} = {numero * ele}')

'''