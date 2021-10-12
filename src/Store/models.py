from sqlalchemy.orm import relationship

from db import db_manager
from sqlalchemy import Column, Integer, String, Float, ForeignKey

#Tabla maestra de productos

class Producto(db_manager.Base):
    __tablename__ = 'producto'

    productID = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    productModel = Column(String, nullable=False)
    cultureID = Column(String, nullable=False)
    Proveedor = relationship('Proveedor')

    def __init__(self, productID, name, productModel, cultureID):
        self.productID = productID
        self.name = name
        self.productModel = productModel
        self.cultureID = cultureID


    def __repr__(self):
        return f'Product({self.productID}, {self.name}, {self.productModel}, {self.cultureID})'

    def __str__(self):
        return self.name


class Proveedor (db_manager.Base):
    __tablename__ = 'provedores'

    provedorID = Column(Integer, primary_key=True)
    productID = Column(Integer, ForeignKey('producto.productID'))
    averageLeadTime = Column (Integer, nullable=False)
    businessEntityID = Column (Integer, nullable=False)
    accountNumber = Column (String, nullable=False)
    name = Column (String, nullable=False)

    def __init__(self, productID, businessEntityID, averageLeadTime, accountNumber, name):
        self.productID = productID
        self.businessEntityID = businessEntityID
        self.averageLeadTime = averageLeadTime
        self.accountNumber = accountNumber
        self.name = name

    def __repr__(self):
        return f'Product({self.productID}, {self.businessEntityID}, {self.averageLeadTime}, {self.accountNumber}, {self.name})'

    def __str__(self):
        return self.name