#importar la libreria principal (flask alchemy)
from flask import Flask, redirect, url_for, request 
from flask_sqlalchemy import SQLAlchemy

import json

# Se crea la aplicacion

app = Flask(__name__)

# Permitir encriptamiento desde la app, se configura una clave principal
app.secret_key = 'dasfkn:LVnaWOGVN;Lk DLILHS [Q'

# Establece la cadena de conexion a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/embebidos'

# realizamos la conexion
db = SQLAlchemy(app)

# Se crea un modelo de la tabla donde esta la informacion (Modelo ORM)
class Lectura(db.Model):
    # defino como se llama la tabla en la base de datos
    __tablename__ = 'lecturas'
    id = db.Column('id', db.Integer, primary_key = True)
    topico = db.Column(db.String(100))
    payload = db.Column(db.String(255))

    def __init__(self, topico, payload):
        self.topico = topico
        self.payload = payload

@app.route('/lecturas')
def get_lecturas():
    lecturas = Lectura.query.all()
    respuesta = []
    for lectura in lecturas:
        data={
            'id': lectura.id,
            'topico': lectura.topico,
            'payload': lectura.payload
            
        }
        respuesta.append(data)
    
        return json.dumps(respuesta, ensure_ascii=False).encode('utf-8')

@app.route('/lecturasById/<valor>')
def get_lecturas_by_id(valor):
    lecturas = Lectura.query.filter_by(id=valor).all()
    respuesta = []
    for lectura in lecturas:
        data={
            'id': lectura.id,
            'topico': lectura.topico,
            'payload': lectura.payload
            
        }
        respuesta.append(data)
    
        return json.dumps(respuesta, ensure_ascii=False).encode('utf-8')