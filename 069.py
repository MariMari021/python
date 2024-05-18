#Escreva um programa que crie um dicionário com as informações de 5 livros,
# como título, autor, ano de lançamento e número de páginas. Em seguida, exiba apenas os autores dos livros.

livros = {'esplêndida': ['Julia Quinn', '15 de abril de 2021 ', 336],
          'Xeque-mate': ['Ali Hazelwood', '7 de novembro de 2023', 336],
          'Quarta Asa': ['Rebecca Yarros', '18 de março de 2024', 544],
          'A noiva': ['Ali Hazelwood', '7 de março de 2024', 368],
          'Caraval': ['Stephanie Garber', '30 de setembro 2022', 352]}


for infos in livros:
    print(livros[infos][0])
'''

#Explicação professor

livros = {'esplêndida': {'autor': 'Julia Quinn', 'ano': '15 de abril de 2021 ', 'paginas': 336},
          'Xeque-mate': {'autor': 'Ali Hazelwood', 'ano': '7 de novembro de 2023', 'paginas': 336},
          'Quarta Asa': {'autor': 'Rebecca Yarros', 'ano': '18 de março de 2024', 'paginas': 544},
          'A noiva': { 'autor': 'Ali Hazelwood','ano': '7 de março de 2024', 'paginas': 368},
          'Caraval': {'autor': 'Stephanie Garber', 'ano': '30 de setembro 2022', 'paginas': 352}}

for chave in livros:
    print(livros[chave]['autor'])'''