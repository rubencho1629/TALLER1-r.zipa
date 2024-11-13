from flask import render_template, request, jsonify
from .. import app, db
from ..models.models import Cuidador, Perro, Guarderia  # Asegúrate de que todos los modelos estén importados
from sqlalchemy.sql import text  # Asegúrate de importar text

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    # Contar perros llamados "Lassie"
    count_lassie = Perro.query.filter_by(Nombre='Lassie').count()
    return render_template('index.html', count_lassie=count_lassie)

@app.route('/perros/lassie', methods=['GET'])
def get_lassie():
    perros_lassie = Perro.query.filter_by(Nombre='Lassie').all()
    return render_template('lassie.html', perros=perros_lassie)

# Ruta para obtener todos los cuidadores
@app.route('/cuidadores', methods=['GET'])
def get_cuidadores():
    cuidadores = Cuidador.query.all()
    return render_template('cuidadores.html', cuidadores=cuidadores)

# Ruta para agregar un nuevo cuidador
@app.route('/cuidadores', methods=['POST'])
def add_cuidador():
    data = request.json
    new_cuidador = Cuidador(Nombre=data['Nombre'], Telefono=data['Telefono'])
    db.session.add(new_cuidador)
    db.session.commit()
    return jsonify({'ID': new_cuidador.ID}), 201

# Ruta para obtener todos los perros
@app.route('/perros', methods=['GET'])
def get_perros():
    perros = Perro.query.all()
    return jsonify([{'ID': p.ID, 'Nombre': p.Nombre, 'Raza': p.Raza, 'Edad': p.Edad, 'Peso': p.Peso} for p in perros])

# Ruta para agregar un nuevo perro
@app.route('/perros', methods=['POST'])
def add_perro():
    data = request.json
    new_perro = Perro(Nombre=data['Nombre'], Raza=data['Raza'], Edad=data['Edad'], Peso=data['Peso'])
    db.session.add(new_perro)
    db.session.commit()
    return jsonify({'ID': new_perro.ID}), 201

# Nueva ruta para obtener detalles de la guardería
@app.route('/guarderia/<nombre>', methods=['GET'])
def get_guarderia(nombre):
    # Realizar la consulta
    results = db.session.execute(text("""
        SELECT
            g.ID AS Guarderia_ID,
            g.Nombre AS Guarderia_Nombre,
            g.Direccion AS Guarderia_Direccion,
            g.Telefono AS Guarderia_Telefono,
            c.ID AS Cuidador_ID,
            c.Nombre AS Cuidador_Nombre,
            c.Telefono AS Cuidador_Telefono,
            p.ID AS Perro_ID,
            p.Nombre AS Perro_Nombre,
            p.Raza AS Perro_Raza,
            p.Edad AS Perro_Edad,
            p.Peso AS Perro_Peso
        FROM
            guarderias g
        LEFT JOIN
            cuidadores c ON g.ID = c.ID_GUARDERIA
        LEFT JOIN
            perros p ON g.ID = p.ID_GUARDERIA AND c.ID = p.ID_CUIDADOR
        WHERE
            g.Nombre = :nombre
    """), {'nombre': nombre}).fetchall()

    return render_template('guarderia.html', results=results)