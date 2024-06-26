from flask import Flask
#Importo un objeto de la clase flask
from appp.views import *
#Importo todas las funciones desde las vistas

#Crear una instancia de Flask
app = Flask(__name__)

#Asociación de las rutas con las vistas, el método correspondiente
app.route('/',methods=['GET'])(index)
app.route('/api/products/',methods=['GET'])(get_all_products)

#Permite separar el código que se ejecuta cuando se corre el archivo
if __name__=='__main__':
    app.run(debug=True)
