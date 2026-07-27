import logging
import os
import asyncio
from datetime import date
import polars as pl

from src.model.coletor import ColetorScraper
from src.model.processador import ProcessadorDados
from src.view.relatorio import VisualizadorConsole

class MonitorController:
    def __init__(self):
        self.scraper = ColetorScraper()
        self.processador = ProcessadorDados()
        self.view = VisualizadorConsole()
        self.pasta_destino = "dados_coletados"

    async def executar_monitoramento(self, cenarios_busca: list[dict]):
        """
        Orquestra o fluxo completo do RPA.
        Recebe uma lista de dicionários contendo os alvos de busca e regiões.
        """
        self.view.mostrar_mensagem("🚀 Iniciando o monitoramento de preços da Cesta Básica (Curitiba/RMC)...")
        
        todas_coletas_brutas = []
        
        # Iterando pelos cenários configurados (supermercado, termo, região)
        for cenario in cenarios_busca:
            termo = cenario["termo"]
            regiao = cenario["regiao"]
            url = cenario["url"]
            
            self.view.mostrar_mensagem(f"🔍 Buscando '{termo}' na região [{regiao}]...")
            
            # 1. Aciona a coleta bruta (Model)
            dados_crus = await self.scraper.buscar_dados_brutos(url=url, termo_busca=termo, regiao=regiao)
            
            # Trata possíveis erros retornados pelo scraper antes de concatenar
            if dados_crus and "erro" not in dados_crus[0]:
                # No monitor_controller.py, após chamar o processador:
                produtos_encontrados = self.processador.extrair_produtos(dados_crus, termo)
                logging.info(f"✅ Sucesso: {len(produtos_encontrados)} itens encontrados para '{termo}'.")
            else:
                erro_msg = dados_crus[0]["erro"] if dados_crus else "Nenhum dado retornado."
                self.view.mostrar_erro(f"❌ Falha ao coletar '{termo}' em [{regiao}]: {erro_msg}")
            
            # Pausa educada entre requisições para evitar bloqueios de IP
            await asyncio.sleep(2)

        # 2. Processamento e Salvamento dos dados (Model)
        if todas_coletas_brutas:
            self.view.mostrar_mensagem("🧹 Aplicando pipeline de limpeza com Polars...")
            
            # Limpa as strings e converte os preços usando o processador
            df_limpo = self.processador.limpar_precos(todas_coletas_brutas)
            
            if not df_limpo.is_empty():
                os.makedirs(self.pasta_destino, exist_ok=True)
                
                # Nomeando o arquivo com a data atual da coleta
                data_hoje = date.today().isoformat()
                caminho_parquet = os.path.join(self.pasta_destino, f"cesta_basica_{data_hoje}.parquet")
                
                # Salva os dados de forma otimizada em Parquet
                df_limpo.write_parquet(caminho_parquet)
                
                # 3. Exibe o resultado na interface (View)
                self.view.mostrar_sucesso(total_itens=len(df_limpo), caminho_arquivo=caminho_parquet)
                
                # Mostra uma prévia dos dados mais baratos encontrados para validar
                print("\n📊 Prévia dos top 3 itens mais em conta coletados:")
                print(df_limpo.sort("preco_formatado").head(3))
            else:
                self.view.mostrar_erro("❌ O DataFrame final ficou vazio após o processamento.")
        else:
            self.view.mostrar_erro("⚠️ Nenhuma informação foi coletada no bloco atual. Operação abortada.")