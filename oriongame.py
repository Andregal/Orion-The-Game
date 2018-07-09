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
import guidescreen
import rankingscreen

pygame.init()

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

#pantalla de inicio
def game_intro():
    
    sesion = singletonsesion.datosSesion.get_instance()
    userExiste = False        
    intro = True
    
    while intro == True:
        for event in pygame.event.get():
            #agarra el input del usuario y lo concatena
            #NUEVO! nombre de usuario solo puede tener un maximo de 10 caracteres y
            #el usuario puede borrar el ultimo caracter con la tecla backspace/return
            #print (event)
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha() and event.unicode != "\x08" and len(sesion.nombreUsuario) <= 10:
                    sesion.nombreUsuario += event.unicode
                if event.unicode == "\x08" and sesion.nombreUsuario != "":
                    sesion.nombreUsuario = sesion.nombreUsuario[:-1]
            if event.type == pygame.QUIT:
                    supportfunciones.quit_juego()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dManager.boton(sesion.nombreUsuario,params2, None, None)
                    userExiste = True
        #fondo de pantalla, ajustar tamaño con transform.scale
        fondo = pygame.image.load("images/fondo.jpg")
        fondo = pygame.transform.scale(fondo, (display_ancho, display_altura))
        gameDisplay.blit(fondo, (0,0))
        orion = pygame.image.load("images/orion.jpg")
        orion = pygame.transform.scale(orion, (int(display_ancho/4), int(display_altura/4)))
        gameDisplay.blit(orion, (0.375*display_ancho,0.2*display_altura))
        config = pygame.image.load("images/config.png")
        config = pygame.transform.scale(config, (int(display_ancho/15), int(display_ancho/15)))
        gameDisplay.blit(config, (0.009*display_ancho,0.9*display_altura))
        rank = pygame.image.load("images/highscore.png")
        rank = pygame.transform.scale(rank, (int(display_ancho/15), int(display_ancho/15)))
        gameDisplay.blit(rank, (0.93*display_ancho,0.9*display_altura))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if (0.009*display_ancho+display_ancho/15) > mouse[0] and 0.009*display_ancho < mouse[0] and (0.9*display_altura+display_ancho/15) > mouse[1] and 0.9*display_altura < mouse[1]:
            if click[0] == 1:
                guidescreen.game_guia()
                #rankingscreen.game_guia()
        if (0.93*display_ancho+display_ancho/15) > mouse[0] and 0.93*display_ancho < mouse[0] and (0.9*display_altura+display_ancho/15) > mouse[1] and 0.9*display_altura < mouse[1]:
            if click[0] == 1:
                rankingscreen.game_guia()

        textoFuente = pygame.font.Font("freesansbold.ttf", 50)
        textSuperficie, textRect = textcreator.objetos_texto("Orion: The Game", textoFuente)
        textRect.center = ((display_ancho/2), (display_altura/2))
        gameDisplay.blit(textSuperficie, textRect)
        #Logica para ingresar usuario:
        #Va a existir un boton que indique que "ingrese su usuario"
        #Cuando el usuario presione el boton izquierdo del mouse se crea un boton que se va a llenar con el nombre de usuario
        #Para que el usuario no tenga que dejar presionado el mouse, creamos una variable para ver si ya presiono
        #anteriormente el mouse
        params1 = supportfunciones.paramBotones(0.4*display_ancho,0.55*display_altura,0.2*display_ancho,25,color.blanco,color.blanco)
        params2 = supportfunciones.paramBotones(0.4*display_ancho,0.6*display_altura,0.2*display_ancho,25,color.blanco,color.blanco)
        params3 = supportfunciones.paramBotones(0.4*display_ancho,0.65*display_altura,0.2*display_ancho,50,color.verde,color.verde_oscuro)
        params4 = supportfunciones.paramBotones(0.4*display_ancho,0.75*display_altura,0.2*display_ancho,50,color.rojo,color.rojo_oscuro)
        dManager.boton("Ingresar jugador",params1, None, None)
        if userExiste == True:
            dManager.boton(sesion.nombreUsuario,params2, None, None)
        bdquery1 = ["validarUser", sesion.nombreUsuario]
        dManager.boton("Iniciar",params3, None,gamescreen.game_bucle)
        dManager.boton("Salir",params4, None,supportfunciones.quit_juego) 
        #actualizar pantalla
        pygame.display.update()
        clock.tick(15)

def main():
    game_intro()
    
if __name__ == "__main__":
    main()
