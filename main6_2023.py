# ___________ FILE __________________
# con la keyword "with" chiudiamo in automatico il file dopo che abbiamo svolto le nostre operazioni,
# in questo modo non dobbiamo fare la close()
# attenzione al percorso /, //, \.

with open('C:/Users/Giaco/Desktop/ddd.txt', "w", encoding="utf-8") as f:
    f.write("this is a test")

open('C:/Users/Giaco/Desktop/ddd.txt', "x")
with open('C:/Users/Giaco/Documenti/ddd.txt', "w", encoding="utf-8") as f:
    f.write("this is a test")

# codice che consente di ottenere il percorso attuale, indipendente dal PC dove viene eseguito
import pathlib
percorso_attuale = pathlib.Path("ddd.txt").parent.resolve()
print(percorso_attuale)


















# ___________________prossimamente! _________
"""
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

"""