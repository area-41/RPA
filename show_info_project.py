import os
import pathlib
import sys
from importlib.metadata import distributions

def get_venv_size(output_filename="tamanho_dependencias.txt"):
    linhas_relatorio = []
    
    # Cabeçalho do relatório
    linhas_relatorio.append(f"{'Pacote':<30} | {'Versão':<10} | {'Tamanho em Disco':<15}")
    linhas_relatorio.append("-" * 62)
    
    total_env_size = 0
    
    # Lista todas as distribuições instaladas no ambiente virtual atual
    for dist in sorted(distributions(), key=lambda x: x.metadata['Name'].lower()):
        name = dist.metadata['Name']
        version = dist.metadata['Version']
        
        # Encontra os arquivos associados ao pacote para calcular o tamanho
        package_size = 0
        if dist.files:
            for file_ref in dist.files:
                abs_path = pathlib.Path(dist.locate_file(file_ref))
                if abs_path.exists() and (abs_file := abs_path.is_file()):
                    package_size += abs_path.stat().st_size
        
        total_env_size += package_size
        size_mb = package_size / (1024 * 1024)
        
        linhas_relatorio.append(f"{name:<30} | {version:<10} | {size_mb:>8.2f} MB")
        
    linhas_relatorio.append("-" * 62)
    linhas_relatorio.append(f"{'TAMANHO TOTAL DO AMBIENTE:':<43} {total_env_size / (1024 * 1024):>8.2f} MB")
    
    # Junta todas as linhas em um bloco de texto único
    conteudo_final = "\n".join(linhas_relatorio)
    
    # 1. Printa no terminal para visualização imediata
    print(conteudo_final)
    
    # 2. Salva no arquivo .txt especificado
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(conteudo_final)
        
    print(f"\n[Sucesso] Relatório salvo com sucesso em: {os.path.abspath(output_filename)}")

if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        print("Aviso: Você não parece estar com o .venv ativo. Ative-o antes de rodar.")
    get_venv_size()