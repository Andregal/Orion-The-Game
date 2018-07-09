import pygame
import sys

# Singleton
class stateConfigure:
    instancia = None

    #se va crear un dictionario que va contener las configuraciones(values)
    #para cada una de las tres dificultades(key): facil, intermedio, dificil
    #cada entrada del dictionario va a ser una dificultad
    #cada dificultad va a tener una lista que posee 3 listas que representan
    #los 3 tipos de NPCs: enemigos, huecos y baterias
    #las listas de NPCs tendran estos valores: cantidad, velocidad, tamanho
    #finalmente, cada dificultad tendra un ultimo valor que representa
    #hasta que puntaje sera valido esa dificultad
    
    enemigos = [2, 15, 1]
    huecos = [2, 15, 1]
    baterias = [1, 10, 1]


    facil = []
    facil.append(enemigos)
    facil.append(huecos)
    facil.append(baterias)
    facil.append(5)

    intermedio = []
    intermedio.append(enemigos)
    intermedio.append(huecos)
    intermedio.append(baterias)
    intermedio.append(20)    

    dificil = []
    dificil.append(enemigos)
    dificil.append(huecos)
    dificil.append(baterias)
    dificil.append(sys.maxsize)

    configurador = {}
    configurador['facil'] = facil
    configurador['intermedio'] = intermedio
    configurador['dificil'] = dificil
    
    @classmethod
    def get_instance(cls):
        if cls.instancia == None:
            cls.instancia = stateConfigure()
        return cls.instancia
    
