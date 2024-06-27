from flask import jsonify
from app.models import Product

#Una función del módulo flask para convertir a formato json listas y diccionarios de python

def index():
    response = {'message':'Hola mundo API FLASK'}
    return jsonify(response)


"""Un crud de productos"""
#Función que busca un producto

def get_product():
    pass

#Función que busca todo el listado de productos
def get_all_products():
    products = Product.get_all()
    return jsonify(products)

def create_product():
    pass

def update_product():
    pass

def delete_product():
    pass

