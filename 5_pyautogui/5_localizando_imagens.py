import pyautogui
import time
import webbrowser
import os

# Ativar Fail-Safe
pyautogui.FAILSAFE = True

try:
    # Abre uma aplicação similar ao Paint (exemplo: Microsoft Paint) na internet
    url = "https://jspaint.app/"
    webbrowser.open(url)

    time.sleep(5)  # Aguarda o carregamento da página
    # Gera imagem de botão se não existir
    imagem_pincel = "botao_pincel.png"
    imagem_texto = "botao_texto.png"
    if not os.path.exists(imagem_pincel) or not os.path.exists(imagem_texto):
        # Salvar imagem do botão pincel
        x_pincel = 31
        y_pincel = 181
        botao_pincel = pyautogui.screenshot(region=(x_pincel, y_pincel, 25, 25))
        botao_pincel.save(imagem_pincel)
        print(f"Imagem do botão pincel salva como {imagem_pincel}")
        time.sleep(1)  # Aguarda um segundo antes de capturar a próxima imagem

        # Salvar imagem do botão texto
        x_texto = 31
        y_texto = 204
        botao_texto = pyautogui.screenshot(region=(x_texto, y_texto, 25, 25))
        botao_texto.save(imagem_texto)
        print(f"Imagem do botão texto salva como {imagem_texto}")
        time.sleep(1)  # Aguarda um segundo antes de prosseguir
        
    try:
        # Localiza a imagem do botão pincel na tela
        posicao_pincel = pyautogui.locateOnScreen(imagem_pincel)
        #posicao_pincel = pyautogui.locateOnScreen(imagem_pincel, confidence=0.7)
        centro_botao_pincel = pyautogui.center(posicao_pincel)
        pyautogui.click(centro_botao_pincel)  # Clica no botão pincel
        time.sleep(1)  # Aguarda um segundo antes de prosseguir

        # Desenhar um quadro
        pyautogui.moveRel(300, 0, duration=0.3)  # Move o cursor para a posição inicial do quadro
        pyautogui.dragRel(200, 0, duration=2.5)  # Linha horizontal
        pyautogui.dragRel(0, 200, duration=2.5)  # Linha vertical
        pyautogui.dragRel(-200, 0, duration=2.5)  # Linha horizontal
        pyautogui.dragRel(0, -200, duration=2.5)  # Linha vertical

        time.sleep(1)  # Aguarda um segundo antes de prosseguir

        # Localiza a imagem do botão texto na tela
        posicao_centralizada_texto = pyautogui.locateOnScreen(imagem_texto, confidence=0.7)
        #posicao_texto = pyautogui.locateCenterOnScreen(imagem_texto, confidence=0.7)
        centro_botao_texto = pyautogui.center(posicao_centralizada_texto)
        pyautogui.click(centro_botao_texto)
        time.sleep(1)  # Aguarda um segundo antes de prosseguir

        # Adiciona um texto dentro do quadro desenhado
        pyautogui.moveRel(350, 60)  # Move o cursor para dentro do quadro
        pyautogui.dragRel(100, 30, duration=0.7)
        time.sleep(1)  # Aguarda um segundo antes de prosseguir
        pyautogui.typewrite("Codemaster!", interval=0.1)  # Digita o texto com intervalo entre as teclas
        time.sleep(1)  # Aguarda um segundo antes de prosseguir

        # Salvar a imagem e abrir no sistema operacional
        pyautogui.press('esc')
        pyautogui.hotkey('ctrl', 's')  # Atalho para salvar
        pyautogui.write('codemaster_paint.png')  # Nome do arquivo
        pyautogui.press('enter')  # Pressiona Enter para salvar
        time.sleep(2)  # Aguarda dois segundos antes de prosseguir
        pyautogui.press('enter')  # Seleciona opção de abrir a imagem salva

        # Fechar o Paint
        pyautogui.hotkey('alt', 'f4')  # Atalho para fechar a aplicação

    except pyautogui.ImageNotFoundException:
        print(f"Não foi possível localizar a imagem na tela.")

except pyautogui.FailSafeException:
    print("O programa foi interrompido pelo usuário.")