# Senderos

Proyecto de un sistema web para la asignatura Sistemas Software Basados en Web del Máster Profesional de Ingeniería Informática de la Universidad de Granada.

Se va a desarrollar a lo largo del segundo cuatrimestre del curso 2020/2021 por la alumna María Jesús López Salmerón.

Se va a intentar realizar una página similar a la página [TurGranada](https://www.turgranada.es/cosas-que-hacer/turismo-activo-y-de-naturaleza/excursiones-y-senderismo/) en donde se incluirán distintas rutas de senderismo y excursiones.

## Tarea 0

Preparar los cimientos del proyecto: 

* Crear el contenedor *Docker* con un fichero [*Dockerfile*](https://github.com/mjls130598/Senderos/blob/main/Dockerfile) para utilizar *Django* junto *Python*.

* Crear el archivo [*docker-compose*](https://github.com/mjls130598/Senderos/blob/main/docker-compose.yml) para utilizarlo como entorno de desarrollo del proyecto.

## Tarea 1

Añadir la base de datos ([MongoDB](https://docs.mongodb.com/guides/)) al proyecto:

* Se añadirá dentro de [requirements.txt](https://github.com/mjls130598/Senderos/blob/main/requirements.txt) la biblioteca [mongo-engine](http://mongoengine.org/).

* Se añade dentro de [docker-compose](https://github.com/mjls130598/Senderos/blob/main/docker-compose.yml) los servicios necesarios para la base de datos. Se pone como almacenamiento de los datos un path dentro del dispositivo puesto que *MongoDB* no detecta los dispositivos externos.

* Se crea el archivo [populate.py](https://github.com/mjls130598/Senderos/commit/eaa1e31a9d96cf2b8cace9ab9bcff84ea195c642) que trabaja como base de datos del sistema en donde se guardan las excursiones.