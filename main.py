from Carrera import Carrera
from CarreraDAO import CarreraDAO
import mysql.connector
import requests as req


def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Añadir  carrera")
        print("2. Actualizar carrera")
        print("3. Ver carreras")
        print("4. Borrar carrera")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Escribe el nombre para añadir carrera: ")
            print("Añadiendo carrera...")
            datos = {'nombre': nombre,}
            resp = req.post('http://localhost:5000/carreras', json=datos)
            print(resp.json()["message"])

        elif opcion == "2":
            print("Obteniendo carreras...")

            res = req.get("http://localhost:5000/carreras",)
            carreras = res.json()

            print("Carreras disponibles:")
            for i, c in enumerate(carreras):
                print(f'{i+1}. {c["nombre"]}')
            
            seleccion = int(input("Selecciona el número de la carrera a actualizar: "))
            if seleccion > len(carreras) or seleccion < 1:
                print("Numero invalido")
            else:
                carrera_seleccionada = carreras[seleccion - 1]
                nuevo_nombre = input("Escribe el nuevo nombre: ")
                datos = {
                    "nombre_actual": carrera_seleccionada["nombre"],
                    "nuevo_nombre": nuevo_nombre
                }
                resp = req.patch("http://localhost:5000/carreras", json=datos)
                print(resp.json()["message"])

        elif opcion == "3":
            print("Obteniendo carreras...")
            res = req.get("http://localhost:5000/carreras")
            carreras = res.json()

            for i, c in enumerate(carreras):
                print(f'{i+1}. {c["nombre"]}')

        elif opcion == "4":
            print("Obteniendo carreras...")

            res = req.get("http://localhost:5000/carreras",)
            carreras = res.json()

            print("Carreras disponibles:")
            for i, c in enumerate(carreras):
                print(f'{i+1}. {c["nombre"]}')
            
            seleccion = int(input("Selecciona el número de la carrera para borrar: "))
            if seleccion > len(carreras) or seleccion < 1:
                print("Numero invalido")
            else:
                carrera_seleccionada = carreras[seleccion - 1]
                datos = {
                    "nombre_actual": carrera_seleccionada["nombre"],
                }
                resp = req.delete("http://localhost:5000/carreras", json=datos)
                print(resp.json()["message"])
        
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
main()