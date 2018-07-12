import pygame
import time
import random

import singletonpausa
import singletonsesion
import singletonconfigurador
import supportfunciones
import textcreator
import supportfunciones


import crashscreen
import pausescreen
import gamescreen
import oriongame
import singletonconfigurador

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
confTemp = singletonconfigurador.stateConfigure.get_instance().listEz
sesion = singletonsesion.datosSesion.get_instance()

def game_configuration():
    intro = True
    
    
    while intro == True:
        #font = pygame.font.SysFont(None,10)
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                supportfunciones.quit_juego()
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha() and event.unicode != "\x08" and len(sesion.nombreUsuario) <= 10:
                    sesion.nombreUsuario += event.unicode
                
            textLinea = []  

            gameDisplay.fill(color.blanco)
            textLinea.append("CONFIGURADOR")
            textLinea.append("DIFICULTAD: FACIL")
            textLinea.append("")
            textLinea.append("CANTIDAD DE VEHICULOS ENEMIGOS:")
            textLinea.append("VELOCIDAD DE VEHICULOS ENEMIGOS:")
            textLinea.append("TAMAÑO DE VEHICULOS ENEMIGOS:")
            textLinea.append("")
            textLinea.append("CANTIDAD DE HUECOS:")
            textLinea.append("VELOCIDAD DE HUECOS:")
            textLinea.append("TAMAÑOS DE HUECOS:")
            textLinea.append("")
            textLinea.append("CANTIDAD DE BATERIAS:")
            textLinea.append("VELOCIDAD DE BATERIAS:")
            textLinea.append("TAMAÑO DE BATERIAS:")


            count = 0
            for text in textLinea:
                font = pygame.font.SysFont(None,30)
                #texto = font.render(text, True, (0,0,0))
                textSuperficie, textRect = textcreator.objetos_texto(text, font)
                gameDisplay.blit(textSuperficie, (20,(count+1)*30))
                count = count +1
                if count >=2:
                    params = supportfunciones.paramBotones(0.8*display_ancho,(count+1)*30,0.15*display_ancho,25,color.blanco,color.blanco)
                    dManager.boton(sesion.nombreUsuario,params, None, None)
                    

            params = supportfunciones.paramBotones(0.5*display_ancho,0.8*display_altura,0.2*display_ancho,50,color.verde,color.verde_oscuro)
            
            dManager.boton("Regresar", params, None, oriongame.game_intro)

            pygame.display.update()
            clock.tick(15)
            
        
