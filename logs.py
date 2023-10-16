# pip install PyMySQL
import pandas as pd
import pymysql
from datetime import datetime

#OBTENER EL NOMBRE DEL GANADOR (NO VA)
def get_name(winner, loser):
    host = 'localhost'
    port = 3306
    user = 'root'
    password = 'root' # PASSWORD QUE TENGÁIS

    connection = pymysql.connect(host=host,
                                port=port,
                                user=user,
                                password=password)

    cursor = connection.cursor()
    # AÑADIR NOMBRE DE LA BASE DE DATOS 
    cursor.execute("CREATE DATABASE IF NOT EXISTS historial")

    cursor.execute("USE historial")

    # AÑADIR VALORES
    table_query = """
    CREATE TABLE IF NOT EXISTS data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        winner VARCHAR(100) NOT NULL,

        date DATE NOT NULL

    );
    """

    cursor.execute(table_query)
    print("El ganador es:", winner)
    # Conectar a la base de datos y realizar la inserción
    #connection = pymysql.connect(host=host, port=port, user=user, password=password, db='historial')
    cursor = connection.cursor()

    # Insertar los datos en la base de datos
    insert_query = "INSERT INTO data (name, date) VALUES (%s, %s)"
    cursor.execute(insert_query, (winner, loser, datetime.now()))

    # Commit y cerrar la conexión
    connection.commit()
    cursor.close()
    connection.close()
