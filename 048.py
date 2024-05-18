#Crie um programa que pede ao usuário para digitar dois números e, em seguida,
# divide o primeiro número pelo segundo número.
#No entanto, o programa deve ser capaz de lidar com a possibilidade de o usuário
# digitar um valor inválido, como uma string ou o número zero.

#ZeroDivisionError ; ValueError

print('----- Divida um pelo outro -----')

try:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))

    div = n1 / n2
    print(f'A divisão será: {div}')

except ZeroDivisionError:
    print('Divisão por zero')
except ValueError:
    print('Apenas números')
