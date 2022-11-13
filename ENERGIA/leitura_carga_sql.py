import csv
import pyodbc


server = \\DENERGIA'
database = '_ENERGIA_DE'
username = '_ENERGIA_DE'
password = ''
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect(
    'DRIVER={SQL Server};SERVER=' + server + ';PORT=4513;DATABASE=' + database + ';ENCRYPT=no;UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

with open('C:\\FGVENERGIA\\ANTT\\producao_origem_destino_2022.csv', mode='r') as arq:
    leitor = csv.reader(arq, delimiter=';')
    linha = 0
    for pos, coluna in enumerate(leitor):
        if linha == 0:
            print(f'Colunas: {" ".join(coluna)}')
            linha += 1
        else:
            print('INSERT INTO antt.producao_origem_destino (mes_ano ,ferrovia ,mercadoria_antt ,'
                  'estacao_origem ,uf_origem,estacao_destino,uf_destino,tu ,tku)')
            print(f'\t VALUES (\'01/{coluna[0]}\', ', end='')
            print(f'\'{coluna[1]}\',', end='')
            print(f' \'{coluna[2]}\', ', end='')
            print(f'\'{coluna[3]}\', ', end='')
            print(f'\'{coluna[4]}\', ', end='')
            print(f'\'{coluna[5]}\', ', end='')
            print(f'\'{coluna[6]}\', ', end='')
            print(f'\'{coluna[7]}\','.replace('.', ''), end='')
            print(f'\'{coluna[8]}\')'.replace('.', ''))
            linha += 1



print(f'Imput {linha} no banco')
