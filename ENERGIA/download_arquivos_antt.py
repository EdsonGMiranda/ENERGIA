import urllib3 as ur
from bs4 import BeautifulSoup
import wget

url = 'https://dados.antt.gov.br/dataset/sistema-de-acompanhamento-do-desempenho-operacional-das-concessionarias-siade'
conexao = ur.PoolManager()
retorno = conexao.request('GET', url)
# print(retorno.data)

pagina = BeautifulSoup(retorno.data, "html.parser")

# print(pagina.prettify())

dado = []
for link in pagina.find_all('a', class_='resource-url-analytics'):
    dado.append(link.get('href'))

link.find(href=".csv")
# caminho_destino = 'C:\\Users\\Pichau\\Downloads\\FGVENERGIA\\'
caminho_destino = 'C://FGVENERGIA//ANTT//'
for item in dado:
    url_origem = item[:]
    wget.download(url_origem, caminho_destino)
# print(dado)
