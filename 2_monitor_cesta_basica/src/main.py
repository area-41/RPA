import os
import sys

# Descobre o caminho da pasta raiz 'monitor_cesta_basica'
caminho_base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if caminho_base not in sys.path:
    sys.path.insert(0, caminho_base)

# Adiciona a pasta 'src' também para garantir
caminho_src = os.path.join(caminho_base, "src")
if caminho_src not in sys.path:  # <--- Corrigido aqui (com 'h')
    sys.path.insert(0, caminho_src)

import asyncio
from src.controller.monitor_controller import MonitorController

async def main():
    # Instancia o orquestrador do fluxo (Controller)
    controller = MonitorController()

    # Cenários de teste iniciais para o Condor (Curitiba e RMC)
    # Dica: Substitua pelas URLs de busca reais do e-commerce do Condor parametrizadas por filial/região
    # Exemplo de como devem ser montados os cenários na raiz da execução:
    cenarios_cesta_basica = [
        {
            "termo": "Feijão Preto 1kg",
            "regiao": "Curitiba - Juvevê",
            "url": "https://www.condor.com.br/"
        },
        {
            "termo": "Arroz Agulhinha 5kg",
            "regiao": "Curitiba - Juvevê",
            "url": "https://www.condor.com.br/"
        }
    ]

    # Executa a automação completa
    await controller.executar_monitoramento(cenarios_cesta_basica)

if __name__ == "__main__":
    # Garante o disparo correto do loop de eventos assíncronos do Playwright
    asyncio.run(main())