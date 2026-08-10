import pyautogui
import time

pyautogui.FAILSAFE = True  # Ativa a função de segurança para evitar movimentos indesejados do mouse

try:
    largura, altura = pyautogui.size()
    print(f'Tamanho da tela: {largura}x{altura}')
    centro_x, centro_y = largura // 2, altura // 2
# ########
# # Mover
# ########
#     # Mover o mouse
#     pyautogui.moveTo(centro_x, centro_y, duration=1)

#     # Aguardar por 1 segundo para observar o movimento
#     time.sleep(1)

#     # Mover o mouse em relação à posição atual
#     pyautogui.move(100, 0, duration=1)  # Mover 100 pixels para a direita
#     time.sleep(1)
#     pyautogui.move(0, 100, duration=1)  # Mover 100 pixels para baixo
#     time.sleep(1)
#     pyautogui.move(-100, 0, duration=1)  # Mover 100 pixels para a esquerda
#     time.sleep(1)

    # ################
    # # CLIQUES
    # ################

    # # Posicionar o mouse em cima do terminal
    # pyautogui.moveTo(largura-146, 26)

    # # Clique com o botão esquerdo
    # pyautogui.click()
    # time.sleep(1)

    # # Posicionar e clique com o botão esquerdo
    # pyautogui.click(largura-146, 400)
    # time.sleep(1)

    # # Clique com o botão direito
    # pyautogui.rightClick(centro_x, centro_y)
    # time.sleep(1)

    # # clique com o botão esquerdo para retornar o foco no terminal
    # pyautogui.click(largura-635, 64)

    # # Clique duplo no texto do terminal
    # pyautogui.doubleClick()
    # time.sleep(1)

    # # Clique com o botão do meio do mouse
    # pyautogui.middleClick()
    # time.sleep(1)

    #############
    # ARRASTAR Drag and Drop
    #############

    # Posicionar no texto do terminal
    pyautogui.moveTo(largura-625, 64)

    # Arrastar para a direita até o final da largura
    # Parâmetro button pode ser 'left', 'right' ou 'middle'
    pyautogui.dragTo(largura, 64, duration=1, button='left')
    time.sleep(1)

    pyautogui.moveTo(largura-625, 64)
    # Arrastar por 200 pixels à direita e 50 pixels para baixo
    pyautogui.dragRel(200, 50, duration=0.5, button='left')


    # Arrastar o mouse
    pyautogui.moveTo(centro_x, centro_y)
    pyautogui.dragTo(centro_x + 100, centro_y + 100, duration=1)  # Arrastar para a direita e para baixo
    time.sleep(1)



except pyautogui.FailSafeException:
    print("\nMovimento do mouse interrompido pelo usuário.")
# clique duplo no texto do terminal