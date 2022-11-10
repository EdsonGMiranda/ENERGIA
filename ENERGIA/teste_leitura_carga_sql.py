import csv
import pyodbc
from utilidades import *


server = 'SQLDC1VDH0003\\DENERGIA'
database = 'FGV_ENERGIA_DE'
username = 'FGV_ENERGIA_DE'
password = 'teste123'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify
# ENCRYPT=yes on the client side to avoid MITM attacks.
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
            count = cursor.execute(f"""INSERT INTO antt.producao_origem_destino (mes_ano ,ferrovia ,mercadoria_antt ,estacao_origem ,uf_origem,estacao_destino,uf_destino,tu ,tku) VALUES (\'01/{coluna[0]}\',
            \'{coluna[1]}\',
            \'{coluna[2]}\', 
            \'{coluna[3]}\', 
            \'{coluna[4]}\', 
            \'{coluna[5]}\', 
            \'{coluna[6]}\', 
            \'{moeda(coluna[7])}\',
            \'{moeda(coluna[8])}\')""").rowcount
            cnxn.commit()
            linha += 1


print('Rows inserted: ' + str(count))
print(f'Imput {linha} no banco')
