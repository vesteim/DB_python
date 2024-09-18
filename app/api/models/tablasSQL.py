from sqlalchemy import Column, Integer, String, Float, Date,ForeignKey

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Lamando a la base para crear tablas
Base=declarative_base()

#DEFINICION DE LAS TABLAS DE MI MODELO

# usuario
class Usuario():
    __tablename__='usuario'
    id=column(Integer, Primary_key=True, autoincrement=True)
    nombres=Column(Strings(50))
    fechaNacimiento=Column(Date)
    ubicacion=Column(String(100))
    metaAhorro= Column(Float)
    pass

class Gastos(Base):
    __tablename__='gasto'
    idGasto=Column(Integer)#,primary_key=True,atoincrement=True)
    descripcion=Column(String(100))
    #categoria
    valor=Column(Integer)
    fecha=Column(Date)
    pass

class Categoria(Base):
    __tablename__='categoria'
    idCat=Column(Integer)
    nombreCat=Column(String)
    #descipcion
    #fotoCategoria

class Ingreso(Base):
    __tablename__='Ingreso'
    """id
       valor
       description
       date
    """


    
