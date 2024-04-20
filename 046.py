#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final mostre:

#Qual é o total gasto na compra
#Quantos produtos custam mais de R$1000,00
#Qual é o produto mais barato

soma = 0
quantidade = 0
menorProduto = None

while True:
    nomeProduto = input('Qual é o nome do produto? ')
    precoProduto = float(input('Qual é o preço do produto? '))
    resposta = input('Deseja continuar? [S/N] ->').strip().upper()

    soma += precoProduto

    if precoProduto > 1000:
        quantidade += 1

    if menorProduto == None:
        menorProduto = precoProduto

    if precoProduto < menorProduto:
        menorProduto = precoProduto
        nomeMenor = nomeProduto

    if resposta == 'N':
        print(f'O total gasto é {soma}, são {quantidade} produtos que custam mais de R$1000,00, o produto mais barato é {nomeMenor}.')
        break



