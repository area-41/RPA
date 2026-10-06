import pytesseract
from PIL import Image
import requests
from io import BytesIO

# Adicione esta linha no início do script extrair_texto_imagem_online.py:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

url_imagem = 'https://raw.githubusercontent.com/madmaze/pytesseract/refs/heads/master/tests/data/test.png'

headers = {
    'User-Agent': 'ExampleRPA/1.0'
}

# Acesso à imagem com o método GET
try:
  resposta = requests.get(url_imagem, headers=headers)

except requests.exceptions.Timeout:
  print('Timeout! O servidor demorou muito para responder.')
except requests.exceptions.ConnectionError:
  print('Não foi possível conectar à página Web. Verifique se possui conexão com a Internet.')

if resposta.status_code == 200:
  # Realiza a conversão da resposta para a imagem
  imagem = Image.open(BytesIO(resposta.content))

  # Mostrar a imagem
  imagem.show()

  # Extrair texto
  texto = pytesseract.image_to_string(imagem)

  print('\nTexto extraído da imagem online:')
  print(texto)
else:
  print(f'Erro HTTP com código {resposta.status_code}')