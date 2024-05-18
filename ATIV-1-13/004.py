'''
Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

V = (4/3) . π . r³
A = 4 . π . r²
'''

print('----- Descubra o volume e a área de qualquer esfera aqui! -----')

try:
    raio = float(input('Qual é o raio da esfera? '))
    volume = (4/3) * 3.14 * raio ** 3
    area = 4 * 3.14 * raio ** 3
    print(f'Volume da esfera: {volume}')
    print(f'Área da esfera: {area}')
except ValueError:
    print("Insira apenas valores numéricos para o raio.")

