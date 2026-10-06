# Módulo schedule pode ser instalado com pip install schedule
# Mais informações podem ser obtidas em https://schedule.readthedocs.io

import schedule
import time

# Função que será executada periodicamente
def funcao_rpa():
    print(f'Início da execução do script na hora certa! Data e hora agora: {time.ctime()}')
    

# Agendar para todo dia às 8h
schedule.every().day.at('08:00').do(funcao_rpa)

# A cada 30 minutos
schedule.every(30).minutes.do(funcao_rpa)

# A cada quarta-feira às 19:45
schedule.every().wednesday.at('19:45').do(funcao_rpa)

schedule.every().tuesday.at('21:55').do(funcao_rpa)

print('Agendador iniciado!')

try: 
    while True:
        # Verifica se existe alguma tarefa pendente. Se existir, executa imediatamente. 
        schedule.run_pending()
        # Verifica a cada 20 segundos
        time.sleep(20)
except KeyboardInterrupt:
    print('Finalizado!')