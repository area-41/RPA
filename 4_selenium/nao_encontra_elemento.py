from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://google.com")

try:
    # Tenta encontrar o elemento na página
    botao = driver.find_element(By.ID, "botao-inexistente")
    botao.click()
except NoSuchElementException:
    print("⚠️ Elemento não encontrado! Executando plano de fundo/log...")


# Encerrar o navegador
driver.quit()