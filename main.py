from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr, condecimal, conint
from sqlalchemy import create_engine, Column, Integer, String, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from datetime import datetime
import re

DATABASE_URL = "postgresql://postgres:12345@localhost:5432/siatasiata"

engine = create_engine(DATABASE_URL)
engine.execute("CREATE SCHEMA IF NOT EXISTS siatasiata")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

# Modelo de la tabla restaurante en SQLAlchemy
class Restaurante(Base):
    __tablename__ = 'restaurante'
    __table_args__ = {'schema': 'siatasiata'}
    id = Column(Integer, primary_key=True, index=True)
    nombreRestaurante = Column(String(100), nullable=False)
    identificacionUsuario = Column(Integer, nullable=False)
    menu = Column(String(255), nullable=False)
    valorMenu = Column(Numeric, nullable=False)
    valorPagado = Column(Numeric, nullable=False)
    fechaPago = Column(Date, nullable=False)

Base.metadata.create_all(bind=engine)

# Esquema de entrada para el endpoint POST
class PagoCreate(BaseModel):
    nombreRestaurante: constr(regex=r'^[A-Za-z\s]+$')  # type: ignore # Solo acepta strings
    identificacionUsuario: conint(gt=0)  # type: ignore # Solo acepta números
    menu: constr(regex=r'^[A-Za-z0-9\s,]+$')  # type: ignore # Alfanumérico
    valorMenu: condecimal(gt=0) # type: ignore
    valorPagado: condecimal(gt=0, le=1000000) # type: ignore
    fechaPago: str

# Función para validar que el día sea impar
def validar_fecha_pago(fecha: str):
    try:
        fecha_obj = datetime.strptime(fecha, "%d/%m/%Y")
        if fecha_obj.day % 2 == 0:
            return False, "Lo siento, no se puede recibir el pago en días pares."
        return True, fecha_obj
    except ValueError:
        raise HTTPException(status_code=400, detail="Fecha no válida")
    

# Endpoint POST para registrar pagos
@app.post("/api/pagos")
def registrar_pago(pago: PagoCreate):
    valido, fecha_pago = validar_fecha_pago(pago.fechaPago)
    if not valido:
        raise HTTPException(status_code=400, detail=fecha_pago)
    
    valor_restante = pago.valorMenu - pago.valorPagado

    if valor_restante > 0:
        respuesta = f"Gracias por tu abono, sin embargo recuerda que te hace falta pagar {valor_restante}"
    elif valor_restante == 0:
        respuesta = "Gracias por pagar todo tu saldo"
    else:
        respuesta = "Error al procesar el pago"

    db = SessionLocal()
    nuevo_pago = Restaurante(
        nombreRestaurante=pago.nombreRestaurante,
        identificacionUsuario=pago.identificacionUsuario,
        menu=pago.menu,
        valorMenu=pago.valorMenu,
        valorPagado=pago.valorPagado,
        fechaPago=fecha_pago
    )
    db.add(nuevo_pago)
    db.commit()
    return {"respuesta": respuesta}

# Endpoint GET para consultar los pagos
@app.get("/api/pagos")
def obtener_pagos():
    db = SessionLocal()
    pagos = db.query(Restaurante).all()
    db.close()
    return pagos

