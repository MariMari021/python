#Escreva um programa que crie um dicionário com os nomes e preços de 5 produtos.
# Em seguida, exiba o produto mais barato e o mais caro.

produtos = {'produtos': ['macarrão', 'café', 'tomate', 'armário', 'batata'],
            'precos': [5.90, 8.60, 2.85, 59.50, 4.20 ]}


print(f'O produto mais caro é : {produtos['produtos'][produtos['precos'].index(max(produtos['precos']))]}')
print(f'O produto mais barato é : {produtos['produtos'][produtos['precos'].index(min(produtos['precos']))]}')