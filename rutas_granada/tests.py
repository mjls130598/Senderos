from django.test import TestCase
from rutas_granada.models import *

# Tests relacionados con el modelo Comentario

class ExcursiónTestCase(TestCase):
    def setUp(self):
        comentarios = [
            {
                "contenido" : 'Primer comentario',
                "autor" : 'Yo'
            },
            {
                "contenido" : 'Otro comentario',
                "autor" : 'Pepito'
            }
        ]

        fotos = [
            {
                "foto" : "./prado.png",
                "pie" : "Prado verde"
            }
        ]

        excursión = Excursión(nombre="Test", descripción="asfd asf asdf", likes=1, 
                            tags=['fácil'], comentarios=comentarios, fotos=fotos)
        excursión.save() # Para escribir en la BD
    def test(self):
        excursion = Excursión.objects.get(nombre="Test")
        self.assertEquals(excursion.comentarios[0].contenido, "Primer comentario")
        excursion.delete()


