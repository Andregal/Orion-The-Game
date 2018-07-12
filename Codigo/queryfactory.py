import pygame
import time
import random
import peticiones

def queryFactory(query, args):
    if query == "validarUser":
        return peticiones.validarExistencia(args)
    elif query == "crearUser":
        return peticiones.crearUsuario(args(0), args(1))
    elif query == "validarPass":
        return peticiones.validarContrasena(args(0), args(1))
    elif query == "actualizarPass":
        return peticiones.actualizarContrasena(args(0), args(1))
    elif query == "getScore":
        return peticiones.obtenerScore(args)
    elif query == "updateScore":
        return peticiones.actualizarScore(args(0), args(1))
    elif query == "showRanking":
        return peticiones.mostrarRanking()
    elif query == "showPositionUser":
        return peticiones.mostrarUsuarioSegunPuesto(args)
    elif query == "showPostion":
        return peticiones.mostrarPosUsuario(args)


def evaluarRespuesta():
    pass
    
