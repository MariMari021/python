#Escreva um programa que leia uma frase, e mostre uma formatação adaptável de acordo com o tamanho da frase, coordenado por uma função

#Exemplo:
# ----------------------------
#     Senai Show de bola
# ----------------------------

def formatacao(frase):
    quant_palavras = len(frase)
    tracos = int(quant_palavras + 8)
    quant_tracos = '-' * tracos
    print(quant_tracos)
    print(frase.center(tracos))
    print(quant_tracos)

frase = input('Digite uma frase: ')

formatacao(frase)

'''
#SOLUÇÃO PROFESSOR
def titulo(msg):
    print('--' * len(msg))
    print(msg.center(2*len(msg)))
    print('--' * len(msg))

titulo('oi')
titulo('Senai Show de bola')'''