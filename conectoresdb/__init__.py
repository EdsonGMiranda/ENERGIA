def conectamysql(user, passwd, server, bd):
    """
    :param user: user to connect to database
    :param passwd:  password to connect to database
    :param server: server of mysql default port is 3306
    :param bd: database name
    :return:
    """
    import mysql.connector
    from mysql.connector import errorcode
    try:
        db_connection = mysql.connector.connect(host=server, user=user, password=passwd, database=bd, auth_plugin='mysql_native_password')
        print("Database connection made!")
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("User name or password is wrong")
        else:
            print(error)
    else:
        db_connection.close()


def conectasqlserver(SQLSERVER_USER, SQLSERVER_PASS, SQLSERVER_HOST, SQLSERVER_DB):
    '''

    :param SQLSERVER_USER: user to connect to database.
    :param SQLSERVER_PASS: password to connect to database.
    :param SQLSERVER_HOST: 'localhost\sqlexpress' # for a named instance.
    :param SQLSERVER_PORT: 'myserver,port' # to specify an alternate port.
    :param SQLSERVER_DB: Database name target.
    :return:
    '''
    import pyodbc
    server = SQLSERVER_HOST
    database = SQLSERVER_DB
    username = SQLSERVER_USER
    password = SQLSERVER_PASS
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';PORT=4513;DATABASE=' + database + ';ENCRYPT=no;UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    # cursor.execute("SELECT @@version;")
    # row = cursor.fetchone()
    # while row:
    #     print(row[0])
    #     row = cursor.fetchone()
    #
    # # Sample insert query
    # count = cursor.execute("""
    # INSERT INTO SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate)
    # VALUES (?,?,?,?,?)""",
    #                        'SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0, CURRENT_TIMESTAMP).rowcount
    # cnxn.commit()
    # print('Rows inserted: ' + str(count))