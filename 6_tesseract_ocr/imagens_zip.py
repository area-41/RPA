import zipfile
import os

import os
import zipfile

arquivo_imagens = 'imagens.zip'
pasta_destino = 'imagens'

if not os.path.exists(arquivo_imagens):
  print(f'Arquivo {arquivo_imagens} não encontrado! Faça o upload do arquivo primeiro.')
else:
  # Criar a pasta de destino caso ela não exista
  if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

  # Descompactar arquivo na pasta especificada
  try:
    with zipfile.ZipFile(arquivo_imagens, 'r') as zip:
      zip.extractall(pasta_destino)
    print(f'Arquivo descompactado com sucesso na pasta "{pasta_destino}"!')

  except Exception as e:
    print(f'Erro ao descompactar {arquivo_imagens}: {e}')