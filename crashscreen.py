import pygame
import time
import random

import singletonpausa
import singletonsesion
import supportfunciones
import textcreator

import crashscreen
import pausescreen
import gamescreen
import oriongame


#VARIABLES 
color = supportfunciones.colorPalette()   
display_ancho = 900
display_altura = 600    
#la ventana de juego
gameDisplay = pygame.display.set_mode((display_ancho,display_altura))    
pygame.display.set_caption("Orion: The Game")
#gestor de pantalla
dManager = supportfunciones.displayManager(gameDisplay)
#reloj del juego, usado para fps
clock = pygame.time.Clock()
    

#algoritmo de choque
def crash(puntaje):
    #print("Si llega a esta pantalla")
    sesion = singletonsesion.datosSesion.get_instance()
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                supportfunciones.quit_juego()

        #se puede omitir la funcion fill para ver el estado del juego pausado   
        #gameDisplay.fill(blanco)
        fondo = pygame.image.load("images/crash.png")
        fondo = pygame.transform.scale(fondo, (display_ancho, display_altura))
        gameDisplay.blit(fondo, (0,0))

        params1 = supportfunciones.paramBotones(0.4*display_ancho,0.3*display_altura,0.2*display_ancho,40,color.blanco,color.blanco)
        params2 = supportfunciones.paramBotones(0.4*display_ancho,0.5*display_altura,0.2*display_ancho,40,color.blanco,color.blanco)
        params3 = supportfunciones.paramBotones(0.1875*display_ancho,0.6*display_altura,0.1875*display_ancho,40,color.verde,color.verde_oscuro)
        params4 = supportfunciones.paramBotones(0.625*display_ancho,0.6*display_altura,0.1875*display_ancho,40,color.rojo, color.rojo_oscuro)
        params5 = supportfunciones.paramBotones(0.4*display_ancho,0.7*display_altura,0.2*display_ancho,40,color.azul,color.azul_oscuro)
        params6 = supportfunciones.paramBotones(0.4*display_ancho,0.4*display_altura,0.2*display_ancho,40,color.blanco,color.blanco)
            
        dManager.boton("Te chocaste!", params1, None, None)
        dManager.boton(sesion.nombreUsuario, params6, None, None)
        dManager.boton("Tu puntaje: " + str(puntaje), params2, None, None)
        dManager.boton("Nueva Partida", params3, None, gamescreen.game_bucle)
        dManager.boton("Regresar al menu", params5, None, oriongame.game_intro)
        dManager.boton("Salir", params4, None, supportfunciones.quit_juego)        

        #actualizar pantalla
        pygame.display.update()
        clock.tick(15)
