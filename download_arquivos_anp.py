import urllib3 as ur
from bs4 import BeautifulSoup
import wget
from utilidades import *


url = 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-abertos-movimentacao-de-derivados-de-petroleo'
conexao = ur.PoolManager()
retorno = conexao.request('GET', url)
#print(retorno.data)

pagina = BeautifulSoup(retorno.data, "html.parser")

#print(pagina.prettify())

dado = []

for link in pagina.find_all('a', class_='internal-link'):
    dado.append(link.get('href'))

link.find(href=".csv")
# caminho_destino = 'C:\\Users\\Pichau\\Downloads\\FGVENERGIA\\'
caminho_destino = 'C://Users//Pichau//Downloads//FGVENERGIA//ANTT//'
for item in dado:
    url_origem = item[:]
    wget.download(url_origem, caminho_destino)


descompactarzip2(dado, caminho_destino)
#print(dado)

