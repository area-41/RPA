import logging
from playwright.async_api import async_playwright

class ColetorScraper:
    async def buscar_dados_brutos(self, url: str, termo_busca: str, regiao: str) -> str:
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=["--disable-blink-features=AutomationControlled"]
            )
            
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                viewport={"width": 1366, "height": 768},
                locale="pt-BR"
            )
            page = await context.new_page()
            
            try:
                # 1. Acessa a Home (permitida pelo robots.txt)
                logging.info(f"Acessando página inicial para buscar: '{termo_busca}'...")
                await page.goto("https://www.condor.com.br/", timeout=40000, wait_until="domcontentloaded")
                
                # 2. Trata o banner de cookies se ele cobrir a tela
                try:
                    botao_cookie = page.get_by_role("button", name="Estou ciente")
                    if await botao_cookie.is_visible(timeout=3000):
                        await botao_cookie.click()
                        await page.wait_for_timeout(500)
                except Exception:
                    pass

                # 3. Localiza o input de busca (usando o placeholder visível no print: 'Leite, arroz, pão...')
                seletor_input = "input[placeholder*='Leite'], input[type='search'], .vtex-styleguide-9-x-input"
                campo_busca = page.locator(seletor_input).first
                
                await campo_busca.wait_for(state="visible", timeout=10000)
                await campo_busca.click()
                
                # Digita o termo de busca e dispara a tecla Enter
                await campo_busca.fill(termo_busca)
                await page.keyboard.press("Enter")
                
                logging.info(f"Busca submetida para '{termo_busca}'. Aguardando carregamento dos resultados...")
                
                # 4. Aguarda a injeção do texto de preços (R$) na vitrine renderizada
                try:
                    await page.wait_for_selector("text=R$", timeout=12000)
                    logging.info("🎯 Produtos e preços carregados com sucesso!")
                except Exception:
                    logging.warning("⚠️ Tempo limite para exibição dos preços atingido. Prosseguindo com o HTML atual.")

                # Scroll rápido para acionar lazy loading de imagens/valores
                await page.evaluate("window.scrollTo(0, 400);")
                await page.wait_for_timeout(1500)

                html_content = await page.content()
                return html_content
                
            except Exception as e:
                logging.error(f"Erro na navegação/busca por '{termo_busca}': {e}")
                return ""
            finally:
                if not page.is_closed():
                    await page.close()
                await browser.close()