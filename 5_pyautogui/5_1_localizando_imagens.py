import pyautogui
import time
import webbrowser
import os

pyautogui.FAILSAFE = True

try:
    url = "https://jspaint.app/"
    webbrowser.open(url)
    time.sleep(5)

    # 1. Seleciona a ferramenta Pincel
    pyautogui.click(43, 193)
    time.sleep(1)

    # 2. Desenho do Quadrado Contínuo
    # Clica e segura no ponto inicial
    x_inicio, y_inicio = 400, 300
    pyautogui.moveTo(x_inicio, y_inicio)
    
    # Desenha as 4 linhas sequenciais sem soltar o ponteiro nos cantos
    pyautogui.dragTo(x_inicio + 200, y_inicio, duration=0.4, button='left')
    pyautogui.dragTo(x_inicio + 200, y_inicio + 200, duration=0.4, button='left')
    pyautogui.dragTo(x_inicio, y_inicio + 200, duration=0.4, button='left')
    pyautogui.dragTo(x_inicio, y_inicio, duration=0.4, button='left')

    time.sleep(1)

    # 3. Seleciona a ferramenta Texto
    pyautogui.click(43, 216)
    time.sleep(1)

    # 4. Criar caixa de texto dentro do quadrado e digitar
    pyautogui.moveTo(x_inicio + 40, y_inicio + 80)
    pyautogui.dragRel(120, 40, duration=0.5, button='left')
    time.sleep(0.5)

    # Clique dentro da caixa de texto criada para garantir o foco
    pyautogui.click(x_inicio + 50, y_inicio + 90)
    time.sleep(0.5)
    
    # Escreve a mensagem
    pyautogui.write("Codemaster!", interval=0.1)
    time.sleep(1)

    # Finaliza a edição de texto clicando fora da caixa
    pyautogui.click(x_inicio + 10, y_inicio + 10)
    time.sleep(1)

    # 5. Salvamento correto em PNG via Menu File -> Save
    # Clica no menu 'File' no canto superior esquerdo
    pyautogui.click(15, 60)
    time.sleep(0.5)
    
    # Pressiona a tecla 's' para acionar 'Save' no menu
    pyautogui.press('s')
    time.sleep(2)  # Aguarda a caixa do Windows "Salvar como" abrir

    # Digita o nome completo com caminho ou nome direto
    pyautogui.write('codemaster_paint.png', interval=0.05)
    time.sleep(1)
    pyautogui.press('enter')

    print("Desenho concluído e salvo com sucesso!")

except pyautogui.FailSafeException:
    print("Execução interrompida pelo usuário.")