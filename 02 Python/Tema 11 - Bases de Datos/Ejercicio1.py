"""
 _______   _______
|  _____| |  ___  |
| |       | |   | |    Rolando Ramos Torres (@rolodoom)
| |       | |___| |    https://github.com/rolodoom
|_|       |_______|
 _         _______
| |       |  ___  |
| |       | |   | |    Sesion 11 - Bases de Datos
| |_____  | |___| |    Ejercicio 1
|_______| |_______|



En este ejercicio tendréis que crear una tabla llamada Alumnos
que constará de tres columnas: la columna id de tipo entero,
la columna nombre que será de tipo texto y la columna apellido
que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos,
como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno
por nombre y mostrar los datos por consola.
"""


# Importar Módulos
import sqlite3
from sqlite3 import Error

# Crear una Conexion
def crear_conexion(db_archivo):
    """
    Crear una conexion a SQLite
    especificada por db_archive
    :parametro db_archivo: archivo de la base de datos
    :return: Objeto de la conexión o None
    """

    conn = None
    try:
        conn = sqlite3.connect(db_archivo)
    except Error as e:
        print(e)

    return conn


# Buscar Alumno
def buscar_alumno(conn, nombre):
    """
    Buscar alumno
    :param conn:
    :param nombre:
    :return:
    """
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Alumnos WHERE Nombre = '{nombre}'")
    rows = cursor.fetchall()
    if len(rows) != 0:
        print(rows)
    else:
        print(f"El alumno {nombre} no está en la tabla!")

    return


# Crear el nuevo alumno
def crear_alumno(conn, tarea):
    """
    Crea un nuevo alumno
    :param conn:
    :param tarea:
    :return:
    """

    # Cadena de consulta
    query = """ INSERT INTO Alumnos(nombre,apellido) VALUES(?,?) """

    cursor = conn.cursor()
    cursor.execute(query, tarea)
    conn.commit()

    return cursor.lastrowid


# Crear la Tabla de Alumnos
def crear_tabla(conn):
    """
    Crea la tabla
    :param conn:
    :return:
    """
    query = "CREATE TABLE IF NOT EXISTS Alumnos(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, apellido TEXT NOT NULL)"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    return


# Subrutina Principal
def main():
    # Crear conexión a base de datos
    conn = crear_conexion("ej1.db")
    with conn:

        # Crear Tabla
        crear_tabla(conn)

        # Datos de Alumnos
        alumnos = [
            ("Maria", "Lopez"),
            ("Pedro", "Pérez"),
            ("Rosalinda", "Martí"),
            ("Iker", "León-Berenguer"),
            ("Severino", "Pablo-Marqués"),
            ("Flor", "Fonseca"),
            ("Hernando", "Portillo"),
            ("Urbano", "Camilo"),
            ("Maria", "Zamora"),
            ("Sol", "Aránzazu"),
            ("Jessica", "Valenciano"),
            ("Agustina", "Pedraza"),
            ("Maria", "Carrera"),
            ("Maricela", "Milla"),
        ]

        # Crear Alumnos
        for alumno in alumnos:
            crear_alumno(conn, alumno)

        # Buscar Almuno
        buscar_alumno(conn, "Sol")
        buscar_alumno(conn, "Maria")
        buscar_alumno(conn, "Jorge")

    # Cerrar conexion
    conn.close()


# Llamar Main
if __name__ == "__main__":
    main()
