# pip install PyMySQL
import pandas as pd
import pymysql
from datetime import datetime

# Parámetros de conexión
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
    name VARCHAR(100) NOT NULL,
    victory BOOLEAN,
    date DATE NOT NULL,
  
);
"""

cursor.execute(table_query)

def generate_data():
    # name = # DEBEMOS SACAR DEL MAIN
    # victory = # DEBEMOS SACAR DEL MAIN
    fecha = datetime.now()
    
    return fecha #, name, victory

def insert_random_data():
    data = generate_data()
    insert_query = """
    INSERT INTO data (fecha, num_estacion, precipitacion, temperatura, humedad)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, data)

connection.commit()
insert_random_data()
cursor.close()
connection.close()
