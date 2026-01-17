from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import URL

conexion_bd = URL.create(
    drivername="postgresql+psycopg2",
    username="prueba",
    password="1234",   
    host="127.0.0.1",
    port=5432,
    database="kardexV1")

engine = create_engine(conexion_bd)

#Autocommit hace que cuando se termine de ejecutar el comando a la BD no se guarde el cambio al instante
#Autoflush envia los cambios pendientes en una consulta y al ponerlo en False nosotros elegimos cuandos se sincronice
SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind = engine)
session = SessionLocal()

Base = declarative_base()