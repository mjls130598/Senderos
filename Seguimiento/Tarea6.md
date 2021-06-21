# Tarea 6: REST API

Para poder realizar esta tarea, se han tenido que realizar las siguientes actividades:

* Se ha tenido que instalar dentro del contenedor Docker *djangorestframework* y *django-rest-framework-mongoengine* para poder construir la API y *djangorestframework_simplejwt* para poder implementar las restricciones a la base de datos y crear los tokens de usuario. Todo ello se encuentra dentro de [requirements.txt](https://github.com/mjls130598/Senderos/blob/5354d2457d349d5e27f9d530407d2f9b2702e0d2/requirements.txt#L4)

* Posteriormente, se deben añadir dichas dependencias dentro de las aplicaciones instaladas del proyecto, dentro de [settings.py](https://github.com/mjls130598/Senderos/blob/5354d2457d349d5e27f9d530407d2f9b2702e0d2/mi_sitio_web/settings.py#L41)

* A continuación, se crean los *serializers* para poder mostrar o añadir los datos de la base de datos correspondiente con las excursiones. Dichos *serializers* se encuentran dentro del fichero [serializers.py](https://github.com/mjls130598/Senderos/blob/main/rutas_granada/serializers.py) en el que se indica el modelo que se tiene que fijar y el conjunto de campos con los que se va a manejar la información.

* Seguidamente, se crean las vistas en distintas clases para ver o añadir las excursiones en general o para ver/modificar/borrar una en particular. Esas vistas se encuentran dentro de [views.py](https://github.com/mjls130598/Senderos/blob/5354d2457d349d5e27f9d530407d2f9b2702e0d2/rutas_granada/views.py#L187).

* Una vez creadas las vistas, se deben crear las restricciones a la base de datos, únicamente se añade a las clases anteriores un atributo (*permission_classes*) en el que se indica que únicamente puede realizar todas las acciones el administrador (*IsAdminUser*) o únicamente leerlos (*ReadOnly*).

* Por último, se crean los enlaces para poder utilizar tanto la API como los tokens de usuario:
    * En cuanto a la API, se incluyen únicamente dos URLs para ver todas o una excursión sola (las acciones HTTP sobre esos datos ya se controlan dentro de las correspondientes clases) en [urls.py](https://github.com/mjls130598/Senderos/blob/5354d2457d349d5e27f9d530407d2f9b2702e0d2/rutas_granada/urls.py#L12) de la aplicación.

    * Correspondiente a los tokens, también se generan dos: una para crear el token y otro para refrescarlo al pasar un tiempo. En este caso se encuentra dentro de [urls.py](https://github.com/mjls130598/Senderos/blob/5354d2457d349d5e27f9d530407d2f9b2702e0d2/mi_sitio_web/urls.py#L25) del proyecto.