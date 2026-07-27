# src/model/processador.py
import re
from bs4 import BeautifulSoup
import logging

class ProcessadorDados:
    def extrair_produtos(self, html_content: str, termo_busca: str):
        if not html_content:
            return []
            
        soup = BeautifulSoup(html_content, "html.parser")
        lista_produtos_processados = []
        
        # 1. Mapeia os contêineres padrão de produtos da VTEX (usados na galeria de busca)
        cards = soup.find_all(class_=lambda x: x and ('galleryItem' in x or 'productSummary' in x or 'product-summary' in x))
        
        # Fallback caso a estrutura de prateleira mude: busca links de produto com preço contido
        if not cards:
            cards = [a for a in soup.find_all('a', href=lambda x: x and ('/p' in x or '-p' in x)) if "R$" in a.get_text()]

        for card in cards:
            try:
                # 🎯 Busca o Nome do Produto: Procura por tags de título ou classes que contenham 'name', 'brand' ou 'title'
                nome_tag = card.find(class_=lambda x: x and ('productName' in x or 'brandName' in x or 'name' in x.lower()))
                if not nome_tag:
                    nome_tag = card.find(['h3', 'h2', 'span'])
                
                nome = nome_tag.get_text(strip=True) if nome_tag else ""
                
                # 🎯 Busca o Preço: Procura elementos com 'price' no nome da classe ou que contenham o símbolo 'R$'
                preco_tag = card.find(class_=lambda x: x and ('sellingPrice' in x or 'price' in x.lower() or 'integer' in x.lower()))
                if preco_tag:
                    preco = preco_tag.get_text(strip=True)
                else:
                    # Fallback via Regex no texto do card se não achar tag específica de preço
                    texto_completo = card.get_text(" ", strip=True)
                    match = re.search(r"R\$\s*\d+,\d{2}", texto_completo)
                    preco = match.group(0) if match else ""

                # Limpeza e validação de segurança
                if not nome or not preco or "R$" not in preco:
                    # Tentativa de resgate se o texto puro tiver padrão aceitável
                    texto_bruto = card.get_text(" ", strip=True)
                    if "R$" in texto_bruto and len(nome) < 3:
                        match_preco = re.search(r"R\$\s*\d+,\d{2}", texto_bruto)
                        if match_preco:
                            preco = match_preco.group(0)
                            nome = texto_bruto.split("R$")[0].strip()

                # Ignora blocos inválidos ou vazios
                if len(nome) < 4 or not preco:
                    continue

                lista_produtos_processados.append({
                    "termo": termo_busca,
                    "produto": nome,
                    "preco": preco
                })
                
            except Exception as e:
                logging.debug(f"Erro ao parsear bloco de produto individual: {e}")
                continue

        # Eliminar itens duplicados no mapeamento
        vistos = set()
        resultado_limpo = []
        for p in lista_produtos_processados:
            chave = (p['produto'].lower(), p['preco'])
            if chave not in vistos:
                vistos.add(chave)
                resultado_limpo.append(p)
                
        logging.info(f"✨ Processador: Encontrados {len(resultado_limpo)} produtos para o termo '{termo_busca}'")
        return resultado_limpo