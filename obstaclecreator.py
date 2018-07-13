import pygame
import sys
import random
import supportfunciones


def agregarNPC(conf, car_ancho, car_altura, display_ancho, display_altura):
    listObst = []
    dictPunt = {}
    listCoord = []
    
    for key, value in conf.items():
        count = 0
        dificultad = key
        for val in value:
            if isinstance(val,(list,)):
                if count == 0:
                    tipo = "enemigo"
                elif count == 1:
                    tipo = "hueco"
                elif count == 2:
                    tipo = "pila"
                cantidad = val[0]
                velocidad = val[1]
                tamanho = val[2]
                ancho = 0.8*car_ancho*tamanho
                altura = 0.8*car_altura*tamanho
                i = 0
                while i < cantidad:
                    if tipo == "enemigo":
                        startX = display_ancho+random.randrange(500,2000)
                    else:
                        startX = display_ancho+random.randrange(1000,3000)
                    startY = random.randrange(0+car_altura,display_altura-car_altura)
                    obstaculo = supportfunciones.Obstaculo(startX, startY, ancho, altura, tipo, dificultad, velocidad)
                    listObst.append(obstaculo)
                    i+= 1
                count += 1
            else:
                dictPunt[key] = val
            
    for obs in listObst:
        print("----------------------------------------")
        print("Posicion X: " + str(obs.x) + " Posicion Y: " + str(obs.y))
        print("Ancho: " + str(obs.ancho) + " Altura: " + str(obs.altura))
        print("Tipo : " + obs.tipo + " Dificultad: " + obs.dificultad + " Velocidad: " + str(obs.velocidad))
        print("----------------------------------------")
    return listObst


def agregarPuntaje(conf, car_ancho, car_altura, display_ancho, display_altura):
    listObst = []
    dictPunt = {}
    listCoord = []
    
    for key, value in conf.items():
        count = 0
        dificultad = key
        for val in value:
            if isinstance(val,(list,)):
                if count == 0:
                    tipo = "enemigo"
                elif count == 1:
                    tipo = "hueco"
                elif count == 2:
                    tipo = "pila"
                cantidad = val[0]
                velocidad = val[1]
                tamanho = val[2]
                ancho = 0.8*car_ancho*tamanho
                altura = 0.8*car_altura*tamanho
                i = 0
                while i < cantidad:
                    if tipo == "enemigo":
                        startX = display_ancho+random.randrange(500,2000)
                    else:
                        startX = display_ancho+random.randrange(1000,3000)
                    startY = random.randrange(0+car_altura,display_altura-car_altura)
                    obstaculo = supportfunciones.Obstaculo(startX, startY, ancho, altura, tipo, dificultad, velocidad)
                    listObst.append(obstaculo)
                    i+= 1
                count += 1
            else:
                dictPunt[key] = val

    return dictPunt
