from .. import db

class Guarderia(db.Model):
    __tablename__ = 'guarderias'

    ID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Direccion = db.Column(db.String(255), nullable=False)
    Telefono = db.Column(db.String(15), nullable=True)

    # Si necesitas relaciones, puedes añadirlas aquí
    cuidadores = db.relationship('Cuidador', backref='guarderia', lazy=True)
    perros = db.relationship('Perro', backref='guarderia', lazy=True)

    def __repr__(self):
        return f'<Guarderia {self.Nombre}>'

class Cuidador(db.Model):
    __tablename__ = 'cuidadores'

    ID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Telefono = db.Column(db.String(15), nullable=True)
    ID_GUARDERIA = db.Column(db.Integer, db.ForeignKey('guarderias.ID'), nullable=True)

    def __repr__(self):
        return f'<Cuidador {self.Nombre}>'

class Perro(db.Model):
    __tablename__ = 'perros'

    ID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Raza = db.Column(db.String(50), nullable=True)
    Edad = db.Column(db.Integer, nullable=True)
    Peso = db.Column(db.Float, nullable=True)
    ID_GUARDERIA = db.Column(db.Integer, db.ForeignKey('guarderias.ID'), nullable=True)
    ID_CUIDADOR = db.Column(db.Integer, db.ForeignKey('cuidadores.ID'), nullable=True)

    def __repr__(self):
        return f'<Perro {self.Nombre}>'

