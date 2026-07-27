from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicialização do WebDriver para o Chrome
driver = webdriver.Chrome()

# Acesso à página do Formulário
driver.get('https://httpbin.org/forms/post')

# Preencher o campo com nome 
campo_nome = driver.find_element(By.NAME, 'custname')
campo_nome.send_keys('João Silva')

# Preencher o campo com telefone
campo_telefone = driver.find_element(By.NAME, 'custtel')
campo_telefone.send_keys('0000-0000')

# Preencher o campo com email
campo_email = driver.find_element(By.NAME, 'custemail')
campo_email.send_keys('teste@teste.com')

# Preencher tamanho da pizza como radio buttons
campo_tamanho = driver.find_element(By.CSS_SELECTOR, "input[value='small']")
campo_tamanho.click()

# Toppings da pizza como checkboxes
toppings = ['bacon', 'mushroom']
for topping in toppings:
    campo_top = driver.find_element(By.CSS_SELECTOR, f"input[value='{topping}']")
    campo_top.click()

# Horário de entrega como input com max, min e steps
campo_horario = driver.find_element(By.NAME, 'delivery')
valor = '19:30'
driver.execute_script('arguments[0].value = arguments[1];', campo_horario, valor)

# Aguardar para visualizar o preenchimento
time.sleep(2)

# Submissão do formulário
botao = driver.find_element(By.TAG_NAME, 'button')
botao.click()

input('Aguardar uma entrada para encerrar!')

# Encerrar o navegador
driver.quit()