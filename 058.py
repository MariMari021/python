#Crie um programa onde serão informados diversos valores em uma lista.
# Caso o número já exista ele não será adicionado. No final, serão exibidos todos
# os valores únicos em ordem crescente




try:
    valores = []
    for ele in range(5):
        valor = int(input('Digite um valor: '))

        if valor not in valores:
            valores.append(valor)

    print(sorted(valores))
except ValueError:
    print('Insira apenas números inteiros.')


'''

#resolucao do prof

lista = []

while True:
    numero = input('Digite um numero [sair para acabar: ')

    if numero == 'sair':
        break

    if int(numero) in lista:
        print('Já existe')
    else:
        lista.append(int(numero))

print(sorted(lista))

'''