import pygame

# Singleton
class datosSesion:
    instancia = None

    nombreUsuario = ""
    contrasenha = ""
    
    @classmethod
    def get_instance(cls):
        if cls.instancia == None:
            cls.instancia = datosSesion()
        return cls.instancia
    
