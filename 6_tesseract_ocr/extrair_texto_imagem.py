import pytesseract
from PIL import Image

# Caminho do executável do Tesseract no Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# --- 1. Primeira Imagem (Inglês) ---
caminho_img1 = 'imagens/imagem_com_texto_eng.png'
imagem1 = Image.open(caminho_img1)

# Abre a imagem no visualizador do Windows
imagem1.show()

# Extrair texto
texto1 = pytesseract.image_to_string(imagem1)

print(f"\n==================================================")
print(f" TEXTO EXTRAÍDO DO ARQUIVO: {caminho_img1}")
print(f"==================================================")
print(texto1)


# --- 2. Segunda Imagem (Português) ---
caminho_img2 = 'imagens/imagem_com_texto_por.png'
imagem2 = Image.open(caminho_img2)

# Abre a imagem no visualizador do Windows
imagem2.show()

# Extrair texto com configuração default (inglês)
texto_eng = pytesseract.image_to_string(imagem2)

print(f"\n==================================================")
print(f" TEXTO EXTRAÍDO DO ARQUIVO: {caminho_img2} (Default: Inglês)")
print(f"==================================================")
print(texto_eng)

# Extrair texto com linguagem especificada em português
texto_por = pytesseract.image_to_string(imagem2, lang='por')

print(f"\n==================================================")
print(f" TEXTO EXTRAÍDO DO ARQUIVO: {caminho_img2} (Idioma: Português)")
print(f"==================================================")
print(texto_por)