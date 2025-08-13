from Conexion import *

class CClientes:
    def mostrarClientes():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            consulta = cone.cursor()
            consulta.execute("SELECT * FROM Usuarios;")
            miResultado = consulta.fetchall()
            cone.close()
            return miResultado
        except sqlite3.Error as error:
            print(f"Error al mostrar registros:{error}")

    def ingresarUsuario(nombres,apellidos,sexo,edad):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            consulta = cone.cursor()
            sql="INSERT INTO Usuarios values (null,?,?,?,?)"

            valores = (nombres,apellidos,sexo,edad)
            consulta.execute(sql,valores)
            cone.commit()
            print(consulta.rowcount,"Registro Ingresado")
            cone.close()
        except sqlite3.Error as error:
            print(f"Error al mostrar registros:{error}")

    def modificarUsuario(idUsuario,nombres,apellidos,sexo,edad):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            consulta = cone.cursor()
            sql="UPDATE Usuarios SET nombres= ?, apellidos= ? ,sexo= ?,edad= ? WHERE id=?"

            valores = (nombres,apellidos,sexo,edad,idUsuario)
            consulta.execute(sql,valores)
            cone.commit()
            print(consulta.rowcount,"Registro Ingresado")
            cone.close()
        except sqlite3.Error as error:
            print(f"Error al actualizar registros:{error}")

    def eliminarUsuario(idUsuario):

        try:
            cone = CConexion.ConexionBaseDeDatos()
            consulta = cone.cursor()
            sql="Delete FROM Usuarios WHERE id=?"

            valores = (idUsuario)
            consulta.execute(sql,valores)
            cone.commit()
            print(consulta.rowcount,"Registro Eliminado")
            cone.close()
        except sqlite3.Error as error:
            print(f"Error al actualizar registros:{error}")