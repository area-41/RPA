"""## Extração de Texto de Imagens com Tamanhos Diferentes

Nesta seção visualizamos como o tamanho da fonte  pode impactar o reconhecimento de texto pelo `pytesseract`.
"""

import pytesseract
from PIL import Image


# Adicione esta linha no início do script extrair_texto_imagem_online.py:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Abrir a imagem com texto pequeno
imagem = Image.open('imagens/imagem_com_texto_pequeno.png')

# Mostrar a imagem
imagem.show()

# Extrair texto
texto = pytesseract.image_to_string(imagem, lang='por')

print('\nTexto extraído:')
print(texto)

# Abrir a imagem com texto grande
imagem_nova = Image.open('imagens/imagem_com_texto_grande.png')

# Mostrar a imagem
imagem_nova.show()

# Extrair texto
texto_nova = pytesseract.image_to_string(imagem_nova, lang='por')

print('\nTexto extraído:')
print(texto_nova)

"""## Pré-processamento para Melhorar OCR

Nesta seção vamos aprender como técnicas de pré-processamento de imagens podem melhorar a precisão do OCR. Começamos com uma extração de texto sem pré-processamento para demonstrar os desafios de imagens de baixa qualidade.

Em seguida, vamos aplicar uma série de passos de pré-processamento, incluindo:

1.  **Conversão para escala de cinza**: reduz a complexidade da imagem, mantendo a informação de luminância para o OCR.
2.  **Filtros de remoção de ruídos (OpenCV)**: suavização da imagem com o filtro da mediana para remover ruídos que podem confundir o Tesseract.
3.  **Redimensionamento**: aumento da resolução da imagem para ajudar o Tesseract a detectar caracteres pequenos ou de baixa qualidade.

O objetivo é mostrar o impacto positivo de cada etapa na qualidade do texto extraído.
"""

import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import cv2

#############################################
# Extrair texto sem pré-processamento
#############################################

# Abrir a imagem com texto pequeno
imagem = Image.open('imagens/documento_problemas.jpg')

# Mostrar a imagem
imagem.show()

# Extrair texto
texto = pytesseract.image_to_string(imagem, lang='por')

print('\nTexto extraído sem pré-processamento:')
print(texto)

#############################################
# Extrair texto com pré-processamento
#############################################

# Conversão para a escala de cinza
imagem_cinza = imagem.convert('L')
imagem_cinza.show()

texto = pytesseract.image_to_string(imagem_cinza, lang='por')
print('\nTexto extraído após escala de cinza:')
print(texto)

# Filtros do OpenCV para remoção dos ruídos
imagem_cv = np.array(imagem_cinza)

# Filtro de mediana com blur suave
imagem_cv_filtro = cv2.medianBlur(imagem_cv, 3)

# Converte novamente para PIL
imagem_filtro = Image.fromarray(imagem_cv_filtro)
imagem_filtro.show()

texto = pytesseract.image_to_string(imagem_filtro, lang='por')
print('\nTexto extraído após filtro:')
print(texto)

# Redimensionamento
largura, altura = imagem_filtro.size
imagem_grande = imagem_filtro.resize((largura*2, altura*2), Image.Resampling.LANCZOS)
imagem_grande.show()

texto = pytesseract.image_to_string(imagem_grande, lang='por')
print('\nTexto extraído após pré-processamento:')
print(texto)