
#scripts para SQL una vez este quede instalado

# CREATE USER siata WITH PASSWORD 'siata';
# CREATE DATABASE siatasiata;
# GRANT ALL PRIVILEGES ON DATABASE siatasiata TO siata;


#para ejecutar el servidor fastAPI:
#uvicorn main:app --reload --port 6969


#CREATE SCHEMA siatasiata;

# creando la tabla con los campos requeridos en la prueba

# CREATE TABLE siatasiata.restaurante (
#   id SERIAL PRIMARY KEY,
#   nombreRestaurante VARCHAR(100) NOT NULL,
#   identificacionUsuario BIGINT NOT NULL,
#   menu VARCHAR(255) NOT NULL,
#   valorMenu NUMERIC NOT NULL,
#   valorPagado NUMERIC NOT NULL,
#   fechaPago DATE NOT NULL
# );