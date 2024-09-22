# api Restaurante prueba tecnica

Esta es una api la cual esta creada con **FastApi** la cual tiene como objetivo gestionar los pagos de una cadena de restaurante, utilizando **POSTGRESQL** como bases de datos

## requisitos 

Antes de levantar el proyecto, asegurense de tener instalado lo siguiente: 

1. **Python 3.12.6** recomendable trabajar con la ultima version: Puedes descargarlo desde [pyhton.org](https://www.python.org/).
2. **PostgresSQL** asegurense de tener PostgreSQL instalado y corriendo en sus maquinas, en mi caso trabaje con la version 15, si lo desean pueden trabajar con la ultima version. para la instalacion del postgreSQL recomiendo mucho este tutorial (https://www.youtube.com/watch?v=cHGaDfzJyY4), por otra parte, deje el puerto 5432 en postgresql ya que no me dejo trabajar con el 6969. una vez instalado el postgresql debes poner una contraseña para el superusuario la cual sera "siata" en este caso u otra como "12345", mejor dicho la que deseen. ya cuando este corriendo todo el programa inicia con la constraseña que se haya establecido y crea la base de datos, el esquema y la tabla restaurante en la base de datos de esta manera: 

'''  
    scripts SQL:

    CREATE DATABASE siatasiata;               #creacion de la base de esta manera

    CREATE SCHEMA siatasiata;                 #creacion del esquema para nuestra base de datos

    CREATE USER siata WITH PASSWORD 'siata';  #creando el usuario con contraseña 

    GRANT ALL PRIVILEGES ON DATABASE siatasiata TO siata; #conceder privilegios a la base de datos siata

    #creando la tabla restaurante en la base de datos siatasiata
    CREATE TABLE siatasiata.restaurante (
        id SERIAL PRIMARY KEY,
        nombreRestaurante VARCHAR(100) NOT NULL,
        identificacionUsuario BIGINT NOT NULL,
        menu VARCHAR(255) NOT NULL,
        valorMenu NUMERIC NOT NULL,
        valorPagado NUMERIC NOT NULL,
        fechaPago DATE NOT NULL
    );

'''

## instalacion