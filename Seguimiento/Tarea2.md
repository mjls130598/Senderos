# Tarea 2: Creación de la aplicación

Se empieza a utilizar *Django* realizando las siguientes tareas:

* Se realiza la configuración correspondiente al proyecto creado modificando el archivo [settings.py](https://github.com/mjls130598/Senderos/blob/main/mi_sitio_web/settings.py):

    * Se conecta a la base de datos de MongoDB.
    * Se ha indicado la zona horaria y el idioma del proyecto.
    * Se indica dónde se van a ubicar los documentos estáticos y los templates.
    * Se le dice los distintos hosts con los que se puede conectar al proyecto.

* Se crean los modelos necesarios en el fichero [models.py](https://github.com/mjls130598/Senderos/blob/main/rutas_granada/models.py) para poder manejar sus datos en la aplicación.

    * Se escribe el modelo de *Comentario*.
    * Se inserta el modelo *Foto*.
    * Se añade el modelo *Excursión*.

* Se crea una aplicación que contiene las rutas de Granada. Dicha aplicación está almacenada en el directorio [rutas_granada](https://github.com/mjls130598/Senderos/tree/main/rutas_granada).

* Se añaden las correspondientes vistas (que se encargan de recoger los datos y mostrárselos al cliente) dentro del archivo [views.py](https://github.com/mjls130598/Senderos/blob/main/rutas_granada/views.py).

* Crear los archivos estáticos que se encuentran dentro del directorio [static](https://github.com/mjls130598/Senderos/blob/main/static).

* Se añaden las rutas para poder acceder la información en [urls.py](https://github.com/mjls130598/Senderos/blob/main/rutas_granada/urls.py). Para que sepa qué rutas debe acceder de la aplicación se realizan los siguientes cambios en [urls.py](https://github.com/mjls130598/Senderos/blob/main/mi_sitio_web/urls.py) del proyecto.

* Poder acceder al panel de administración de la aplicación se debe crear un usuario. Para ello se accede dentro del bash del contenedor y se escribe el siguiente comando y se siguen los pasos que se le indican durante su ejecución:
```
python manage.py createsuperuser
``` 
* Se comprueba que funciona correctamente la aplicación realizando sus correspondientes tests. Dichos tests se encuentran en el fichero [tests.py](https://github.com/mjls130598/Senderos/blob/main/rutas_granada/tests.py) de la aplicación *rutas_granada*.