# monitor_cesta_basica/src/view/relatorio.py

class VisualizadorConsole:
    @staticmethod
    def mostrar_mensagem(mensagem: str):
        """Exibe uma mensagem informativa padrão no console."""
        print(f"[INFO] {mensagem}")

    @staticmethod
    def mostrar_erro(mensagem: str):
        """Exibe uma mensagem de erro destacada."""
        print(f"\n[ERRO] 🚨 {mensagem}\n")

    @staticmethod
    def mostrar_sucesso(total_itens: int, caminho_arquivo: str):
        """Exibe o sumário de sucesso após a conclusão do pipeline."""
        print("\n" + "="*60)
        print("🎉 EXECUÇÃO CONCLUÍDA COM SUCESESSO!")
        print(f"📦 Total de itens processados: {total_itens}")
        print(f"💾 Arquivo Parquet persistido em: {caminho_arquivo}")
        print("="*60 + "\n")