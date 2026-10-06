# Documentação sobre a função usada para Windows: https://learn.microsoft.com/pt-br/windows/win32/api/winuser/nf-winuser-messageboxw
# Documentação sobre a função usada para Linux: https://man.archlinux.org/man/notify-send.1.en
# Documentação sobre a função usada para MacOS: https://ss64.com/mac/osascript.html e https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/DisplayNotifications.html

import platform

def notificar(mensagem, titulo="RPA bot"):
    sistema = platform.system()
    
    if sistema == "Windows":
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, mensagem, titulo, 0)
        
    elif sistema == "Linux":
        import subprocess
        subprocess.run(['notify-send', titulo, mensagem])
        
    elif sistema == "Darwin": 
        import subprocess
        subprocess.run(['osascript', '-e', f'display notification "{mensagem}" with title "{titulo}"'])

# Exemplo de notificação
notificar("Script finalizado com sucesso!")