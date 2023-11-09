# Se generan todas las rutas o endpoints

from flask import (
    jsonify,
    render_template,
    request,
)

from app import app  # Llamar la variable app del init desde la carpeta
from app import db

from app.models.models import (
    User,
    Post,
    Comment,
    Category,
)  # Importamos las tablas generadas en models

from app.schemas.schema import PostSchema, UserSchema, CommentSchema, CategorySchema

from flask.views import MethodView

from datetime import datetime


@app.route("/")  # Generar ruta
def index():
    return render_template("index.html")


class UserApi(MethodView):
    def get(self, user_id=None):
        try:
            if user_id is None:
                users = User.query.all()
                users_schema = UserSchema().dump(users, many=True)
                return jsonify(users_schema)
            if user_id is not None:
                # Busco un unico usuario por su ID
                user = User.query.get(user_id)
                # Lo convierto en un esquema
                user_schema = UserSchema().dump(user)
                return jsonify(user_schema)
        except:
            return jsonify("Error 404 usuario no encontrado.")

    # if request.method == "POST"
    def post(self):
        data = request.get_json()
        username = data.get("username")
        first_name = data.get("first_name")
        last_name = data.get("last_name")

        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify(MENSAJE=f"Se creo el usuario {username}")

    def put(self, user_id):
        user = User.query.get(user_id)
        # Info a modificar
        data = request.get_json()
        nuevo_nombre_de_usuario = data.get("username")

        user.username = nuevo_nombre_de_usuario
        db.session.commit()

        user_schema = UserSchema().dump(user)
        return jsonify(user_schema)

    def delete(self, user_id):
        try:
            # Busco un unico usuario por su ID
            user = User.query.get(user_id)
            # Elimino el usuario
            db.session.delete(user)
            db.session.commit()
            return jsonify(Mensaje=f"User {user_id} deleted")
        except:
            return jsonify("Error 404 usuario no encontrado.")


# Registro la URL para acceder a la clase
app.add_url_rule("/user", view_func=UserApi.as_view("user"))
app.add_url_rule("/user/<user_id>", view_func=UserApi.as_view("user_by_id"))


class PostApi(MethodView):
    def get(self, post_id=None):
        try:
            if post_id is None:
                posts = Post.query.all()
                posts_schema = PostSchema().dump(posts, many=True)
                return jsonify(posts_schema)
            if post_id is not None:
                # Busco un unico usuario por su ID
                post = Post.query.get(post_id)
                # Lo convierto en un esquema
                post_schema = PostSchema().dump(post)
                return jsonify(post_schema)
        except:
            return jsonify("A ocurrido un error 404")

    # if request.method == "POST"
    def post(self):
        data = request.get_json()
        title = data.get("title")
        content = data.get("content")
        user = data.get("user_id")
        category = data.get("category_id")

        new_post = Post(title=title, content=content, fecha_creacion=datetime.now(), user=user, category=category)

        db.session.add(new_post)
        db.session.commit()

        return jsonify(MENSAJE=f"Se creo el post {title}")

    def put(self, post_id):
        post = Post.query.get(post_id)
        # Info a modificar
        data = request.get_json()
        nuevo_contenido = data.get("content")

        post.content = nuevo_contenido
        db.session.commit()

        post_schema = PostSchema().dump(post)
        return jsonify(post_schema)

    def delete(self, post_id):
        try:
            # Busco un unico usuario por su ID
            post = Post.query.get(post_id)
            # Elimino el usuario
            db.session.delete(post)
            db.session.commit()
            return jsonify(Mensaje=f"Post {post_id} deleted")
        except:
            return jsonify("A ocurrido un error 404")


# Registro la URL para acceder a la clase
app.add_url_rule("/post", view_func=PostApi.as_view("post"))
app.add_url_rule("/post/<post_id>", view_func=PostApi.as_view("post_by_id"))


class CategoryApi(MethodView):
    def get(self, category_id=None):
        try:
            if category_id is None:
                categories = Category.query.all()
                categories_schema = CategorySchema().dump(categories, many=True)
                return jsonify(categories_schema)
            if category_id is not None:
                # Busco un unico usuario por su ID
                category = Category.query.get(category_id)
                # Lo convierto en un esquema
                category_schema = CategorySchema().dump(category)
                return jsonify(category_schema)
        except:
            return jsonify("A ocurrido un error 404")

    # if request.method == "POST"
    def post(self):
        data = request.get_json()
        category = data.get("category")

        new_category = Category(
            category=category,
        )

        db.session.add(new_category)
        db.session.commit()

        return jsonify(MENSAJE=f"Se creo la categoria {category}")

    def put(self, category_id):
        category = Category.query.get(category_id)
        # Info a modificar
        data = request.get_json()
        nuevo_nombre_de_categoria = data.get("category")

        category.category = nuevo_nombre_de_categoria
        db.session.commit()

        category_schema = CategorySchema().dump(category)
        return jsonify(category_schema)

    def delete(self, category_id):
        try:
            # Busco un unico usuario por su ID
            category = Category.query.get(category_id)
            # Elimino el usuario
            db.session.delete(category)
            db.session.commit()
            return jsonify(Mensaje=f"Category {category_id} deleted")
        except:
            return jsonify("A ocurrido un error 404")


# Registro la URL para acceder a la clase
app.add_url_rule("/category", view_func=CategoryApi.as_view("category"))
app.add_url_rule("/category/<category_id>", view_func=CategoryApi.as_view("category_by_id"))


class CommentApi(MethodView):
    def get(self, comment_id=None):
        try:
            if comment_id is None:
                comments = Comment.query.all()
                comments_schema = CommentSchema().dump(comments, many=True)
                return jsonify(comments_schema)
            if comment_id is not None:
                # Busco un unico usuario por su ID
                comment = User.query.get(comment_id)
                # Lo convierto en un esquema
                comment_schema = CommentSchema().dump(comment)
                return jsonify(comment_schema)
        except:
            return jsonify("A ocurrido un error 404")

    # if request.method == "POST"
    def post(self):
        data = request.get_json()
        content = data.get("content")
        post = data.get("post_id")
        user = data.get("user_id")

        new_comment = Comment(content=content, fecha_creacion=datetime.now(), post=post, user=user)
        db.session.add(new_comment)
        db.session.commit()

        return jsonify(MENSAJE=f"Se creo el comentario")

    def put(self, comment_id):
        comment = Comment.query.get(comment_id)
        # Info a modificar
        data = request.get_json()
        nuevo_comentario = data.get("comment")

        comment.content = nuevo_comentario
        db.session.commit()

        comment_schema = CommentSchema().dump(comment)
        return jsonify(comment_schema)

    def delete(self, comment_id):
        try:
            # Busco un unico usuario por su ID
            comment = Comment.query.get(comment_id)
            # Elimino el usuario
            db.session.delete(comment)
            db.session.commit()
            return jsonify(Mensaje=f"Comment {comment_id} deleted")
        except ValueError:
            return jsonify("A ocurrido un error 404")


# Registro la URL para acceder a la clase
app.add_url_rule("/comment", view_func=CommentApi.as_view("comment"))
app.add_url_rule("/comment/<comment_id>", view_func=CommentApi.as_view("comment_by_id"))


# https://black.vercel.app/ (acomodar código de python)

# https://playcode.io/ (acomodar código de js)
# ctrl shift i lo hace en js automáticamente en vscode 

# AQUI DEBERIAN GENERARA LO MISMO QUE PARA USER; PERO PARA POSTS, LO DE ABAJO YA NO SERIA UTIL SI APLICAN EL METHODVIEW
# rutas para el posts

