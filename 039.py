#Faça um programa que leia um número e retorne o fatorial !
#4! = 4 x 3 x 2 x 1

minimo = 1
valor = 1

fatorial = int(input('Digite um valor: '))

while minimo <= fatorial:
    valor *= minimo
    minimo += 1
print(valor)
