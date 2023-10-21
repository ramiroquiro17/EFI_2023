from app import db
from sqlalchemy import ForeignKey

# CREACION TABLA USUARIO
class User(db.Model):
    __tablename__ = 'User'
    id= db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique= True, nullable= False)
    password_hash = db.Column(db.String(300), unique = False, nullable= False)
    is_admin = db.Column(db.Boolean, default=False)

# CREACION TABLA PAIS
class Pais(db.Model):
    __tablename__ = 'pais'

    id = db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(100), nullable=False)

    def __str__(self):
        return self.name

# CREACION TABLA PROVINCIA
class Provincia(db.Model):
    __tablename__ = 'provincia'

    id = db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(100), nullable=False)
    pais= db.Column(
        db.Integer,
        ForeignKey('pais.id'),
        nullable= False
    )
    pais_obj = db.relationship('Pais')
    
    def __str__(self):
        return self.name

# CREACION TABLA LOCALIDAD
class Localidad(db.Model):
    __tablename__ = 'localidad'

    id= db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(100), nullable=False)
    provincia= db.Column(
        db.Integer,
        ForeignKey('provincia.id'),
        nullable= False
    )
    provincia_obj = db.relationship('Provincia')

    def __str__(self):
        return self.name

# CREACION TABLA PERSONA
class Persona(db.Model):
    __tablename__ = 'persona'

    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email= db.Column(db.String(100), nullable=False)
    telefono= db.Column(db.Integer, nullable=False)
    localidad= db.Column(db.Integer, 
                        ForeignKey('localidad.id'),
                        nullable=False
                        )
    domicilio= db.Column(db.String(100), nullable=False)
    f_nacimiento= db.Column(db.Date, nullable=False)
    activo= db.Column(db.Boolean, nullable=False, default=True)

    def __str__(self):
        return self.name
