# %pip install pdfplumber


import pdfplumber
from PIL import Image
import matplotlib.pyplot as plt
import io

# Abrir um arquivo pdf
nome_arquivo = 'exemplo_aula.pdf'

with pdfplumber.open(nome_arquivo) as pdf:
  paginas = pdf.pages
  print(f'Arquivo {nome_arquivo} possui {len(paginas)} paginas.\n')

  # Iterando por cada página
  for i, pagina in enumerate(paginas):
    print(f'Pagina {i} possui como dimensões {pagina.width} x {pagina.height}')

  # Extraindo texto da primeira página
  texto_pagina1 = paginas[0].extract_text()
  print('\nTexto presente na primeira pagina:')
  print(texto_pagina1)

  # Extraindo imagens da primeira página
  imagens = paginas[0].images
  print(f'\n Número de imagens encontradas na primeira pagina: {len(imagens)}')

  for i, imagem in enumerate(imagens):
    # Extrair dados da imagem
    imagem_dados = imagem['stream'].get_data()

    # Converter para formato PIL
    imagem_pil = Image.frombytes(mode='RGB', size=imagem['srcsize'], data=imagem_dados)

    # Exibir a imagem
    plt.figure(figsize=(8, 6))
    plt.imshow(imagem_pil)
    plt.title(f'Imagem {i+1}')
    plt.axis('off')
    plt.show()

  # Busca de texto no arquivo pdf, retornando as linhas em que foi encontrado
  print('\n\n')
  texto_busca = 'item'
  for i, pagina in enumerate(paginas, start=1):
    texto = pagina.extract_text()
    # Encontrar a linha completa
    linhas = texto.split('\n')
    for linha in linhas:
      if linha and texto_busca.lower() in linha.lower():
        print(f'Texto {texto_busca} encontrado na pagina {i}:')
        print(linha)
