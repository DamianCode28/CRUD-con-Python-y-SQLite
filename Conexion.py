import sqlite3

class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = sqlite3.connect("BDUsuarios.db")
            print("Conexion correcta")
            return conexion 
        except sqlite3.Error as error:
            print("Error en la conexion:"+ error)
            return None

CConexion.ConexionBaseDeDatos()