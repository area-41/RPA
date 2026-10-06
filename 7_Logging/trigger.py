# Módulo watchdog pode ser instalado com pip install watchdog
# Mais informações podem ser obtidas em https://python-watchdog.readthedocs.io

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Classe com o processamento que deve ser realizado no diretório
class RPAHandler(FileSystemEventHandler):

    # Evento que irá disparar o processamento
    # Também poderia definir como on_deleted ou on_moved
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.txt'):
            print(f'Novo arquivo de texto adicionado: {event.src_path}')
            processar_arquivo(event.src_path)

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('.txt'):
            print(f'Arquivo {event.src_path} modificado.')

def processar_arquivo(caminho):
    print(f'Processando: {caminho}')
    with open(caminho, 'a+') as arquivo:
        arquivo.seek(0)
        texto = arquivo.read()
        print(texto)
        arquivo.write('Adicionando novos dados.\n')


# Monitorar diretório
observer = Observer()
diretorio = "./Dados/"
observer.schedule(RPAHandler(), diretorio, recursive=False)
observer.start()
print(f'Monitorando diretorio: {diretorio}')

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Sinaliza a thread para encerrar sua execução
    observer.stop()
# Aguarda a thread finalizar 
observer.join()