# Se generan todas las rutas o endpoints

from flask import (
    jsonify,
    render_template,
    request,
)

from app import app # Llamar la variable app del init desde la carpeta
from app import db

from app.models.models import (
    User,
    Post,
    Comment,
    Category,
) # Importamos las tablas generadas en models

from app.schemas.schema import (
    PostSchema,
    UserSchema,
    CommentSchema,
    CategorySchema
)

from flask.views import MethodView

from datetime import datetime

@app.route('/') # Generar ruta
def index():
    return render_template("index.html") 

@app.route('/user', methods=['POST', 'GET']) # Métodos para poder ingresar o ver datos de la base de datos
def users():
    if request.method == 'POST': # método para ingresar datos
        data = request.get_json() # get_json (convierte la información en formato JSON)
        username = data.get('username') # Le agrego una variable a lo ingresado en el json de postman
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        new_user = User( 
            username = username, # especifico la variable creada anteriormente que quiero ingresar a la base de datos.
            first_name = first_name,
            last_name = last_name,
        )

        db.session.add(new_user) # Agregar a la base de datos
        db.session.commit() # Confirmar cambios

        return jsonify(Mensaje=f"Se creó el usuario {username}") # Mensaje que verifica que todo se realizó correctamente.

    if request.method == 'GET': # Si se busca ver datos
        users = User.query.all() # Contiene todos los datos de una tabla
        users_schema = UserSchema().dump(users, many=True) # Traer todos los usuarios de la base de datos en forma de lista.
        return jsonify(users_schema)
    

@app.route('/post', methods=['POST', 'GET'])
def posts():
    if request.method == 'POST': # método para ingresar datos
        data = request.get_json()
        title = data.get("title")
        content = data.get("content")
        user = data.get("user_id")
        category = data.get("category_id")

        new_post = Post(
            title = title,
            content = content,
            fecha_creacion = datetime.now(),
            user = user,
            category = category
        )

        db.session.add(new_post)
        db.session.commit()
        return jsonify(Mensaje = "Nuevo post creado") # Ingreso datos a la base de datos desde el thunder

    if request.method == 'GET': # Si se busca ver datos
        posts = Post.query.all()
        posts_schema = PostSchema().dump(posts, many=True) # Muestra todas las columnas de la tabla post.
        return jsonify(posts_schema)
    
@app.route('/user/<id_user>', methods=['PUT', 'DELETE', 'PATCH', 'GET'])
def users_by_id(id_user):
    if request.method == 'GET':
        # Muestra un usuario específico con su id
        user = User.query.get(id_user)  
        # Convierto en esquema
        user_schema = UserSchema().dump(user)
        return jsonify(user_schema)

    if request.method == 'DELETE':
        # Busco usuario
        user = User.query.get(id_user)
        # Elimino usuario
        db.session.delete(user)
        db.session.commit()
        return jsonify(Mensaje=f'User {id_user} eliminado')

    if request.method == 'PUT':
        # Busco usuario para modificar
        user = User.query.get(id_user)
        # Datos para modificar
        data = request.get_json()
        nuevo_nombre = data.get('username')

        user.username = nuevo_nombre
        db.session.commit()

        user_schema = UserSchema().dump(user)
        return jsonify(user_schema)

    if request.method == 'PATCH':
        return jsonify(Mensaje=f'Recibi un GET')

    return jsonify(Mensaje=f'Recibi el usuario {id_user}')

@app.route('/comment', methods=['POST', 'GET'])
def comment():
    if request.method == 'POST': # método para ingresar datos
        data = request.get_json()
        content = data.get("content")
        post = data.get("post_id")
        user = data.get("user_id")

        new_comment = Comment(
            content = content,
            fecha_creacion = datetime.now(),
            post = post,
            user = user
        )

        db.session.add(new_comment)
        db.session.commit()
        return jsonify(Mensaje = "Nuevo comentario") # Verifico que se ingresaron datos a la base de datos

    if request.method == 'GET': # Si se busca ver datos
        comments = Comment.query.all()
        comment_schema = CommentSchema().dump(comments, many=True) # Muestra todas las columnas de la tabla post.
        return jsonify(comment_schema)

@app.route('/categories', methods=['POST', 'GET'])
def categories():
    if request.method == 'POST': # método para ingresar datos
        data = request.get_json()
        category = data.get("category")

        new_category = Category(
            category = category,
        )

        db.session.add(new_category)
        db.session.commit()
        return jsonify(Mensaje = "Nueva categoría creada") # Ingreso datos a la base de datos desde el thunder

    if request.method == 'GET': # Si se busca ver datos
        categories = Category.query.all()
        categories_schema = CategorySchema().dump(categories, many=True) # Muestra todas las columnas de la tabla post.
        return jsonify(categories_schema)


###
""" 
class UserApi(MethodView):
    def get(self, user_id=None):
        if user_id in None:
            users = User.query.all()
            user_schema = UserSchema().dump(users, many=True)
            return {"Mensaje":"Entro al metodo GET"}

        if user_id is not None:
            
            # Busco un único usuario por su ID
            user = User.query.get(user_id)
            # Lo convierto en un esquema
            user_schema = UserSchema().dump(user)
            return jsonify(user_schema)

    # if request.method == "POST"        
    def post(self):
            data = request.get_json() # get_json (convierte la información en formato JSON)
            username = data.get('username') # Le agrego una variable a lo ingresado en el json de postman
            first_name = data.get('first_name')
            last_name = data.get('last_name')

            new_user = User( 
                username = username, # especifico la variable creada anteriormente que quiero ingresar a la base de datos.
                first_name = first_name,
                last_name = last_name,
            )

            db.session.add(new_user) # Agregar a la base de datos
            db.session.commit() # Confirmar cambios

            return jsonify(Mensaje=f"Se creó el usuario {username}") # Mensaje que verifica que todo se realizó correctamente.

    def put(self, user_id):
        if not user_id:
            # Busco usuario para modificar
            user = User.query.get(user_id)
            # Datos para modificar
            data = request.get_json()
            nuevo_nombre = data.get('username')

            user.username = nuevo_nombre
            db.session.commit()

            user_schema = UserSchema().dump(user)
            return jsonify(user_schema)

    def delete(self, user_id):
        # Busco usuario
        user = User.query.get(user_id)
        # Elimino usuario
        db.session.delete(user)
        db.session.commit()
        return jsonify(Mensaje=f'User {user_id} eliminado')
###     

# Registro la URL para acceder a la clase
app.add_url_rule("/user", view_func=UserApi.as_view('user'))
app.add_url_rule("/user/<user_id>", view_func=UserApi.as_view('user_by_id'))
"""
