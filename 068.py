#Escreva um programa que crie um dicionário com as informações de 5 países, como nome, capital,
# população e idioma oficial. Em seguida, permita que o usuário digite o nome de um país e exiba suas informações.

paises = {'brasil': ['brasília', '215 milhões', 'português'],
          'japão': ['tóquio', '126 milhões', 'japonês'],
          'argentina': ['buenos aires', '46 milhões', 'espanhol'],
          'espanha': ['madrid', '47 milhões', 'espanhol'],
          'frança': ['paris', '67 milhões', 'francês']}

for infos in paises:
    chave = input('Digite o país que deseja saber : ').lower()
    print(paises[chave])
