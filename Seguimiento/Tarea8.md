# Tarea 8: React

Las actividades que se han tenido que realizar para implementar la página [TurGranada](https://www.turgranada.es/cosas-que-hacer/turismo-activo-y-de-naturaleza/excursiones-y-senderismo/) en *React* siguiendo más o menos la misma estructura que *Django* son las siguientes:

* Configurar *Django* para que permitiera llamadas a la API desde otras URLs externas. Para ello hay que instalar la dependencia dentro del contenedor *django-cors-headers* (dentro de [requirements.txt](https://github.com/mjls130598/Senderos/blob/554c610f90691fba54c18a2ff2fac063c55fd8b2/requirements.txt#L7)). A continuación, dentro de la configuración del proyecto [settings.py](https://github.com/mjls130598/Senderos/blob/main/mi_sitio_web/settings.py) había que indicar que se permite el acceso a todas las URLs.

* Una vez configurado, se crea el proyecto de *React* (que se encuentra dentro de la carpeta [frontend](https://github.com/mjls130598/Senderos/tree/main/frontend)).

* Seguidamente, dentro del proyecto de *React* se instala *Bootstrap* para facilitar con la visualización de las páginas y se añade su importación dentro de los componentes correspondientes.

* Dentro del proyecto React se realizan las siguientes labores:

    * Dentro de [Apps.js](https://github.com/mjls130598/Senderos/blob/main/frontend/src/App.js), se crea la vista "base" de todas las páginas y, además, se crean las rutas con las que se trabajará la aplicación (*buscar*, *excursiones*, *excursion/id*) que llamarán a sus correspondientes componentes, en la carpeta [components](https://github.com/mjls130598/Senderos/tree/main/frontend/src/components).

    * En el directorio [static](https://github.com/mjls130598/Senderos/tree/main/frontend/src/static) se encuentra todo lo relacionado con los CSSs y las imágenes de la aplicación.

    * La página *buscar* se encuentra dentro del componente [Buscar.js](https://github.com/mjls130598/Senderos/blob/main/frontend/src/components/Buscar.js) que lo único que hay es un formulario de búsqueda y un conjunto de *Cards* de excursiones, que se halla la visualización de cada uno de ellos dentro de [Excursion-cards.js](https://github.com/mjls130598/Senderos/blob/main/frontend/src/components/Excursion-cards.js).

    * La página *excursiones* del componente [Excursiones.js](https://github.com/mjls130598/Senderos/blob/main/frontend/src/components/Excursiones.js) únicamente tiene el conjunto de *Cards* de cada excursión de la base de datos.

    * El último componente por nombrar, [Excursion.js](https://github.com/mjls130598/Senderos/blob/main/frontend/src/components/Excursion.js), muestra el detalle de una excursión dado su id en la URL (*excursion/id*).