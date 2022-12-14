from flask import Flask ,jsonify ,request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend
# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/cursoslearn'
# desde el objeto app configuro la URI de la BBDD    user:clave@localhost/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)
ma=Marshmallow(app)
 
# defino la tabla
class Cursos(db.Model):   # la clase cursos hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    precio=db.Column(db.Integer)
    descripcion=db.Column(db.String(1000))
    imagen=db.Column(db.String(500))
    def __init__(self,nombre,precio,descripcion,imagen):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.precio=precio
        self.descripcion=descripcion
        self.imagen=imagen
 
with app.app_context():
    db.create_all()  # crea las tablas
#  ************************************************************
class CursoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','precio','descripcion','imagen')
curso_schema=CursoSchema()            # para crear un curso
cursos_schema=CursoSchema(many=True)  # multiples registros
 
# crea los endpoint o rutas (json)
@app.route('/cursos',methods=['GET'])
def get_Cursos():
    all_cursos=Cursos.query.all()     # query.all() lo hereda de db.Model
    result=cursos_schema.dump(all_cursos)  # .dump() lo hereda de ma.schema
    return jsonify(result)
 
@app.route('/cursos/<id>',methods=['GET'])
def get_curso(id):
    curso=Cursos.query.get(id)
    return curso_schema.jsonify(curso)

@app.route('/cursos/<id>',methods=['DELETE'])
def delete_curso(id):
    curso=Cursos.query.get(id)
    db.session.delete(curso)
    db.session.commit()
    return curso_schema.jsonify(curso)

@app.route('/cursos', methods=['POST']) # crea ruta o endpoint
def create_curso():
    print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    precio=request.json['precio']
    descripcion=request.json['descripcion']
    imagen=request.json['imagen']
    new_curso=Cursos(nombre,precio,descripcion,imagen)
    db.session.add(new_curso)
    db.session.commit()
    return curso_schema.jsonify(new_curso)

@app.route('/cursos/<id>' ,methods=['PUT'])
def update_curso(id):
    curso=Cursos.query.get(id)
   
    nombre=request.json['nombre']
    precio=request.json['precio']
    descripcion=request.json['descripcion']
    imagen=request.json['imagen']
 
    curso.nombre=nombre
    curso.precio=precio
    curso.descripcion=descripcion
    curso.imagen=imagen
    db.session.commit()
    return curso_schema.jsonify(curso)


 
# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)