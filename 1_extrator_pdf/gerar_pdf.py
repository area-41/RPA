import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def criar_pdf_treinamento(nome_arquivo):
    # Configuração do documento
    doc = SimpleDocTemplate(nome_arquivo, pagesize=letter,
                            rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    
    # Estilos
    styles = getSampleStyleSheet()
    
    titulo_style = ParagraphStyle(
        'TituloCustomizado',
        parent=styles['Heading1'],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1A365D'),
        spaceAfter=15
    )
    
    subtitulo_style = ParagraphStyle(
        'SubtituloCustomizado',
        parent=styles['Heading2'],
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#2C5282'),
        spaceBefore=15,
        spaceAfter=10
    )
    
    texto_style = ParagraphStyle(
        'TextoCustomizado',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        spaceAfter=8
    )

    # --- PÁGINA 1 ---
    story.append(Paragraph("RELATÓRIO AVANÇADO DE PROSPECÇÃO E VENDAS", titulo_style))
    story.append(Paragraph("Ambiente de Testes para Automação (RPA) - Data: 07/07/2026", texto_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("1. Lembretes Operacionais (Validação de Caracteres)", subtitulo_style))
    story.append(Paragraph("• Confirmar recebimento dos lotes de NF-e com o setor financeiro.", texto_style))
    story.append(Paragraph("• Verificar divergências no cálculo de ICMS/ST para produtos importados.", texto_style))
    story.append(Paragraph("• Enviar relatórios consolidados até as 18:00 (fuso horário de Brasília).", texto_style))
    
    # TABELA 1: Resumo Financeiro Mensal
    story.append(Paragraph("2. Tabela 1: Resumo Financeiro Mensal (Faturamento)", subtitulo_style))
    dados_t1 = [
        ['Mês', 'Faturamento Bruto', 'Impostos', 'Lucro Líquido'],
        ['Janeiro', 'R$ 145.000,00', 'R$ 21.750,00', 'R$ 123.250,00'],
        ['Fevereiro', 'R$ 162.300,00', 'R$ 24.345,00', 'R$ 137.955,00'],
        ['Março', 'R$ 158.900,00', 'R$ 23.835,00', 'R$ 135.065,00']
    ]
    t1 = Table(dados_t1, colWidths=[100, 140, 120, 140])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2B6CB0')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#EDF2F7')])
    ]))
    story.append(t1)
    story.append(Spacer(1, 15))

    # TABELA 2: Controle de Estoque Crítico
    story.append(Paragraph("3. Tabela 2: Itens de Hardware com Estoque Crítico", subtitulo_style))
    dados_t2 = [
        ['SKU', 'Componente', 'Qtd Atual', 'Mínimo', 'Fornecedor'],
        ['HD-SSD-512', 'SSD NVMe 512GB', '3 unidades', '15', 'TechDistribuidora'],
        ['MEM-DDR4-16', 'Memória RAM 16GB', '5 unidades', '20', 'GlobalImports'],
        ['FON-ATX-750', 'Fonte ATX 750W Gold', '2 unidades', '10', 'PowerSupply Co.']
    ]
    t2 = Table(dados_t2, colWidths=[90, 150, 70, 60, 130])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#C53030')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('ALIGN', (2,1), (3,-1), 'CENTER')
    ]))
    story.append(t2)
    
    # Quebra de página forçada para garantir a estrutura multi-página
    from reportlab.platypus import PageBreak
    story.append(PageBreak())

    # --- PÁGINA 2 ---
    story.append(Paragraph("DETALHAMENTO E CADASTROS ADICIONAIS", titulo_style))
    
    # TABELA 3: Cadastro de Clientes VIP
    story.append(Paragraph("4. Tabela 3: Leads e Clientes Corporativos (VIP)", subtitulo_style))
    dados_t3 = [
        ['ID', 'Empresa', 'Contato Principal', 'Telefone', 'Status'],
        ['901', 'Alpha Tecnologia', 'Roberto Souza', '(11) 98888-1111', 'Ativo'],
        ['902', 'Beta Alimentos', 'Carla Dias', '(21) 97777-2222', 'Em Negociação'],
        ['903', 'Gama Logística', 'Marcos Prado', '(31) 96666-3333', 'Inativo']
    ]
    t3 = Table(dados_t3, colWidths=[40, 140, 120, 110, 90])
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2D3748')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F7FAFC')])
    ]))
    story.append(t3)
    story.append(Spacer(1, 15))

    # TABELA 4: Logística de Entregas
    story.append(Paragraph("5. Tabela 4: Rastreamento de Encomendas Internacionais", subtitulo_style))
    dados_t4 = [
        ['Código Rastreio', 'Destino', 'Transportadora', 'Peso', 'Taxado'],
        ['BR-88271-X', 'Curitiba/PR', 'Correios Prio', '1.2 kg', 'Sim'],
        ['BR-11920-O', 'Campinas/SP', 'FedEx Express', '5.4 kg', 'Não'],
        ['BR-55362-A', 'Belo Horizonte/MG', 'DHL Global', '0.8 kg', 'Sim']
    ]
    t4 = Table(dados_t4, colWidths=[110, 110, 110, 70, 100])
    t4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#D69E2E')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.black),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ALIGN', (3,0), (-1,-1), 'CENTER')
    ]))
    story.append(t4)
    story.append(Spacer(1, 15))

    # TABELA 5: Licenciamento de Software
    story.append(Paragraph("6. Tabela 5: Renovação de Licenças de Software", subtitulo_style))
    dados_t5 = [
        ['Software', 'Chave/Licença', 'Vencimento', 'Custo Anual'],
        ['CloudSuite Pro', 'A92D-FFA1-9923', '15/12/2026', 'U$ 1,200.00'],
        ['SecureShield AI', 'BC81-3321-LL02', '30/01/2027', 'U$ 850.00']
    ]
    t5 = Table(dados_t5, colWidths=[120, 150, 100, 130])
    t5.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#4A5568')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ALIGN', (2,1), (-1,-1), 'CENTER')
    ]))
    story.append(t5)

    # Construir PDF
    doc.build(story)
    print(f"PDF '{nome_arquivo}' gerado com sucesso contendo 5 tabelas e 2 páginas!")

if __name__ == "__main__":
    criar_pdf_treinamento("documento_treinamento_rpa.pdf")