
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
            zipfile.ZipFile(caminho_origem + arquivo[107:]).extractall(caminho_destino + arquivo[-21:])
    except Exception as erro:
        print(f'Erro! tivemos o erro {erro}')
        print(caminho_destino + arquivo[-21:-4])
    else:
        return True
