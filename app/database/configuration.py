from sqlalchemy import create_engine,event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

#datos oara ka cibexuib a BD

dataBaseName="gestirdb"
userName="root"
userPasword=""
connectionPort=3300
server="localhost"

#creando la conexion
dataBaseConnection=f"mysql+mysqlconnector://{userName}:{userPasword}@{server}:{connectionPort}/{dataBaseName}"

#creo el motor de conexion
engine = create_engine(dataBaseConnection)

#abrir la sesion con la bd
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
