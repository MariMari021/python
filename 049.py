#Crie um programa que tenha a função área(), que receba as dimensões de um muro
# retangular e mostra a área do terreno

print('----- Calcule a área de um muro retangular -----')
def area (a, b):
    area = a * b

    return area

try:
    a = float(input('Digite a altura do muro retangular: '))
    b = float(input('Digite o comprimento do muro retangular: '))

    if a == b:
        print('Apenas dimensões de um muro retangular.')
    else:
        print(f'A área do muro retangular é {area(a, b)}')

except ValueError:
    print(f"Insira apenas números")




'''
#RESOLUÇÃO DO PRFESSOR
def area(a, b):
    resultado = a * b
    print(f'A área do terreno é {resultado}')

#ele rrecomenda esse
def area_terreno(a, b):
    resultado = a * b
    return resultado

print(area_terreno(1, 3))
area(4, 5)'''