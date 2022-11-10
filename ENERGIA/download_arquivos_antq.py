import urllib3 as ur
from bs4 import BeautifulSoup
import wget
from utilidades import *

url = 'https://dados.gov.br/dataset/movimentacao-carga'
conexao = ur.PoolManager()
retorno = conexao.request('GET', url)
# print(retorno.data)

pagina = BeautifulSoup(retorno.data, "html.parser")

# print(pagina.prettify())

dado = []
for link in pagina.find_all('a', class_='resource-url-analytics'):
    dado.append(link.get('href'))

link.find(href=".csv")
caminho_destino = 'C://FGVENERGIA//ANTQ//'
for item in dado:
    url_origem = item[56:]
    wget.download(url_origem, caminho_destino)

descompactarzip(dado, caminho_destino)

print(dado)

