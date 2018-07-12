import pygame


# Singleton
class statePause:
    instancia = None

    pausa = False
    
    @classmethod
    def get_instance(cls):
        if cls.instancia == None:
            cls.instancia = statePause()
        return cls.instancia
    
