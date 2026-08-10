import pyautogui
import time

# Ativa o Fail-Safe para evitar movimentos indesejados do mouse
pyautogui.FAILSAFE = True

try:
    # Tirar uma captura de tela da tela inteira
    screenshot = pyautogui.screenshot()
    print("Captura de tela tirada com sucesso.\nTamanho da tela capturada:", screenshot.size)

    # Salvar a captura de tela em um arquivo
    arquivo_imagem = 'captura_tela.png'
    screenshot.save(arquivo_imagem)
    print(f"Captura de tela salva como '{arquivo_imagem}'.")

    time.sleep(2)  # Aguardar 2 segundos para o usuário ver a mensagem antes de abrir a imagem  

    # Tirar uma captura de tela de uma região específica (x=100, y=100, largura=300, altura=200)
    screenshot_regiao = pyautogui.screenshot(region=(100, 100, 300, 200))
    arquivo_regiao = 'captura_tela_regiao.png'
    screenshot_regiao.save(arquivo_regiao)
    print(f"Captura de tela da região específica salva como '{arquivo_regiao}'.")

except Exception as e:
    print(f"Ocorreu um erro ao capturar a tela: {e}")

except pyautogui.FailSafeException:
    print("Movimento do mouse detectado. A automação foi interrompida para evitar ações indesejadas.")
