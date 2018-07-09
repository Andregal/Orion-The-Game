import pygame
import supportfunciones
import singletonpausa
import textcreator

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

#menu de pausa
def pausado():
    
    #global pausa
    estadoPausa = singletonpausa.statePause.get_instance()
    while estadoPausa.pausa == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                supportfunciones.quit_juego()

        #se puede omitir la funcion fill para ver el estado del juego pausado   
        gameDisplay.fill(color.blanco)
        textoFuente = pygame.font.Font("freesansbold.ttf", 50)
        textSuperficie, textRect = textcreator.objetos_texto("Juego Pausado", textoFuente)
        textRect.center = ((display_ancho/2), (display_altura/2))
        gameDisplay.blit(textSuperficie, textRect)

        params1 = supportfunciones.paramBotones(0.1875*display_ancho,0.6*display_altura,0.1875*display_ancho,65,color.verde,color.verde_oscuro)
        params2 = supportfunciones.paramBotones(0.625*display_ancho,0.6*display_altura,0.1875*display_ancho,65, color.rojo, color.rojo_oscuro)
        
        dManager.boton("Continuar",params1, None, supportfunciones.continuar)
        dManager.boton("Salir",params2, None,supportfunciones.quit_juego)        

        #actualizar pantalla
        pygame.display.update()
        clock.tick(15)

