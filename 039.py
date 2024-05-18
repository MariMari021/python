#Faça um programa que leia um número e retorne o fatorial !
#4! = 4 x 3 x 2 x 1

print('----- Saiba o fatorial de qualquer número -----')

minimo = 1
valor = 1

try:
    fatorial = int(input('Digite um valor: '))

    while minimo <= fatorial:
        valor *= minimo
        minimo += 1
    print(valor)
except ValueError:
    print('Insira apenas valores númericos inteiros.')
