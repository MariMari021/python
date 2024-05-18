#Exercicio 074

def soma(a,b):
    return a + b

def divisao(a,b):
    return a/b

def subtracao(a,b):
    return a - b

def multi(a,b):
    return a*b

def somaMais(*numeros):
    return sum(numeros)

def divisaoMais(*numeros):
    return sum(numeros)/len(numeros)

def multiMais(*numeros):
    d = 1
    for ele in numeros:
        d *= ele
    return d


#Exercicio 075

def titulo(msg):
    titulos = msg.title()
    return titulos

def frase(msg):
    frases = '----' * len(msg) + msg.center(2*len(msg)) + '----' * len(msg)
    return frases

def quebra_linha():
    pular = '\n'
    return pular