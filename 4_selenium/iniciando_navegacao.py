from selenium import webdriver
import time

# Inicialização do WebDriver para o Chrome
# Poderia ser usado o webdriver.Firefox(), webdriver.Edge() ou webdriver.Safari()  
driver = webdriver.Chrome()

# Abrir uma página Web
driver.get('https://www.utfpr.edu.br/')

# Aguardar 3 segundos para que a página seja renderizada
time.sleep(3)

# Abrir outra página Web 
driver.get('https://www.python.org')

# Aguardar 3 segundos para que a página seja renderizada
time.sleep(3)

# Voltar para a página anterior
driver.back()

# Aguardar 3 segundos para que a página seja renderizada
time.sleep(3)

# Avançar para a página seguinte
driver.forward()

# Aguardar 3 segundos para que a página seja renderizada
time.sleep(3)

# Encerrar o navegador
driver.quit()

