# Tarea 9: Despliegue

Las actividades que se han tenido que realizar para desplegar ambas aplicaciones (*Django* y *React*) son las siguientes:

* Extraer los ficheros estáticos de ambas aplicaciones al directorio raíz dentro del directorio [static](https://github.com/mjls130598/Senderos/tree/main/static) de este proyecto para que pueda acceder *Nginx* a ellos:

    * Para Django, únicamente hay que ejecutar la orden `python manage.py collectstatic` dentro del contenedor.

    * Para React, ejecutar el comando `npm run build` dentro del proyecto y copiar los directorios resultado en el directorio *static* comentario anteriormente.

* Añadir como dependencia dentro del contenedor en [requirements.txt](https://github.com/mjls130598/Senderos/blob/a24dba9479e3331aa6fa9031a0b3117ec6f2f3f0/requirements.txt#L8) de la aplicación *Gunicorn* que será el encargado de desplegar la aplicación de *Django*.

* Cambiar la configuración de *Django* los siguientes aspectos:

    * Permitir que accedan a él [todos los hosts](https://github.com/mjls130598/Senderos/blob/a24dba9479e3331aa6fa9031a0b3117ec6f2f3f0/mi_sitio_web/settings.py#L183).

    * Poner a falso el modo [debug](https://github.com/mjls130598/Senderos/blob/a24dba9479e3331aa6fa9031a0b3117ec6f2f3f0/mi_sitio_web/settings.py#L28).

    * Cambiar la dirección donde se encuentran los [ficheros estáticos](https://github.com/mjls130598/Senderos/blob/a24dba9479e3331aa6fa9031a0b3117ec6f2f3f0/mi_sitio_web/settings.py#L178).

* Cambiar la estructura del Dockerfile para las siguientes acciones:

    * Añadir [*nginx*](https://github.com/mjls130598/Senderos/blob/a24dba9479e3331aa6fa9031a0b3117ec6f2f3f0/docker-compose.yml#L4), con su correspondiente [fichero de configuración](https://github.com/mjls130598/Senderos/blob/main/conf/default.conf) y la ubicación de los ficheros estáticos.

    * Ejecutar el proyecto web con [*gunicorn*](https://github.com/mjls130598/Senderos/blob/a24dba9479e3331aa6fa9031a0b3117ec6f2f3f0/docker-compose.yml#L17).

* Modificar las URLs dentro de React para acceder a la API de Django a través de *nginx*. Se han modificado dentro de [Buscar.js](https://github.com/mjls130598/Senderos/blob/a24dba9479e3331aa6fa9031a0b3117ec6f2f3f0/frontend/src/components/Buscar.js#L21), [Excursion.js](https://github.com/mjls130598/Senderos/blob/a24dba9479e3331aa6fa9031a0b3117ec6f2f3f0/frontend/src/components/Excursion.js#L21) y [Excursiones](https://github.com/mjls130598/Senderos/blob/a24dba9479e3331aa6fa9031a0b3117ec6f2f3f0/frontend/src/components/Excursiones.js#L18).