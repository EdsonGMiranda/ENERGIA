# This is a sample Python script.
import conectoresdb
import mysql.connector
from mysql.connector import errorcode
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_hi('Edson')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#conectoresdb.conectamysql('edson_2', 'Oracle$22', '192.168.0.158', 'teste')

conectoresdb.conectasqlserver('FGV_ENERGIA_DE', 'teste123', 'SQLDC1VDH0003\\DENERGIA', 'FGV_ENERGIA_DE')


print_hi('Edson')