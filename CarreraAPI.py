from flask import Flask, jsonify, request
from Carrera import Carrera
from CarreraDAO import CarreraDAO
from config import get_db_connection

try:
    db = get_db_connection()
    cursor = db.cursor()
    print("✅ Conexión exitosa a MySQL")
except Exception as e:
    print("❌ Error de conexión:", e)
    exit()

app = Flask(__name__)
dao = CarreraDAO(cursor, db)

@app.route('/carreras', methods=['GET'])
def get_carreras():
    carreras = dao.see_all()
    carreras_json = [
            {"nombre": c.get_nombre()} for c in carreras
    ]
    return jsonify(carreras_json)

@app.route('/carreras', methods=['POST'])
def add_carreras():
    data = request.json
    nueva_carrera = Carrera(data["nombre"])
    nueva_carrera_creada = dao.insert(nueva_carrera)
    return jsonify({'message': 'Carrera creada con el nombre: ' + nueva_carrera_creada.get_nombre()})

@app.route('/carreras', methods=['PATCH'])
def update_carreras():
    data = request.json
    nombre_actual = data.get("nombre_actual")
    nuevo_nombre = data.get("nuevo_nombre")
    if not nombre_actual or not nuevo_nombre:
        return jsonify({"error": "Faltan datos (nombre_actual o nuevo_nombre)."}), 400

    carrera = Carrera(nombre_actual)
    carrera_actualizada = dao.update(carrera, nuevo_nombre)
    return jsonify({"message": f" Carrera '{nombre_actual}' actualizada a '{carrera_actualizada.get_nombre()}'" })

@app.route('/carreras', methods=['DELETE'])
def delete_carreras():
    data = request.json
    nombre_actual = data.get("nombre_actual")
    if not nombre_actual:
        return jsonify({"error": "Faltan datos."}), 400

    carrera = Carrera(nombre_actual)
    carrera_actualizada = dao.delete(carrera)
    return jsonify({"message": f"Carrera '{nombre_actual}' borrada"})