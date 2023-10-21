#IMPORTS NATIVOS DE PYTHON.
import os, sys
import bcrypt

#IMPORTS NATIVOS DEL FRAMEWORK
from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#IMPORTS PROPIOS
# from app.models.models import (
#     User,
#     Pais,
#     Provincia,
#     Localidad,
#     Persona
# )


app= Flask(__name__)

#app.config['SQLALCHEY_DATABASE_URI'] = mysql+pymysql://usuario:contraseña@ip/nombre_db
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')


db = SQLAlchemy(app) #recibe la app 
migrate = Migrate(app, db) #recibe la app en si y donde va a instanciar el migrate.
jwt = JWTManager(app)
ma= Marshmallow(app)

load_dotenv()

from app.views import view

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5005)



#Query para obtener datos de la persona

#flask db migrate -m "creacion_de_pais"
#flask db upgrade


# ver marshmallow