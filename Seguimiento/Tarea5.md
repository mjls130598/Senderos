# Tarea 5: Autentificación, autorización y registro de eventos

Las diversas actividades que se han realizado dentro de esta tarea son las siguientes:

* **Autenticación**: Dentro de ella se han tenido que realizar distintas labores:

    * Se ha realizado la configuración correspondiente a *Auth* de *Django* mirando que se encontrara la aplicación instalada dentro de [settings.py](https://github.com/mjls130598/Senderos/blob/978bb66880aaca4967f18e6922795064a1689990/mi_sitio_web/settings.py#L35) y añadir dentro de [urls.py](https://github.com/mjls130598/Senderos/blob/978bb66880aaca4967f18e6922795064a1689990/mi_sitio_web/urls.py#L23) del proyecto las URLs relacionadas con la cuenta de un usuario implementadas por esa misma aplicación.

    * Se han creado distintos botones para iniciar, cerrar o crear una cuenta dentro del sistema. Además, cuando el usuario haya iniciado en el sistema se mostrará un mensaje de bienvenida. Todo lo comentado anteriormente se encuentra dentro del fichero [base.html](https://github.com/mjls130598/Senderos/blob/978bb66880aaca4967f18e6922795064a1689990/rutas_granada/templates/base.html#L50).

    * Para realizar el login de un usuario, únicamente ha sido necesario crear su visualización que se encargan los archivos [login.html](https://github.com/mjls130598/Senderos/blob/main/rutas_granada/templates/registration/login.html) y [login.css](https://github.com/mjls130598/Senderos/blob/main/rutas_granada/static/rutas_granada/css/login.css). Ambos ficheros, y todos los templates relacionados con las cuentas de usuario deben encontrarse dentro de la carpeta [registration](https://github.com/mjls130598/Senderos/tree/main/rutas_granada/templates/registration) de la app para que *Auth* los pueda encontrar.

    * Las acciones de logout y login ya las implementa la aplicación *auth* dentro de *Django*, pero del registro de un usuario no se encuentra implementado. Por lo tanto, es necesario crear su visualización (dentro de [signup.html](https://github.com/mjls130598/Senderos/blob/main/rutas_granada/templates/registration/signup.html)) y su funcionalidad (que se encuentra dentro del fichero [views.py](https://github.com/mjls130598/Senderos/blob/978bb66880aaca4967f18e6922795064a1689990/rutas_granada/views.py#L157))

* **Autorización**: En este caso, únicamente se ha comprobado antes de mostrar cualquier acción sobre la pantalla que el usuario que se ha logeado forma parte de *staff*. Para ello, hay una función dentro de *user* en el template que devuelve un booleano de si ese usuario puede modificar la BD o no. Se puede ver su uso dentro de [excursiones.html](https://github.com/mjls130598/Senderos/blob/978bb66880aaca4967f18e6922795064a1689990/rutas_granada/templates/rutas_granada/excursiones.html#L15) y de [excursion.html](https://github.com/mjls130598/Senderos/blob/978bb66880aaca4967f18e6922795064a1689990/rutas_granada/templates/rutas_granada/excursion.html#L15)

* **Registro**: En este caso se utilizan dos tipos de registros distintos:

    * *Logging*: En el que se guarda dentro de un fichero los distintos mensajes que indican lo que sucede dentro de la aplicación. Para ello es necesario que en el fichero [views.py](https://github.com/mjls130598/Senderos/blob/main/rutas_granada/views.py) crear el logger y utilizarlo dentro de él cuando sea necesario. Para que se guarde en un fichero y se muestre por la consola dentro de [settings.py](https://github.com/mjls130598/Senderos/blob/978bb66880aaca4967f18e6922795064a1689990/mi_sitio_web/settings.py#L53) se necesita añadir su configuración (como que tipos de mensajes se van a mostrar, el formato de estos, ...). 

    * *Signals*: En este caso se muestra mensajes por la consola cuando reciba algún evento relacionado con la sesión de un usuario. Para poder realizarlo se crea el fichero [signals.py](https://github.com/mjls130598/Senderos/blob/main/rutas_granada/signals.py) donde se muestra cuando deben mostrarse los distintos mensajes y en [apps.py](https://github.com/mjls130598/Senderos/blob/978bb66880aaca4967f18e6922795064a1689990/rutas_granada/apps.py#L7) al fichero que tiene que llamar el proyecto para que reciba esas señales.
