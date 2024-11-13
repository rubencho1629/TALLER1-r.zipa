from flask import request, jsonify
from .. import db,app
from ..models.usuario  import Usuario

# Ruta para obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{'id': u.id, 'username': u.username} for u in usuarios])

# Ruta para crear un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    nuevo_usuario = Usuario(username=data['username'], password=data['password'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'id': nuevo_usuario.id, 'username': nuevo_usuario.username}), 201

# Ruta para obtener un usuario específico por ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    return jsonify({'id': usuario.id, 'username': usuario.username})

# Ruta para eliminar un usuario
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'message': 'Usuario eliminado'})
