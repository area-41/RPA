import pyautogui
import time
import shutil
import subprocess
import sys

# Ativa o Fail-Safe para evitar movimentos indesejados do mouse
pyautogui.FAILSAFE = True

try:
    pyautogui.alert("A automação vai começar. Por favor, não mova o mouse ou pressione teclas durante a execução.")

    # Abre o editor de texto de acordo com o sistema operacional
    if sys.platform == 'win32' or sys.platform == 'win64':
        subprocess.Popen(['notepad.exe'])
    elif sys.platform == 'darwin':
        subprocess.Popen(['open', '-n', '-e'])
    else:
        editores = ['gedit', 'gnome-text-editor', 'kate', 'xed', 'mousepad']
        for editor in editores:
            # verifica se o comando existe no sistema
            if shutil.which(editor):
                subprocess.Popen([editor])
                break
        print("Sistema operacional não suportado.")
        sys.exit(1)

    # Aguardar 2 segundos para o editor abrir
    time.sleep(2)

    # Digitar o texto no editor
    pyautogui.write('Este texto esta sendo escrito por uma solucao RPA', interval=0.1)

    # Pressionar a tecla Enter para criar uma nova linha
    pyautogui.press('enter')
    pyautogui.write('Automacao com PyAutoGUI!', interval=0.2)
    time.sleep(1)

    # Selecionar todo o texto usando Ctrl+A (ou Command+A no macOS)
    pyautogui.hotkey('ctrl', 'a') if sys.platform != 'darwin' else pyautogui.hotkey('command', 'a')

    # Copiar o texto selecionado usando Ctrl+C (ou Command+C no macOS)
    pyautogui.hotkey('ctrl', 'c') if sys.platform != 'darwin' else pyautogui.hotkey('command', 'c')

    time.sleep(1)

    # Pressionar para baixo e Enter 2 vezes
    pyautogui.press(['down', 'enter', 'enter'])

    time.sleep(1)

    # Colar o texto copiado usando Ctrl+V (ou Command+V no macOS)
    pyautogui.hotkey('ctrl', 'v') if sys.platform != 'darwin' else pyautogui.hotkey('command', 'v')
    
    # Todas as teclas que podem ser pressionadas usando o método press() ou hotkey()
    print("Teclas disponíveis para pressionar:", pyautogui.KEYBOARD_KEYS)
    pyautogui.write('Teclas disponíveis para pressionar: ' + str(pyautogui.KEYBOARD_KEYS))
    time.sleep(5)  # Aguardar 5 segundos para o usuário ver a mensagem antes de fechar o editor
    pyautogui.alert("Automação concluída! O texto foi escrito e copiado com sucesso.\nPode fechar o editor de texto agora.")

    
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    sys.exit(1)