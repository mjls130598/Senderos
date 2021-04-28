# Tarea 4: CRUD

Durante esta tarea se realizan las siguientes actividades relacionadas con CRUD:

* Primero, se creará una vista únicamente para mostrar la información de una excursión. En este caso se modificará el fichero [excursion.html](https://github.com/mjls130598/Senderos/blob/main/rutas_granada/templates/rutas_granada/excursion.html) para que muestre toda la información almacenada en la base de datos sobre una excursión en concreto y se puedan realizar las funciones correspondientes sobre ella.

* A continuación, se implementa el borrado de una excursión. Para eso se modifica el primer formulario de la página (el que únicamente tiene el botón de la papelera) y se le indica que su acción es de tipo POST y llamo al método que se llama para mostrar la información de una excursión. Por lo tanto, se ha modificado dentro de [views.py](https://github.com/mjls130598/Senderos/blob/main/rutas_granada/views.py) su método correspondiente para que cuando sea una petición GET muestre la página y para cuando sea POST, dependiendo del valor del input oculto de los formularios, haga una acción u otra.