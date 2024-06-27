from app.database import get_db


class Product:
    #Método constructor
    def __init__(self,id_product=None, title=None,price=None,release_date=None, banner=None):
        self.id_product = id_product
        self.title = title
        self.price = price
        self.release_date = release_date
        self.banner = banner


    @staticmethod
    #Lógica para traer los productos:
    def get_all(): 
        db = get_db()
        cursor = db.cursor() #cursor permite ejecutar ciertas instrucciones de la base de datos y extraer el resultado de esa consulta o de la conexión con la bd.
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall() 
        return rows

    def save(self):
        #Lógica para el INSERT/UPDATE en la base de datos
        pass

    def delete(self):
        #Lógica para hacer un DELETE en la base de datos
        pass

    

