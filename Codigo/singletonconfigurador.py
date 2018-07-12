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

    ezEnemyCantidad = 0
    ezEnemyVelocidad = 0
    ezEnemyTamanho = 0
    ezHuecoCantidad = 0
    ezHuecoVelocidad = 0
    ezHuecoTamanho = 0
    ezPilaCantidad = 0
    ezPilaVelocidad = 0
    ezPilaTamanho = 0
    ezPuntaje = 0

    listEz = []
    listEz.append(ezEnemyCantidad)
    listEz.append(ezEnemyVelocidad)
    listEz.append(ezEnemyTamanho)
    listEz.append(ezHuecoCantidad)
    listEz.append(ezHuecoVelocidad)
    listEz.append(ezHuecoTamanho)
    listEz.append(ezPilaCantidad)
    listEz.append(ezPilaVelocidad)
    listEz.append(ezPilaTamanho)
    listEz.append(ezPuntaje)


    medEnemyCantidad = 0
    medEnemyVelocidad = 0
    medEnemyTamanho = 0
    medHuecoCantidad = 0
    medHuecoVelocidad = 0
    medHuecoTamanho = 0
    medPilaCantidad = 0
    medPilaVelocidad = 0
    medPilaTamanho = 0
    medPuntaje = 0

    listMed = []
    listMed.append(medEnemyCantidad)
    listMed.append(medEnemyVelocidad)
    listMed.append(medEnemyTamanho)
    listMed.append(medHuecoCantidad)
    listMed.append(medHuecoVelocidad)
    listMed.append(medHuecoTamanho)
    listMed.append(medPilaCantidad)
    listMed.append(medPilaVelocidad)
    listMed.append(medPilaTamanho)
    listMed.append(medPuntaje)

    difEnemyCantidad = 0
    difEnemyVelocidad = 0
    difEnemyTamanho = 0
    difHuecoCantidad = 0
    difHuecoVelocidad = 0
    difHuecoTamanho = 0
    difPilaCantidad = 0
    difPilaVelocidad = 0
    difPilaTamanho = 0
    difPuntaje = 0

    listDif = []
    listDif.append(difEnemyCantidad)
    listDif.append(difEnemyVelocidad)
    listDif.append(difEnemyTamanho)
    listDif.append(difHuecoCantidad)
    listDif.append(difHuecoVelocidad)
    listDif.append(difHuecoTamanho)
    listDif.append(difPilaCantidad)
    listDif.append(difPilaVelocidad)
    listDif.append(difPilaTamanho)
    listDif.append(difPuntaje)


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
    
