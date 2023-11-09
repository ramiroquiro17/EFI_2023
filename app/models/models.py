from app import db # Importo de app.py donde ya está establecida la variable db
from sqlalchemy import ForeignKey

from datetime import datetime

class User(db.Model): # Crear tabla
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True) # primary_key (hacer que el id sea autoincremental y única)
    username = db.Column(db.String(50), unique=True, nullable=False) # Más columnas
    first_name = db.Column(db.String(50), unique=False, nullable=False) # unique (no permite que se vuelva a repetir la misma información)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    post = db.relationship('Post')
    comment = db.relationship('Comment')

class Category(db.Model): 
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(200))
    post = db.relationship('Post')

class Post(db.Model): 
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(200))
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    user = db.Column(
        db.Integer,
        ForeignKey('user.id'),
        nullable=False,
    ) # Columna que relaciona la tabla post con la tabla user
    category = db.Column(
        db.Integer,
        ForeignKey('category.id'),
        nullable=False,
    )# Columna que relaciona la tabla post con la tabla category
    user_obj = db.relationship('User') # Recibe la clase con la que se relacionará esta tabla
    comment = db.relationship('Comment')
    category_obj = db.relationship("Category")
    
class Comment(db.Model): 
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    post = db.Column(
        db.Integer,
        ForeignKey('post.id'),
        nullable=False,
    ) # Columna que relaciona la tabla post con la tabla user
    user = db.Column(
        db.Integer,
        ForeignKey('user.id'),
        nullable=False,
    ) # Columna que relaciona la tabla post con la tabla user
    post_obj = db.relationship('Post')
    user_obj = db.relationship('User')

    # username = fields.Method("get_username")
    # first_name = fields.Method("get_first_name")    

    # def get_username(self, obj):
    #     user = User.query.filter(id=obj.user).first
    #     return user.username
    
    # def get_firt_name(self, obj):
    #     user = User.query.filter_by(id=obj.user).first
    #     return user.first_name

