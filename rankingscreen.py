import pygame
import time
import random

import singletonpausa
import singletonsesion
import supportfunciones
import textcreator
import peticiones

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

def game_guia():
    intro = True

    while intro == True:
        #font = pygame.font.SysFont(None,10)
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                supportfunciones.quit_juego()
        textLinea = []  

        jsonRanking = peticiones.mostrarRanking()        
        
        gameDisplay.fill(color.blanco)
        #print(jsonRanking[0]["username"])
        count = 0
        while count < len(jsonRanking):
            for ranking in jsonRanking:
                textLinea.append(ranking["username"] + "  " + str(ranking["score"]))
                count = count + 1

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
        
        
