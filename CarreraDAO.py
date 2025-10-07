from Carrera import Carrera

class CarreraDAO:
    def __init__(self, cursor, db):
        self.cursor = cursor
        self.db = db

    def insert(self, carrera):
        sql = "INSERT INTO carrera (nombre) VALUES (%s)"
        val = (carrera.get_nombre(),)
        self.cursor.execute(sql, val)
        self.db.commit()
        return carrera

    def see_all(self):
        self.cursor.execute("SELECT * FROM carrera")
        rows = self.cursor.fetchall()
        return [Carrera(nombre=row[1]) for row in rows]

    def update(self, carrera, nuevo_nombre):
        sql = "UPDATE carrera SET nombre = %s WHERE nombre = %s"
        val = (nuevo_nombre, carrera.get_nombre())
        self.cursor.execute(sql, val)
        self.db.commit()
        print(f"Carrera '{carrera.get_nombre()}' actualizada a '{nuevo_nombre}'.")
        carrera.set_nombre(nuevo_nombre)
        return carrera

    def delete(self, carrera):
        sql = "DELETE FROM carrera WHERE nombre = %s"
        val = (carrera.get_nombre(),)
        self.cursor.execute(sql, val)
        self.db.commit()
        return carrera