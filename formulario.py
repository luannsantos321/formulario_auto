from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
import pandas as pd

#aparelhos

sheets = pd.read_csv('https://docs.google.com/spreadsheets/d/1RLxskHG3J8ou-pQz3BkZ4d82KbPeNzTDWoxEujquUAk/export?format=csv')

for i,aparelho in enumerate(sheets.iloc[0:, 0]):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    web = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    web.get('https://docs.google.com/forms/u/0/d/e/1FAIpQLSeNtAq2pJoDqOm4nyvEHdyS1EPKXqYpuPK2UV1iEwlcio94vQ/formResponse')

    form = web.find_element(By.TAG_NAME, 'form')
    spans2 = form.find_elements(By.TAG_NAME, 'span')
    dic1 = dict({span.text: span for span in spans2})
    dic1['TESTE NIVEL 1'].click()
    dic1['TELEFONE'].click()
    dic1['LUANN RODRIGO'].click()
    dic1['Próxima'].click()
    sleep(1)

    form = web.find_element(By.TAG_NAME, 'form')
    spans = form.find_elements(By.TAG_NAME, 'span')
    texto = form.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    dic2 = dict({span.text: span for span in spans})
    #print(dic2.keys())
    num = dic2['NUMERO DE SÉRIE']
    texto.click()
    texto.send_keys(aparelho)
    dic2['SEM DEFEITOS'].click()
    dic2['TELEFONE - NENHUM REPARO'].click()
    #dic2[''].click()
    dic2['Próxima'].click()
    sleep(1)

    final = {
        'RECUPERADO NIVEL 1': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span',
        'EQUIPAMENTO NIVEL 2':'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[2]/div/span'
             }
    rec = web.find_element(By.XPATH,final['RECUPERADO NIVEL 1']).click()
    enviar = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()
    print(aparelho)
    i += 1
    print(i)
   
    
    web.close()
print('*'* 25,'FIM','*'* 25)
