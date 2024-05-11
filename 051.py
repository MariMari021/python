#Escreva um programa que tenha uma função, verifica_par(), que receba um número e verifique se é par
def verifica_par(n):
    if n % 2 == 0:
        print('É PAR')
    else:
        print('É IMPAR')

n = int(input('Digite um número: '))
verifica_par(n)

'''
#RESOLUÇÃO PROFESSOR
def verifica_par(n):
    if n % 2 == 0:
        return 1
    else:
        return 0
'''