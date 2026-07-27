import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import time
import random

# Função auxiliar para acessar a página, com tratamento de erros
def acessar_pagina(url):
  # Cabeçalho para identificação do acesso
  headers = {'User-Agent': 'CustomRPA/1.0'}

  # Acesso à página com o método GET
  try:
    resposta = requests.get(url, headers=headers)

  except requests.exceptions.Timeout:
    print(f'Timeout! O servidor demorou muito para responder na requisição de {url}.')
    return None
  except requests.exceptions.ConnectionError:
    print(f'Não foi possível conectar à página Web {url}. Verifique se possui conexão com a Internet.')
    return None

  if resposta.status_code == 200:
    return resposta
  else:
    print(f'Erro HTTP com código {resposta.status_code} na requisição de {url}. Conteúdo da resposta:')
    print(resposta.text)
    return None

# Função auxiliar para extrair os dados do livro
def extrair_dados_livro(livro):
  dados_livro = {}

  # Extração do título do livro
  titulo = livro.h3.a.get('title')
  if titulo:
    dados_livro['titulo'] = titulo.strip()
  else:
    dados_livro['titulo'] = None

  # Extração do preço do livro
  preco_tag = livro.find('p', class_='price_color')
  if preco_tag:
    try:
      preco = float(preco_tag.string.replace('£', '').replace('Â', ''))
    except ValueError:
      preco = 0.0
  dados_livro['preco'] = preco

  # Extração da disponibilidade do livro
  disponivel_tag = livro.find('p', class_='instock')
  if disponivel_tag and disponivel_tag.i.get('class')[0] in 'icon-ok':
    dados_livro['disponivel'] = 'Sim'
  else:
    dados_livro['disponivel'] = 'Não'

  # Extração da classificação do livro
  classificacao_tag = livro.find('p', class_='star-rating')
  if classificacao_tag:
    estrelas = classificacao_tag.get('class')
    if estrelas[1]:
      mapeamento_estrelas = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
      dados_livro['classificacao'] = mapeamento_estrelas[estrelas[1]]
    else:
      dados_livro['classificacao'] = 0

  return dados_livro

# Script Principal

# url = 'https://books.toscrape.com/'
url = 'https://books.toscrape.com/catalogue/page-48.html'

# Lista de livros par armazenar os dados extraídos
livros = []

# Navegação entre páginas
contador_paginas = 1
paginas_fim = -1 # Se for igual a -1, buscar todas as páginas
url_atual = url

while True:
  print(f'Web Scraping da pagina {contador_paginas}')

  # Acesso à página
  resposta = acessar_pagina(url_atual)
  if not resposta:
    break

  # Criação do objeto BeautifulSoup para navegar nos elementos da página
  soup = BeautifulSoup(resposta.text, 'html.parser')

  # Busca por todos os livros
  livros_pagina = soup.find_all('article', class_='product_pod')
  print(f'{len(livros_pagina)} encontrados na pagina {url_atual}')

  # Extração dos dados de cada livro
  for livro in livros_pagina:
    dados_livro = extrair_dados_livro(livro)
    livros.append(dados_livro)

  print(f'Extraídos {len(livros)} dados de livros no total')

  # Busca pelo botão de próxima página
  botao_proxima = soup.find('li', class_='next')

  if not botao_proxima or not botao_proxima.a:
    print('Última página processada!')
    break
  else:
    # Definição da URL da próxima página
    link_proxima_pagina = botao_proxima.a.get('href')
    url_atual = urljoin(url_atual, link_proxima_pagina)
    contador_paginas += 1

  # Verificação se atingiu o número de páginas limite
  if paginas_fim != -1 and contador_paginas > paginas_fim:
    break

  # Aguarda um tempo aleatório entre 1 e 5 segundos antes da próxima requisição
  time.sleep(random.randint(1, 5))


# Se os dados de pelo menos um livro for coletado, salvá-los em um arquivo
if len(livros) > 0:

  df_livros = pd.DataFrame(livros)

  # Verificar dados duplicados e nulos nos dados extraídos
  print(f'\nNúmero de livros duplicados: {df_livros.duplicated().sum()}')
  if df_livros.duplicated().sum() > 0:
    df_livros.drop_duplicates(inplace=True)

  print(f'Dados nulos por colunas:')
  print(df_livros.isnull().sum())

  # Escrita dos dados em arquivo xlsx
  arquivo = 'dados_livros.xlsx'
  df_livros.to_excel(arquivo, index=False, sheet_name='Livros')
  print(f'Arquivo {arquivo} gerado com os dados coletados.')

