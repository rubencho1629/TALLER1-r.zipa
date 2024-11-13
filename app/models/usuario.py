from .. import db
from flask_login import UserMixin

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)

    # Relación con usuarios (un rol puede tener muchos usuarios)
    usuarios = db.relationship('Usuario', backref='role', lazy=True)

    def __repr__(self):
        return f"<Role(nombre={self.nombre})>"

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=True)  # Clave foránea al rol

    def __repr__(self):
        return f"<Usuario(username={self.username})>"
