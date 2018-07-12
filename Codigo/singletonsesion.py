import pygame

# Singleton
class datosSesion:
    instancia = None

    nombreUsuario = ""
    contrasena = ""
    score = 0

    qRespuesta = None
    
    @classmethod
    def get_instance(cls):
        if cls.instancia == None:
            cls.instancia = datosSesion()
        return cls.instancia
    
