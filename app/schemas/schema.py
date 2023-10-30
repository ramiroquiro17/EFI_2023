from app import ma
from marshmallow import fields
from app.models.models import User
from app.models.models import Post
from app.models.models import Comment
from app.models.models import Category

class CommentSchema(ma.Schema):
    id = fields.Integer(dump_only=True) # Mostrar id del posteo
    content = fields.String() 
    post = fields.Integer()
    user = fields.Integer()

class PostSchema(ma.Schema):
    id = fields.Integer(dump_only=True) # Mostrar id del posteo
    title = fields.String() # 
    content = fields.String()
    user = fields.Integer()
    category = fields.Integer()

    # user_obj = fields.Nested(UserSchema, exclude=["id",])
    comments = fields.Nested(CommentSchema, many=True) # Muestra los comentarios de cada posteo almacenados en la tabla comment

class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True) # Mostrar id del usuario
    username = fields.String() # Convierte texto json en esquema
    first_name = fields.String()
    last_name = fields.String()
    posts = fields.Nested(PostSchema, many=True) # Muestra los post de cada usuario almacenados en la tabla post
    comments = fields.Nested(CommentSchema, many=True)

class CategorySchema(ma.Schema):
    id = fields.Integer(dump_only=True) # Mostrar id del posteo
    category = fields.String()
    posts = fields.Nested(PostSchema, many=True) # Muestra los post de cada usuario almacenados en la tabla post
