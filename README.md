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

* Para restaurar y realizar el backup de la base de datos, se debe ejecutar **mongodump** (backup) y **mongorestore** (restauración) con la instancia de *MongoDB* ejecutándose según indica la página oficial de *MongoDB* encargado en [esos temas](https://docs.mongodb.com/manual/tutorial/backup-and-restore-tools/).

## Tarea 2

Se empieza a utilizar *Django* realizando las siguientes tareas:

* Se realiza la configuración correspondiente al proyecto creado modificando el archivo [settings.py](https://github.com/mjls130598/Senderos/blob/main/mi_sitio_web/settings.py):

    * Se ha indicado la zona horaria y el idioma del proyecto.
    * Se indica dónde se van a ubicar los documentos estáticos.
    * Se le dice los distintos hosts con los que se puede conectar al proyecto.

* Se crea el modelo *Excursión* en el fichero [models.py](https://github.com/mjls130598/Senderos/blob/main/rutas_granada/models.py) para poder manejar sus datos en la aplicación.

* Se crea una aplicación que contiene las rutas de Granada. Dicha aplicación está almacenada en el directorio [rutas_granada](https://github.com/mjls130598/Senderos/tree/main/rutas_granada).

* Se añaden las correspondientes vistas (que se encargan de recoger los datos y mostrárselos al cliente) dentro del archivo [views.py](https://github.com/mjls130598/Senderos/blob/main/rutas_granada/views.py).

* Crear los archivos estáticos que se encuentran dentro del directorio [static](https://github.com/mjls130598/Senderos/blob/main/static).

* Se añaden las rutas para poder acceder la información en [urls.py](https://github.com/mjls130598/Senderos/blob/main/rutas_granada/urls.py).