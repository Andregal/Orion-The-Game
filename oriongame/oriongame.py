import pygame
import time
import random

def main():
    pygame.init()

    #VARIABLES
    display_ancho = 800
    display_altura = 600
    
    # mezcla de colores : (rojo, verde, azul)
    negro = (0,0,0)
    blanco = (255,255,255)
    rojo = (255,0,0)
    verde = (0,255,0)
    azul = (0,0,255)

    rojo_oscuro=(200,0,0)
    verde_oscuro=(0,200,0)

    pausa = False

    #la ventana de juego
    gameDisplay = pygame.display.set_mode((800,600))    
    pygame.display.set_caption("Orion: The Game")
    #reloj del juego, usado para fps
    clock = pygame.time.Clock()

    car_ancho = 100
    car_altura = 100
    #cargar el bus
    carImg = pygame.image.load("orionbus_nuevo.png")
    carImg = pygame.transform.scale(carImg, (car_ancho, car_altura))

    #FUNCIONES
    
    #puntaje en el gameDisplay
    def obs_esquivados(count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Esquivado: " +str(count), True, negro)
        gameDisplay.blit(text, (0,0))    

    def obstaculo(obsX, obsY, obsAn, obsAl, color):
        #draw.rect(ValorX, ValorY, Ancho, Altura)
        pygame.draw.rect(gameDisplay, color, [obsX, obsY, obsAn, obsAl])
        
    #clase carro con su valores en eje X y Y
    def car(x,y):
        gameDisplay.blit(carImg,(x,y))

    #algoritmo de choque
    def crash():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_juego()

            #se puede omitir la funcion fill para ver el estado del juego pausado   
            gameDisplay.fill(blanco)
            textoFuente = pygame.font.Font("freesansbold.ttf", 50)
            textSuperficie, textRect = objetos_texto("Te chocaste!", textoFuente)
            textRect.center = ((display_ancho/2), (display_altura/2))
            gameDisplay.blit(textSuperficie, textRect)
       
            boton("Nueva Partida",150,400,200,50,verde,verde_oscuro, game_bucle)
            boton("Salir",450,400,200,50, rojo, rojo_oscuro, quit_juego)        

            #actualizar pantalla
            pygame.display.update()
            clock.tick(15)

    #clase para mostrar el mensaje
    def mostrar_mensaje(texto):
        textoFuente = pygame.font.Font("freesansbold.ttf", 115)    
        textSuperficie, textRect = objetos_texto(texto, textoFuente)
        textRect.center = ((display_ancho/2), (display_altura/2))
        gameDisplay.blit(textSuperficie, textRect)

        pygame.display.update()
        #muestra el mensaje y pausea el juego por 2 segundos
        time.sleep(2)
        #despues se reinicia el juego
        game_bucle()

    #se crea el texto 
    def objetos_texto(text, fuente):
        textSuper = fuente.render(text, True, negro)
        return textSuper, textSuper.get_rect()
        
    #funcion de boton
    #Se pasa el mensaje, valores X e Y, ancho, altura,
    #sus colores en estado activo e inactivo y tipo de accion del boton
    def boton(mensaje,x,y,an,al,cAct,cInact, accion=None):
        #devuelve posicion del mouse en una tupla de 2 valores:
        #(valorX, valorY)
        mouse = pygame.mouse.get_pos()
        #devuelve clicks del mouse en una tupla en valores binarios de 3 valores:
        #(click izquierdo, click rueda, click derecho)
        click = pygame.mouse.get_pressed()
        
        #botones, cambian de color cuando el mouse los toca
        if (x+an) > mouse[0] and x < mouse[0] and (y+al) > mouse[1] and y < mouse[1]:
            pygame.draw.rect(gameDisplay, cAct, (x,y,an,al))
            if click[0] == 1 and accion != None:
                accion()
        else:
            pygame.draw.rect(gameDisplay, cInact, (x,y,an,al))
        
        #texto para los botones
        textoBotones = pygame.font.Font("freesansbold.ttf", 20)
        textSup, textRect = objetos_texto(mensaje, textoBotones)
        textRect.center = ((x+(an/2)), (y+(al/2)))
        gameDisplay.blit(textSup, textRect)


    def quit_juego():
        pygame.quit()
        quit()

    def continuar():
        global pausa
        pausa = False
    
    #JUEGO - INTERFACES

    #menu de inicio


    def pausado():
        
        global pausa
        while pausa == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_juego()

            #se puede omitir la funcion fill para ver el estado del juego pausado   
            #gameDisplay.fill(blanco)
            textoFuente = pygame.font.Font("freesansbold.ttf", 50)
            textSuperficie, textRect = objetos_texto("Juego Pausado", textoFuente)
            textRect.center = ((display_ancho/2), (display_altura/2))
            gameDisplay.blit(textSuperficie, textRect)
       
            boton("Continuar",150,400,100,50,verde,verde_oscuro, continuar)
            boton("Salir",550,400,100,50, rojo, rojo_oscuro, quit_juego)        

            #actualizar pantalla
            pygame.display.update()
            clock.tick(15)
        
    def game_intro():

        intro = True

        while intro == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_juego()
                    
            gameDisplay.fill(blanco)
            textoFuente = pygame.font.Font("freesansbold.ttf", 50)
            textSuperficie, textRect = objetos_texto("Orion: The Game", textoFuente)
            textRect.center = ((display_ancho/2), (display_altura/2))
            gameDisplay.blit(textSuperficie, textRect)
       
            boton("Iniciar",150,400,100,50,verde,verde_oscuro, game_bucle)
            boton("Salir",550,400,100,50, rojo, rojo_oscuro, quit_juego)        

            #actualizar pantalla
            pygame.display.update()
            clock.tick(15)


    def game_bucle():

        global pausa 
        #coordenadas iniciales del carro
        x = (display_ancho * 0.45)
        y = (display_altura * 0.8)
        #indica por cuantas coordinadas se mueve en el eje X
        x_cambio = 0

        #coordinadas de obstaculos
        obs_startX= random.randrange(0,display_ancho)
        obs_startY= -500
        #modificar la velocidad para aumentar la dificultad
        obs_speed= 3
        obs_ancho= 100
        obs_altura = 100

        #puntaje
        esquivado = 0
        
        gameExit = False

        #main game - bucle
        while not gameExit:
            #event - bucle
            for event in pygame.event.get():
                #quit = boton X en la ventana de juego
                if event.type == pygame.QUIT:
                    quit_juego()
                #print(event)
                #keydown = tecla presionada
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_cambio = -5
                    if event.key == pygame.K_RIGHT:
                        x_cambio = 5
                    if event.key == pygame.K_p:
                        pausa = True
                        pausado()
                #keyup = se deja de presionar tecla
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_cambio = 0
                
            x += x_cambio
            gameDisplay.fill(blanco)
            #actualizar las coordinadas del carro y del obstaculo
            obstaculo(obs_startX, obs_startY, obs_ancho, obs_altura, azul)
            #simula velocidad del obstaculo, se mueve en el eje Y
            obs_startY += obs_speed
            car(x,y)
            obs_esquivados(esquivado)

            #el carro se choca con los bordes
            if x > display_ancho - car_ancho or x < 0:
                crash()
                
            #simula obstaculos infinitos al regresarlo al comienzo si desaperece
            #de la pantalla, y se agrega un punto al puntaje
            if obs_startY > display_altura:
                obs_startY = 0 - obs_altura
                obs_startX = random.randrange(0, display_ancho)
                esquivado = esquivado + 1
                obs_speed = obs_speed +0.5
                
            #logica de crash:
            #Y de carro es menor que la altura del obstaculo MAS la coordenada
            #del obstaculo, en otras palabras, obstaculo esta dentro del carro
            if y < obs_startY + obs_altura:
                #Eye X del carro debe rozar con una de las esquinas de X
                #o debe chocar con el borde de inferior del obstaculo
                #SI esquina izquierda del carro es mayor que la esquina izquierda del obstaculo
                #MAS la esquina izquierda del carro es menor que la esquina derecha del obstaculo
                #O la esquina derecha del carro es mayor que la esquina izquierda del obstaculo
                #MAS la esquina derecha del carro es menor que la esquina derecha del obstaculo
                if x + car_ancho > obs_startX and x < obs_startX + obs_ancho:
                #if x > obs_startX and x < obs_startX + obs_ancho or x+car_ancho > obs_startX and x+car_ancho < obs_startX+obs_ancho:
                    crash()
            #actualizar el display
            pygame.display.update()
            clock.tick(60)

    game_intro()
    game_bucle()
    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main()
