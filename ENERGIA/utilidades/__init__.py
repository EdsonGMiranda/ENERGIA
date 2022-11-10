
def moeda(n=0):
    return f'{n}'.replace('.', '')



def descompactarzip(lista, dire=''):
    import zipfile
    caminho_origem = caminho_destino = dire
    try:
        for arquivo in lista:
            zipfile.ZipFile(caminho_origem + arquivo[107:]).extractall(caminho_destino + arquivo[-15:-4])
    except Exception as erro:
        print(f'Erro! tivemos o erro {erro}')
        print(caminho_destino + arquivo[-25:])
    else:
        return True


def descompactarzip2(lista, dire=''):
    import zipfile
    caminho_origem = caminho_destino = dire
    try:
        for arquivo in lista:
            zipfile.ZipFile(caminho_origem + arquivo[109:]).extractall(caminho_destino + arquivo[-18:-4])
            print(caminho_destino + arquivo[-33:-4])
    except Exception as erro:
        print(f'Erro! tivemos o erro {erro}')
        print(caminho_destino + arquivo[-33:-4])
    else:
        return True
