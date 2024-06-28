from app.database import get_db


class Product:
    #Método constructor
    def __init__(self,id_product=None, title=None,price=None,release_date=None,banner=None):
        self.id_product = id_product
        self.title = title
        self.price = price
        self.release_date = release_date
        self.banner = banner


    @staticmethod 
    def get_all(): #Lógica para traer los productos.
        db = get_db()
        cursor = db.cursor() #cursor permite ejecutar ciertas instrucciones de la base de datos y extraer el resultado de esa consulta o de la conexión con la bd.
        # cursor.execute("SELECT * FROM products")
        cursor.execute("SELECT * FROM compumundo_hr_flask.products")
        rows = cursor.fetchall() 
        products = [Product(id_product=row[0], title=row[1], price=row[2], release_date=row[3], banner=row[4]) for row in rows]
        cursor.close()
        return rows

    def save(self):
        #Lógica para el INSERT/UPDATE en la base de datos
        pass

    def delete(self):
        #Lógica para hacer un DELETE en la base de datos
        pass


    def serialize(self):
        return{ #Dado un objeto de la clase product, devuelvo un diccionario con los objetos de la instancia, de la representación. 
            'id_product': self.id_product,
            'title': self.title,
            'price': self.price,
            'release_date': self.release_date,
            'banner': self.banner,

        }

    

