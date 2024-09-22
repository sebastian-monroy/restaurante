# api Restaurante prueba tecnica

Esta es una api la cual esta creada con **FastApi** la cual tiene como objetivo gestionar los pagos de una cadena de restaurante, utilizando **POSTGRESQL** como bases de datos

## requisitos 

Antes de levantar el proyecto, asegurense de tener instalado lo siguiente: 

1. **Python 3.12.6** recomendable trabajar con la ultima version: Puedes descargarlo desde [pyhton.org](https://www.python.org/).
2. **PostgresSQL** asegurense de tener PostgreSQL instalado y corriendo en sus maquinas, en mi caso trabaje con la version 15, si lo desean pueden trabajar con la ultima version. para la instalacion del postgreSQL recomiendo mucho este tutorial (https://www.youtube.com/watch?v=cHGaDfzJyY4), por otra parte, deje el puerto 5432 en postgresql ya que no me dejo trabajar con el 6969. una vez instalado el postgresql debes poner una contraseña para el superusuario la cual sera "siata" en este caso u otra como "12345", mejor dicho la que deseen. ya cuando este corriendo todo el programa inicia con la constraseña que se haya establecido y crea la base de datos, el esquema y la tabla restaurante en la base de datos de esta manera: 

'''  
    scripts SQL a implementar

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

una vez creada la base de datos junto con la tabla restaurante junto con sus columnas con todo lo requerido, ahora se procedera con la instalacion del proyecto en tu maquina local, para ello realizamos lo siguiente en la consola la cual abres con windows + r

1. digitas en la consola dentro de la carpeta donde quieras que vaya el proyecto: git clone https://github.com/sebastian-monroy/restaurante.git

2. ahora dentro de la raiz del proyecto creas un entorno virtual con los siguientes comandos
- creacion de un entorno virtual: python -m venv venv
- para windows: venv\Scripts\activate
- para linux y macOS: source venv/bin/activate

3. ahora instalamos las dependencias necesarias, esto aun dentro de la raiz de donde se haya descargado el proyecto

- pip install -r requirements.txt

otras instalaciones como paquetes y demas cosas con las cuales se trabajo el proyecto
- pip install fastapi uvicorn psycopg2-binary #para ejecutar el servidor
- pip install sqlalchemy databases #para manejar la conexion a bases de datos
- pip install asyncpg[postgresql]  #para manejar postgresql driver


4. configura ahora en el archivo main.py la cadena de conexion a la base de datos
- DATABASE_URL = 'postgresql://nombreusuario:contraseña@localhost:5432/nombre_basededatos' #esta es la estructura de la url de como se compone, por lo tanto queda de la siguiente manera 

- DATABASE_URL = 'postgresql://postgres:12345@localhost:5432/siatasiata'
    Observaciones: Aqui me toco con el puerto 5432 porque intente con el 6969 y puso muchisimos problemas, la base de datos se llama siatasiata que fue la que creamos por medio de los scripts de SQL, el usuario  es postgres y la contraseña es 12345, si lo desean pueden cambiarlo a su gusto, use la contraseña de siata pero no me dejaba abrir el servidor por eso use otra contraseña diferente a siata

5. ahora para ejecutar  el proyecto, debes ejecutar el siguiente comando en la consola:

- uvicorn main:app --reload --port 5432 #en mi caso con respecto al problema de los puertos

- uvicorn main:app --reload --port 6969 # en caso de que les funcione el puerto 6969


