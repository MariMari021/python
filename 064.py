#Crie um programa onde o usuário possa digitar sete letras, e cadastre em uma única lista,
# que mantenha separado as consoantes das vogais

lista = []
lista_auxiliar_vogais = []
lista_auxiliar_consoantes = []

for ele in range(7):
    letras = input('Digite uma letra: ').upper()
    if letras in 'AEIOU':
        lista_auxiliar_vogais.append(letras)
    else:
        lista_auxiliar_consoantes.append(letras)

lista.append(lista_auxiliar_vogais[:])
lista.append(lista_auxiliar_consoantes[:])

print(lista)
