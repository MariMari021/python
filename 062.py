#Escreva um programa que crie duas listas com 5 números cada uma e exiba a soma dos elementos correspondentes das
# duas listas. Por exemplo, se as listas forem [1, 2, 3, 4, 5] e [5, 4, 3, 2, 1], o programa deve exibir [6, 6, 6, 6, 6].


listaUm = [1, 2, 3, 4, 5]
listaDois = [5, 4, 3, 2, 1]
lista = []

for ele in range(5):
    soma = listaUm[ele] + listaDois[ele]
    lista.append(soma)

print(f'A soma desses valores é {lista}')

