from sqlalchemy import Boolean, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import engine, Base

class Productos(Base):
    __tablename__ = 'productos'
    codigo_producto = Column(String(50), primary_key= True, nullable = False)

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
'''Terminar de crear la tabla de abajo'''

# CREATE TABLE productos (
#     codigo_producto VARCHAR(15) PRIMARY KEY,
#     nombre VARCHAR(100) NOT NULL,
#     marca VARCHAR(50) NOT NULL,
#     modelo VARCHAR(50) NOT NULL,
#     fabricante VARCHAR(50) NOT NULL,
#     unidad_stock VARCHAR(20) NOT NULL,
#     stock_actual INTEGER NOT NULL DEFAULT 0,
#     estado BOOLEAN NOT NULL DEFAULT TRUE,
# );