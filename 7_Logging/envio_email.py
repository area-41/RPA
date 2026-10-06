# Mais informações sobre o módulo smtplib: https://docs.python.org/3/library/smtplib.html
# Mais informações sobre o módulo email.message: https://docs.python.org/3/library/email.message.html
# Mais exemplos: https://docs.python.org/pt-br/dev/library/email.examples.html

import smtplib
from email.message import EmailMessage
import os
import time
from pathlib import Path

def enviar_email(assunto, corpo, destinatario, arquivo_anexo):
    # Configurações de exemplo com o Gmail
    email_origem = 'seuemail@gmail.com'
    senha = os.environ['SENHA_EMAIL_CODEMASTER']
    
    # Definição da mensagem de e-mail 
    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = email_origem
    msg['To'] = destinatario
    msg.set_content(corpo)
    
    # Anexar um arquivo
    path_arquivo = Path(arquivo_anexo)

    if path_arquivo.exists():
        with open(path_arquivo, 'rb') as arquivo:
            conteudo = arquivo.read()
            
            # Adicionar anexo
            msg.add_attachment(
                conteudo,
                maintype='application',
                subtype='octet-stream',
                filename=path_arquivo.name
            )
            print(f'Arquivo {path_arquivo.name} anexado.')
    else:
        print(f'Arquivo {path_arquivo.name} não encontrado e não anexado.')

    # Envio do e-mail de fato
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_origem, senha)
            smtp.send_message(msg)
        print('E-mail enviado!')
        return True
    except Exception as e:
        print(f"Erro ao enviar: {e}")
        return False

# Uso da função para o envio de e-mails 
enviar_email(
    'Relatório RPA com Anexo',
    f'Script finalizado em {time.ctime()}\n',
    'codemaster.rpa@gmail.com',
    'imagem_com_texto_por.png'
)