import pyautogui
import time

try:
    print("Pressione Ctrl+C para encerrar o programa.")
    while True:
        x, y = pyautogui.position()
        print(f'Posição do mouse: ({x}, {y})', end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nPrograma encerrado.")