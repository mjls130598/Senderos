# Tarea 1: Base de datos

Añadir la base de datos ([MongoDB](https://docs.mongodb.com/guides/)) al proyecto:

* Se añadirá dentro de [requirements.txt](https://github.com/mjls130598/Senderos/blob/main/requirements.txt) la biblioteca [mongo-engine](http://mongoengine.org/).

* Se añade dentro de [docker-compose](https://github.com/mjls130598/Senderos/blob/main/docker-compose.yml) los servicios necesarios para la base de datos. Se pone como almacenamiento de los datos un path dentro del dispositivo puesto que *MongoDB* no detecta los dispositivos externos.

* Se crea el archivo [populate.py](https://github.com/mjls130598/Senderos/commit/eaa1e31a9d96cf2b8cace9ab9bcff84ea195c642) que trabaja como base de datos del sistema en donde se guardan las excursiones.

* Para restaurar y realizar el backup de la base de datos, se debe ejecutar **mongodump** (backup) y **mongorestore** (restauración) con la instancia de *MongoDB* ejecutándose según indica la página oficial de *MongoDB* encargado en [esos temas](https://docs.mongodb.com/manual/tutorial/backup-and-restore-tools/).