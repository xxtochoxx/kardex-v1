from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import engine, Base

class Producto(Base):
    __tablename__ = 'productos'
    
    codigo_producto = Column(String(50), primary_key = True, nullable = False)
    nombre = Column(String(50), nullable = False)

    marca_id = Column(Integer, ForeignKey('marcas.id'))
    modelo_id = Column(Integer, ForeignKey('modelos.id'))
    fabricante_id = Column(Integer, ForeignKey('fabricantes.id'))

    unidad_stock = Column(String(50), nullable = False)
    stock_actual = Column(Integer, nullable = False, default = 0)
    estado = Column(Boolean, nullable = False, default = False)
    
    modelo = relationship("Modelo", back_populates="productos")
    marca = relationship("Marca", back_populates="productos")
    fabricante = relationship("Fabricante", back_populates = "productos")

class Fabricante(Base):
    __tablename__ = "fabricantes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True)
    codigo = Column(String(5), nullable=False, unique=True)
    
    productos = relationship("Producto", back_populates="fabricante")

class Marca(Base):
    __tablename__ = "marcas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True)
    codigo = Column(String(5), nullable=False, unique=True)

    fabricante_id = Column(Integer, ForeignKey('fabricantes.id'))

    productos = relationship("Producto", back_populates="marca")

class Modelo(Base):
    __tablename__ = "modelos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True)
    codigo = Column(String(5), nullable=False, unique=True)

    marca_id = Column(Integer, ForeignKey('marcas.id'))
    
    productos = relationship("Producto", back_populates="modelo")

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
