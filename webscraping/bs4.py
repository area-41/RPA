import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

# Acesso à página com o método GET
try:
  resposta = requests.get(url)

except requests.exceptions.Timeout:
  print('Timeout! O servidor demorou muito para responder.')
except requests.exceptions.ConnectionError:
  print('Não foi possível conectar à página Web. Verifique se possui conexão com a Internet.')

if resposta.status_code == 200:
  # Criação do objeto BeautifulSoup que representa a estrutura do documento
  soup = BeautifulSoup(resposta.text, 'html.parser')

  # Apresentar o código HTML da página de maneira mais clara e organizada
  # Como pode ser muito grande, selecionamos os primeiros 2000 caracteres
  print(soup.prettify()[:2000])

  # Acesso às informações da página com os atributos do objeto BeautifulSoup
  print(f'\nTítulo da página: {soup.title}')
  print(f'Conteúdo do título da página: {soup.title.string}')

  # Busca pelo primeiro elemento quote
  print(f'\nPrimeiro quote:')
  quote = soup.find('div', class_='quote')
  print(quote)
  print(f'\nPrimeira citação: {quote.span.string}')

  # Busca por todas as tags span no primeiro quote
  spans_quote = quote.find_all('span')
  print('\nTodos os spans do primeiro quote')
  print(spans_quote)
  print(f'\nPrimeira citação: {spans_quote[0].string} do autor {spans_quote[1].small.string}')

  # Busca por todas as citações e autores
  todas_citacoes = soup.find_all('div', class_='quote')
  print(f'\nForam encontradas {len(todas_citacoes)} citações')

  # Mostra as primeiras 5 citações, com autores e tags
  print('\nPrimeiras 5 citações:')
  for citacao in todas_citacoes[:5]:
    autor = citacao.find('small', class_='author')
    tags = citacao.find('meta', class_='keywords').get('content')
    if citacao.span and autor and tags:
      print(f'{citacao.span.string} por {autor.string}.\nTags: {tags}')

else:
  print(f'Erro HTTP com código {resposta.status_code}')