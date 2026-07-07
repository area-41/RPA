import pdfplumber

with pdfplumber.open("exemplo_aula.pdf") as pdf:
    primeira_pagina = pdf.pages[0]
    
    # Extraindo o texto formatado como tabela
    tabelas = primeira_pagina.extract_tables()
    
    for i, tabela in enumerate(tabelas):
        print(f"\n--- Tabela {i+1} Encontrada ---")
        for linha in tabela:
            print(linha)