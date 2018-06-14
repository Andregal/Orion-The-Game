import pygame
import time
import random
import threading

import singletonpausa
import supportfunciones
import textcreator

import crashscreen
import pausescreen
import gamescreen


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
timeStun = 0

#pantalla de juego inicial
def game_bucle():

    #global pausa
    estadoPausa = singletonpausa.statePause.get_instance()
    musicaPausa = 0
    #coordenadas iniciales del carro
    x = (display_ancho * 0.45)
    y = (display_altura * 0.8)
    #indica por cuantas coordinadas se mueve en el eje X
    x_cambio = 0
    y_cambio = 0

    #se crea el bus del jugador
    car_ancho = 100
    car_altura = 100
    busPlayer = supportfunciones.Bus(car_ancho, car_altura)
    carImg = busPlayer.cargarBus("orionbus_nuevo.png")
    #dj de canciones
    musicDJ = supportfunciones.MusicManager()
    
    #pygame.key.set_repeat(10,10)
    musicDJ.tocarMusica("music/musica.mp3", -1)
    #modificar la velocidad de obstaculos para aumentar la dificultad
    listaObs = []
    obs_speed= 15
    obs_ancho= car_ancho
    obs_altura = car_altura
    obs_startX= random.randrange(0+car_ancho,display_ancho-car_ancho)
    obs_startY= -500
    obs_buff1X= random.randrange(0+car_ancho,display_ancho-car_ancho)
    obs_buff1Y= random.randrange(-3000, -1000)
    obs_buff2X= random.randrange(0+car_ancho,display_ancho-car_ancho)
    obs_buff2Y= random.randrange(-3000, -1000)
    obsEne= supportfunciones.Obstaculo(obs_startX, obs_startY, obs_ancho, obs_altura, "enemigo")
    obsHue= supportfunciones.Obstaculo(obs_buff1X, obs_buff1Y, obs_ancho/2, obs_altura/2, "hueco")
    obsEsc= supportfunciones.Obstaculo(obs_buff2X, obs_buff2Y, obs_ancho/2, obs_altura/2, "escudo")
    listaObs.append(obsEne)
    listaObs.append(obsHue)
    listaObs.append(obsEsc)
    enemigoPlayer = supportfunciones.Bus(obsEne.ancho, obsEne.altura)
    enemigoImg = enemigoPlayer.cargarBus("orion_enemigo.png")
    escudoBuff = False
    estadoStun = False
    timerStart = False
    #el usuario no podra pausar mientras que este en movimiento
    estado_mov = False
    #puntaje
    esquivado = 0
    
    gameExit = False

    #main game - bucle
    while not gameExit:
        #event - bucle
        for event in pygame.event.get():
            #quit = boton X en la ventana de juego
            if event.type == pygame.QUIT:
                supportfunciones.quit_juego()
            #print(event)
            #keydown = tecla presionada
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_cambio = -40
                    estado_mov = True
                if event.key == pygame.K_RIGHT:
                    x_cambio = 40
                    estado_mov = True
                if event.key == pygame.K_UP:
                    y_cambio = -40
                    estado_mov = True
                if event.key == pygame.K_DOWN:
                    y_cambio = 40
                    estado_mov = True
                if event.key == pygame.K_p:
                    if estado_mov == False:
                        estadoPausa.pausa = True
                        pausescreen.pausado()
                if event.key == pygame.K_m:
                    if estado_mov == False:
                        if musicaPausa == 0:
                            musicDJ.pausarMusica()
                            musicaPausa = 1
                        elif musicaPausa == 1:
                            musicDJ.resumirMusica()
                            musicaPausa = 0
            #keyup = se deja de presionar tecla
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_cambio = 0
                    estado_mov = False
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_cambio = 0
                    estado_mov = False
        
        
        if estadoStun == True and pygame.time.get_ticks() - timeStun <= 2000 and timeStun != 0:
            x_cambio = 0
            y_cambio = 0

        x += x_cambio
        y += y_cambio

        #gameDisplay.fill(blanco)
        fondo = pygame.image.load("images/pista.jpg")
        fondo = pygame.transform.scale(fondo, (display_ancho, display_altura))
        gameDisplay.blit(fondo, (0,0))
        #actualizar las coordinadas del carro y del obstaculo
##        dManager.cargarobstaculo(obsEne, color.azul)

        dManager.cargarobstaculo(obsHue, color.rojo)
        dManager.cargarobstaculo(obsEsc, color.verde)

        #simula velocidad del obstaculo, se mueve en el eje Y
        #obsEne.y += obs_speed
        for obstaculo in listaObs:
            obstaculo.y += obs_speed

        dManager.car(carImg,x,y)
        dManager.car(enemigoImg, obsEne.x, obsEne.y)
        dManager.obs_esquivados(esquivado)

        #verifica si el carro se choca con los bordes
        if x > display_ancho - car_ancho or x < 0:
            musicDJ.pararMusica()
            musicDJ.tocarMusica("music/crash.mp3", 0)
            crashscreen.crash(esquivado)
        if y > display_altura - car_altura:
            y=display_altura - car_altura
        elif y < 0:
            y=0
        #simula obstaculos infinitos al regresarlo al comienzo si desaperece
        #de la pantalla, y se agrega un punto al puntaje

        for obstaculo in listaObs:
            if obstaculo.y > display_altura:
                if obstaculo.tipo == "enemigo":
                    obstaculo.y = 0 - obstaculo.altura
                else:
                    obstaculo.y = random.randrange(-3000, -1000)
                obstaculo.x = random.randrange(0 + obstaculo.ancho, display_ancho-obstaculo.ancho)
                esquivado = esquivado + 1
                obs_speed = obs_speed + 2  
            
        #logica de crash:
        #Y de carro es menor que la altura del obstaculo MAS la coordenada
        #del obstaculo, en otras palabras, obstaculo esta dentro del carro

        for obstaculo in listaObs:           
            if obstaculo.tipo == "enemigo":
                if y < obstaculo.y + obstaculo.altura and y + car_altura > obstaculo.y:
                    #Eye X del carro debe rozar con una de las esquinas de X
                    #o debe chocar con el borde de inferior del obstaculo
                    #SI esquina izquierda del carro es mayor que la esquina izquierda del obstaculo
                    #MAS la esquina izquierda del carro es menor que la esquina derecha del obstaculo
                    #O la esquina derecha del carro es mayor que la esquina izquierda del obstaculo
                    #MAS la esquina derecha del carro es menor que la esquina derecha del obstaculo
                    if x + car_ancho > obstaculo.x and x < obstaculo.x + obstaculo.ancho:
                    #Si tiene escudo, mata el enemigo, gana un punto y pierde su escudo
                        if escudoBuff == False:
                            musicDJ.pararMusica()
                            musicDJ.tocarMusica("music/crash.mp3", 0)
                            crashscreen.crash(esquivado)
                        elif escudoBuff == True:
                            obstaculo.y = 0 - obstaculo.altura
                            obstaculo.x = random.randrange(0 + obstaculo.ancho, display_ancho-obstaculo.ancho)
                            esquivado = esquivado + 1
                            escudoBuff = False

            elif obstaculo.tipo == "escudo":
                if y < obstaculo.y + obstaculo.altura and y + car_altura > obstaculo.y:
                    if x + car_ancho > obstaculo.x and x < obstaculo.x + obstaculo.ancho:
                    #Si tiene escudo, mata el enemigo, gana un punto y pierde su escudo
                        escudoBuff = True
                        obstaculo.y = random.randrange(-3000, -1000)
                        obstaculo.x = random.randrange(0 + obstaculo.ancho, display_ancho-obstaculo.ancho)
            elif obstaculo.tipo == "hueco":
                if y < obstaculo.y + obstaculo.altura and y + car_altura > obstaculo.y:
                    if x + car_ancho > obstaculo.x and x < obstaculo.x + obstaculo.ancho:
                    #Si tiene escudo, mata el enemigo, gana un punto y pierde su escudo
                    #stun por 2 segundos
                        estadoStun = True
                        timeStun=pygame.time.get_ticks()
                        obstaculo.y = random.randrange(-3000, -1000)
                        obstaculo.x = random.randrange(0 + obstaculo.ancho, display_ancho-obstaculo.ancho)

        #actualizar el display
        pygame.display.update()
        clock.tick(60)
