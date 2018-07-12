import pygame
import time
import random

import singletonpausa
import singletonsesion
import singletonconfigurador
import supportfunciones
import textcreator


import crashscreen
import pausescreen
import gamescreen
import oriongame


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

def game_configuration():
    intro = True
    
    
    while intro == True:
        #font = pygame.font.SysFont(None,10)
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                supportfunciones.quit_juego()
        textLinea = []  

        gameDisplay.fill(color.blanco)
        textLinea.append("Bienvenido a Orion: The Game!")
        textLinea.append("Orion: The Game es un pequeño juego desarrollado")
        textLinea.append("para nuestro curso de Ingenieria de Sistemas")
        textLinea.append("Los controles del juego son sencillos:")
        textLinea.append("Presiona M para pausar o reanudar la musica y P para pausar o reanudar la partida")
        textLinea.append("Cada vez que esquivas un enemigo, tu puntaje incrementa por 1")
        textLinea.append("Si logras recoger una pila, podras resistir un choque mas")
        textLinea.append("Sin embargo, ten cuidado con los huecos, estos pueden privarte del movimiento")
        textLinea.append("Trata de esquivar la mayor cantidad de enemigo para alcanzar un highscore!")

        count = 1
        for text in textLinea:
            font = pygame.font.SysFont(None,30)
            #texto = font.render(text, True, (0,0,0))
            textSuperficie, textRect = textcreator.objetos_texto(text, font)
            gameDisplay.blit(textSuperficie, (20,count*30))
            count = count +1

        params = supportfunciones.paramBotones(0.5*display_ancho,0.8*display_altura,0.2*display_ancho,50,color.verde,color.verde_oscuro)
        
        dManager.boton("Regresar", params, None, oriongame.game_intro)

        pygame.display.update()
        clock.tick(15)
        
        
