import pdfplumber

with pdfplumber.open("documento_treinamento_rpa.pdf") as pdf:
    for pagina in pdf.pages:
        print(f"\nPágina {pagina.page_number} possui dimensões: {pagina.width} x {pagina.height}")
        pagina_texto = pagina.extract_text()
        # Extraindo o texto formatado como tabela
        tabelas = pagina.extract_tables()
        
        for i, tabela in enumerate(tabelas):
            print(f"\n--- Tabela {i+1} Encontrada ---")
            for linha in tabela:
                print(linha)