from selenium import webdriver
from selenium.webdriver.common.by import By 
import openpyxl

# acessar o site https://www.kabum.com.br/promocao/MENU_PCGAMER
driver = webdriver.Chrome()
driver.get('https://www.kabum.com.br/promocao/MENU_PCGAMER')

# extrair todos os títulos
titulos = driver.find_elements(By.XPATH,"//span[@class='sc-d79c9c3f-0 nlmfp sc-93fa31de-16 bBOYrL nameCard']")
#for titulo in titulos:
#    print(titulo.text)

# extrair todos os preços
precos = driver.find_elements(By.XPATH,"//span[@class='sc-6889e656-2 bYcXfg priceCard']")

# criando a planilha
workbook = openpyxl.Workbook()
#criando a página 'produtos'
workbook.create_sheet('produtos')
# Sleciono a página produtos
sheets_produtos = workbook['produtos']
sheets_produtos['A1'].value = 'Produto'
sheets_produtos['B1'].value = 'Preços'
workbook.save('produtos.xlsx')

# inserir os títulos e preços na planilha
for titulo, precos in zip(titulos, precos):
    sheets_produtos.append([titulo.text,precos.text])

workbook.save('produtos.xlsx')
