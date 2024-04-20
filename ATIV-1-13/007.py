#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** 0.5

print(f'A dobro de {numero} é: {dobro}'
      f'\nO triplo de {numero} é: {triplo}')
print(f'A raiz quadrada de {numero} é: {raiz}')