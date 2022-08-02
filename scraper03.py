# Missão: Pegar Modelo e Valor de Iphone do site da Kabum

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://lista.mercadolivre.com.br/iphone-x'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

page = requests.get(url, headers=header)


soup = BeautifulSoup(page.text, 'html.parser')

produtos = soup.find_all(
    'div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

modelo = []
valor = []
info = []


for i, produto in enumerate(produtos):
    modelo.append(produto.find(
        'h2', attrs={'class': 'ui-search-item__title'}).text)
    valor.append(produto.find('span', attrs={
                 'class': 'price-tag-text-sr-only'}).text)
    info.append([modelo[i], valor[i]])


df = pd.DataFrame(data=info, columns=['Modelo', 'Valor'])
print(df)

df.to_excel('iphone.xlsx', index=False)
