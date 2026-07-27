from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicialização do WebDriver para o Chrome
driver = webdriver.Chrome()

driver.get('https://www.python.org')
print(f'\nNavegando pela página {driver.title} na URL {driver.current_url}')

# Método find_element para retornar o primeiro elemento
# Poderia ser usado o By.ID, By.NAME, By.CLASS_NAME, By.TAG_NAME e By.LINK_TEXT
campo_busca = driver.find_element(By.ID, 'id-search-field')
print(f'\nTag e id do campo de busca: {campo_busca.tag_name} - {campo_busca.get_attribute('id')}')

# Método find_elements para retornar todos os elementos com a classe exata
widgets = driver.find_elements(By.CLASS_NAME, 'widget-title')
# Cada widget é um h2
print('\nSeções da página:')
for widget in widgets:
    titulo = widget.text
    print(f"   - {titulo}")

# Outros tipos de busca que são muito usadas é o CSS Selector e XPATH
# Mais informações sobre o CSS Selector: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Basic_selectors
# Mais informações sobre o XPATH: https://developer.mozilla.org/en-US/docs/Web/XML/XPath

# CSS Selector é uma busca mais flexível 
# Busca com CSS Selector por classe e tag 
itens_menu = driver.find_elements(By.CSS_SELECTOR, ".main-navigation li")
print(f'\nQuantidade de itens do menu: {len(itens_menu)}')

# Busca com CSS Selector por tag e atributo
link_download = driver.find_element(By.CSS_SELECTOR, "a[href='/downloads/']")
print(f'\nLink de {link_download.text}: {link_download.get_attribute('href')}')

# XPATH é uma linguagem usada para localizar nós em arquivos XML, mas que pode ser aplicada para HTML. 
# Permite realizar buscas relativas e aplicar operadores.
# Busca com XPATH por atributo parcial
campo_busca_XPATH = driver.find_element(By.XPATH, "//input[contains(translate(@placeholder, 'SEARCH', 'search'), 'search')]")
print(f'\nTag e id do campo com placeholder que contém o texto search: {campo_busca_XPATH.tag_name} - {campo_busca_XPATH.get_attribute('id')}')

time.sleep(3)

# Encerrar o navegador
driver.quit()