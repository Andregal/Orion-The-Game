import pygame
import time
import random

import singletonpausa
import singletonsesion
import singletonconfigurador
import supportfunciones
import textcreator
import transfercreator
import supportfunciones


import crashscreen
import pausescreen
import gamescreen
import mediumconfscreen
import hardconfscreen
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
conf = singletonconfigurador.stateConfigure.get_instance().configurador

    
sesion = singletonsesion.datosSesion.get_instance()

def game_configuration():
    intro = True
    
    
    while intro == True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #font = pygame.font.SysFont(None,10)
        for event in pygame.event.get():
            #print(event)

            if event.type == pygame.QUIT:
                supportfunciones.quit_juego()
            if event.type == pygame.KEYDOWN:
                if 57 >= event.key >= 48 and len(sesion.nombreUsuario) <= 10:
                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (90+25) > mouse[1] and 90 < mouse[1]:
                        if click[0] == 1:
                            confTemp[0]= str(event.key - 48)
                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (120+25) > mouse[1] and 120 < mouse[1]:
                        if click[0] == 1:
                           confTemp[1]= str(event.key - 48)
                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (150+25) > mouse[1] and 150 < mouse[1]:
                        if click[0] == 1:
                            confTemp[2]= str(event.key - 48)
                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (180+25) > mouse[1] and 180 < mouse[1]:
                        if click[0] == 1:
                            confTemp[3]= str(event.key - 48)
                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (210+25) > mouse[1] and 210 < mouse[1]:
                        if click[0] == 1:
                            confTemp[4]= str(event.key - 48)
                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (240+25) > mouse[1] and 240 < mouse[1]:
                        if click[0] == 1:
                            confTemp[5]= str(event.key - 48)
                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (270+25) > mouse[1] and 270 < mouse[1]:
                        if click[0] == 1:
                            confTemp[6]= str(event.key - 48)
                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (300+25) > mouse[1] and 300 < mouse[1]:
                        if click[0] == 1:
                            confTemp[7]= str(event.key - 48)
                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (330+25) > mouse[1] and 330 < mouse[1]:
                        if click[0] == 1:
                            confTemp[8]= str(event.key - 48)
                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (360+25) > mouse[1] and 360 < mouse[1]:
                        if click[0] == 1:
                            confTemp[9]= str(event.key - 48)
##                elif event.unicode == "\x08":
##                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (90+25) > mouse[1] and 90 < mouse[1] and confTemp[0] != "":
##                        if click[0] == 1:
##                            confTemp = confTemp[:-1]
##                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (120+25) > mouse[1] and 120 < mouse[1] and confTemp[1] != "":
##                        if click[0] == 1:
##                            confTemp = confTemp[:-1]
##                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (150+25) > mouse[1] and 150 < mouse[1] and confTemp[2] != "":
##                        if click[0] == 1:
##                            confTemp = confTemp[:-1]
##                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (180+25) > mouse[1] and 180 < mouse[1] and confTemp[3] != "":
##                        if click[0] == 1:
##                            confTemp = confTemp[:-1]
##                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (210+25) > mouse[1] and 210 < mouse[1] and confTemp[4] != "":
##                        if click[0] == 1:
##                            confTemp = confTemp[:-1]
##                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (240+25) > mouse[1] and 240 < mouse[1] and confTemp[5] != "":
##                        if click[0] == 1:
##                            confTemp = confTemp[:-1]
##                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (270+25) > mouse[1] and 270 < mouse[1] and confTemp[6] != "":
##                        if click[0] == 1:
##                            confTemp = confTemp[:-1]
##                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (300+25) > mouse[1] and 300 < mouse[1] and confTemp[7] != "":
##                        if click[0] == 1:
##                            confTemp = confTemp[:-1]
##                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (330+25) > mouse[1] and 330 < mouse[1] and confTemp[8] != "":
##                        if click[0] == 1:
##                            confTemp = confTemp[:-1]
##                    if (0.8*display_ancho+0.15*display_ancho) > mouse[0] and 0.8*display_ancho < mouse[0] and (360+25) > mouse[1] and 360 < mouse[1] and confTemp[9] != "":
##                        if click[0] == 1:
##                            confTemp = confTemp[:-1]
                
            textLinea = []  

            gameDisplay.fill(color.blanco)
            textLinea.append("CONFIGURADOR")
            textLinea.append("DIFICULTAD: FACIL")
            textLinea.append("NO USAR BAJO CONSTRUCCION")
            textLinea.append("CANTIDAD DE VEHICULOS ENEMIGOS:")
            textLinea.append("VELOCIDAD DE VEHICULOS ENEMIGOS:")
            textLinea.append("TAMAÑO (0.8*TAMAÑO PLAYER BUS) DE VEHICULOS ENEMIGOS:")
            textLinea.append("CANTIDAD DE HUECOS:")
            textLinea.append("VELOCIDAD DE HUECOS:")
            textLinea.append("TAMAÑOS DE HUECOS:")
            textLinea.append("CANTIDAD DE BATERIAS:")
            textLinea.append("VELOCIDAD DE BATERIAS:")
            textLinea.append("TAMAÑO DE BATERIAS:")


            count= 0
            count2= 0
            for text in textLinea:
                font = pygame.font.SysFont(None,30)
                #texto = font.render(text, True, (0,0,0))
                textSuperficie, textRect = textcreator.objetos_texto(text, font)
                gameDisplay.blit(textSuperficie, (20,(count+1)*30))
                if count >=3:
                    params = supportfunciones.paramBotones(0.8*display_ancho,(count+1)*30,0.15*display_ancho,25,color.azul,color.azul_oscuro)
                    dManager.boton(str(confTemp[count-2]),params, None, None)
                count = count +1               
            
            params = supportfunciones.paramBotones(0.2*display_ancho,0.8*display_altura,0.2*display_ancho,50,color.verde,color.verde_oscuro)
            params2 = supportfunciones.paramBotones(0.5*display_ancho,0.8*display_altura,0.2*display_ancho,50,color.verde,color.verde_oscuro)

            if((0.5*display_ancho+0.2*display_ancho) > mouse[0] and 0.5*display_ancho < mouse[0]) and (0.8*display_altura+50 > mouse[1] and 0.8*display_altura< mouse[1]):
                count = 0
                for key, value in  conf.items():
                    if key == "facil":
                        for val in value:
                            if isinstance(val,(list,)):
                                while count <= 2:
                                    print("----------")
                                    print(val[count])
                                    print(confTemp[count+1])
                                    val[count] =  confTemp[count]
                                    count = count +1
                                count = 0
                            else:
                                val = confTemp[9]
                
            dManager.boton("Regresar", params, None, oriongame.game_intro)
            dManager.boton("Continuar", params2, None, mediumconfscreen.game_configuration)
    
            pygame.display.update()
            clock.tick(15)
            
        
