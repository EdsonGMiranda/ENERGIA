def pega_arquivo(url_, dir_):

    import urllib3 as ur
    from bs4 import BeautifulSoup
    import wget

    #url = 'https://dados.antt.gov.br/dataset/sistema-de-acompanhamento-do-desempenho-operacional-das-concessionarias-siade'
    url = str(url_)
    conexao = ur.PoolManager()
    retorno = conexao.request('GET', url)
    #print(retorno.data)

    pagina = BeautifulSoup(retorno.data, "html.parser")

    #print(pagina.prettify())

    dado = []
    for link in pagina.find_all('a', class_='resource-url-analytics'):
        dado.append(link.get('href'))

    link.find(href=".csv")
    caminho_destino = dir_
    #caminho_destino = 'C://Users//Pichau//Downloads//FGVENERGIA//ANTT//'
    for item in dado:
        #url_origem = item[:]
        url_origem = item[45:67]
        wget.download(url_origem, caminho_destino)

    print(dado)

#pega_arquivo('https://dados.antt.gov.br/dataset/sistema-de-acompanhamento-do-desempenho-operacional-das-concessionarias-siade' , 'C://Users//Pichau//Downloads//FGVENERGIA//ANTT//')

pega_arquivo('https://dados.gov.br/dataset/movimentacao-carga','C://Users//Pichau//Downloads//FGVENERGIA//ANTQ//')