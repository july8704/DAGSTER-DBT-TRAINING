from db import db_manager
from models import Producto, Proveedor

def run () :
    ## Insertar valores
    #producto_1 = Producto (995,'LL Bottom Bracket','LL Bottom Bracket','en')
    #db_manager.session.add(producto_1)
    #db_manager.session.commit()

    ### Consulta
    consulta = db_manager.session.query(Producto)
    print(consulta.all())

if __name__ == '__main__':
    db_manager.Base.metadata.create_all(db_manager.engine)
    run()