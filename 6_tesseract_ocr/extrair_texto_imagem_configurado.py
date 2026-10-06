"""## Configurações do Tesseract

Nesta seção vamos aplicar configurações específicas do Tesseract para reconhecer uma placa de carro e uma imagem com um código de barras e seu respectivo código numérico.

O Tesseract possui duas funcionalidades que podem afetar o resultado do OCR, o *whitelist* e o *Page Segmentation Mode* (PSM). Seu uso correto pode auxiliar na acurácia do OCR.

O *whitelist* determina quais caracteres são esperados para a detecção. Os usos mais comuns de *whitelist* são:

* `ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`: letras maiúsculas e números
* `0123456789`: apenas números
* `0123456789.-/`: números com separadores, usado para CPF, telefone e datas
* `0123456789,.R$`: valores monetários

Já o PSM determina como a *engine* de OCR deve interpretar a estrutura da página, ou seja, como ele deve dividir a imagem em blocos, linhas, palavras ou caracteres antes de tentar reconhecer o texto. Os modos mais comuns são:

* `--psm 3`: segmentação totalmente automática
* `--psm 6`: bloco de texto uniforme
* `--psm 7`: única linha
* `--psm 8`: única palavra
* `--psm 13`: linha de texto simples (mais específico para linhas individuais)

"""

import pytesseract
from PIL import Image

# Adicione esta linha no início do script extrair_texto_imagem_online.py:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Abrir a imagem com placa de carro
imagem_placa = Image.open('imagens/placa_carro.png')

# Mostrar a imagem
imagem_placa.show()

# Exemplo: extrair apenas números e letras maiúsculas
config_placa = '-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 8'
texto_placa = pytesseract.image_to_string(imagem_placa, config=config_placa)
print("\nIdentificação da placa:")
print(texto_placa)

# Abrir a imagem com código de barras
imagem_codigo = Image.open('imagens/codigo_barras.png')

# Mostrar a imagem
imagem_codigo.show()

# Exemplo: extrair apenas números
config_codigo = '-c tessedit_char_whitelist=0123456789 --psm 6'
texto_codigo = pytesseract.image_to_string(imagem_codigo, config=config_codigo)
print("\nIdentificação de código de barras:")
print(texto_codigo)

# Recorte da imagem para eliminar o texto que não interessa
largura, altura = imagem_codigo.size
imagem_codigo_recorte = imagem_codigo.crop((0, 0, largura, altura*0.8))

# Mostrar a imagem recortada
imagem_codigo_recorte.show()

# Exemplo: extrair apenas números
texto_codigo_recorte = pytesseract.image_to_string(imagem_codigo_recorte, config=config_codigo)
print("\nIdentificação de código de barras após o recorte:")
print(texto_codigo_recorte)