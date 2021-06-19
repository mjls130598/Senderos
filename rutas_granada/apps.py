from django.apps import AppConfig


class RutasGranadaConfig(AppConfig):
    name = 'rutas_granada'
 
    def ready(self):
        import rutas_granada.signals
