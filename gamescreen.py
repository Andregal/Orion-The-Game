import pygame
import time
import random
import threading

import singletonpausa
import supportfunciones
import singletonconfigurador
import textcreator
import obstaclecreator

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
    x = (display_ancho * 0.2)
    y = (display_altura * 0.45)
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

    #se crea un lista con todos los obstaculos configurados y se cargan sus imagenes
    conf = singletonconfigurador.stateConfigure.get_instance().configurador
    listObst = obstaclecreator.agregarNPC(conf, car_ancho, car_altura, display_ancho, display_altura)
    dictPunt = obstaclecreator.agregarPuntaje(conf, car_ancho, car_altura, display_ancho, display_altura)
    #print(conf)    
    listImg = []
    for obs in listObst:
        if obs.tipo == "enemigo":
            player = supportfunciones.Bus(int(obs.ancho), int(obs.altura))
            img = player.cargarBus("orion_enemigo.png")
            listImg.append(img)
        elif obs.tipo == "hueco":
            player = supportfunciones.Bus(int(obs.ancho), int(obs.altura))
            img = player.cargarBus("orion_hueco.png")
            listImg.append(img)
        elif obs.tipo == "pila":
            player = supportfunciones.Bus(int(obs.ancho), int(obs.altura))
            img = player.cargarBus("orion_pila.png")
            listImg.append(img)
    
    escudoBuff = False
    estadoStun = False
    timerStart = False
    stageTipo = "FACIL"
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
                    x_cambio = -20
                    estado_mov = True
                if event.key == pygame.K_RIGHT:
                    x_cambio = 20
                    estado_mov = True
                if event.key == pygame.K_UP:
                    y_cambio = -20
                    estado_mov = True
                if event.key == pygame.K_DOWN:
                    y_cambio = 20
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
        fondo = pygame.transform.rotate(fondo, 90)
        fondo = pygame.transform.scale(fondo, (display_ancho, display_altura))
        gameDisplay.blit(fondo, (0,0))
        #actualizar las coordinadas del carro y del obstaculo

        #simula velocidad del obstaculo, se mueve en el eje X
        #obstaculo.x -= obs_speed
        imgCount = 0        
        if esquivado <= dictPunt.get("facil"):
            stageTipo = "FACIL"
        elif dictPunt.get("facil") <= esquivado + 1 <= dictPunt.get("intermedio"):
            stageTipo = "INTERMEDIO"
        elif esquivado +1 >= dictPunt.get("intermedio"):
            stageTipo = "DIFICIL"
        dManager.car(carImg,x,y)

        #logica de movimiento
        #en la primera stage "FACIL" solo se mueven los obstaculos configuradas para la etapa facil
        #en la segunda stage "INTERMEDIO" se mueven los obstaculos facil e intermedio, porque pueden
        #existir obstaculos faciles que estan en la pantalla durante la transicion de facil a intermedio
        #NO pueden moverse obstaculos de dificultad dificil en este etapa
        #en la etapa dificil ya no hay limitacion
        #si esta en estado terminado YA NO SE MUEVE
        for index, obstaculo in enumerate(listObst, start=0):
            if obstaculo.estadoTerminado == False or obstaculo.x <= display_ancho:
                if stageTipo == "FACIL" and obstaculo.dificultad == "facil":
                    obstaculo.x -= obstaculo.velocidad
                    dManager.car(listImg[index],obstaculo.x,obstaculo.y)
                elif stageTipo == "INTERMEDIO" and obstaculo.dificultad == "intermedio" or obstaculo.dificultad == "facil":
                    obstaculo.x -= obstaculo.velocidad
                    dManager.car(listImg[index],obstaculo.x,obstaculo.y)
                elif stageTipo == "DIFICIL":
                    obstaculo.x -= obstaculo.velocidad
                    dManager.car(listImg[index],obstaculo.x,obstaculo.y)
            
        if esquivado <= dictPunt.get("facil"):
            stageTipo = "FACIL"
        elif dictPunt.get("facil") <= esquivado + 1 <= dictPunt.get("intermedio"):
            stageTipo = "INTERMEDIO"
        elif esquivado +1 >= dictPunt.get("intermedio"):
            stageTipo = "DIFICIL"
        dManager.obs_esquivados(esquivado, escudoBuff, stageTipo)
        #verifica si el carro se choca con los bordes
        if y + car_altura > display_altura or y < 0:
            musicDJ.pararMusica()
            musicDJ.tocarMusica("music/crash.mp3", 0)
            crashscreen.crash(esquivado)
        if x + car_ancho > display_ancho:
            x=display_ancho - car_ancho
        elif x < 0:
            x=0

        #simula obstaculos infinitos al regresarlo al comienzo si desaperece
        #de la pantalla, y se agrega un punto al puntaje
        #Si es enemigo se agrega un punto
        #AQUELLOS QUE YA PERTENECEN A LA DIFICULTAD SE LES CAMBIA
        #A ESTADO TERMINADO TRUE PARA QUE NO SE MUEVAN
        for obstaculo in listObst:
            if obstaculo.x + obstaculo.ancho < 0:
                if obstaculo.tipo == "enemigo":
                    esquivado += 1
                    if stageTipo == "FACIL" and obstaculo.dificultad == "facil":
                        obstaculo.x = display_ancho+random.randrange(200,600)
                        obstaculo.y = random.randrange(0+car_altura,display_altura-car_altura)
                    elif stageTipo == "INTERMEDIO" and obstaculo.dificultad == "intermedio":
                        obstaculo.x = display_ancho+random.randrange(200,600)
                        obstaculo.y = random.randrange(0+car_altura,display_altura-car_altura)
                    elif stageTipo == "DIFICIL" and obstaculo.dificultad == "dificil":
                        obstaculo.x = display_ancho+random.randrange(200,600)
                        obstaculo.y = random.randrange(0+car_altura,display_altura-car_altura)
                    else:
                        obstaculo.x = display_ancho+random.randrange(200,600)
                        obstaculo.y = random.randrange(0+car_altura,display_altura-car_altura)
                        obstaculo.estadoTerminado = True
                else:
                    if stageTipo == "FACIL" and obstaculo.dificultad == "facil":
                        obstaculo.x = display_ancho+random.randrange(500,2000)
                        obstaculo.y = random.randrange(0+car_altura,display_altura-car_altura)
                    elif stageTipo == "INTERMEDIO" and obstaculo.dificultad == "intermedio":
                        obstaculo.x = display_ancho+random.randrange(500,2000)
                        obstaculo.y = random.randrange(0+car_altura,display_altura-car_altura)
                    elif stageTipo == "DIFICIL" and obstaculo.dificultad == "dificil":
                        obstaculo.x = random.randrange(1000, 3000)
                        obstaculo.y = random.randrange(0+car_altura,display_altura-car_altura)
                    else:
                        obstaculo.x = display_ancho+random.randrange(500,2000)
                        obstaculo.y = random.randrange(0+car_altura,display_altura-car_altura)
                        obstaculo.estadoTerminado = True                        
        #logica de crash:
        #Y de carro es menor que la altura del obstaculo MAS la coordenada
        #del obstaculo, en otras palabras, obstaculo esta dentro del carro
        for obstaculo in listObst:           
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
                            obstaculo.y = random.randrange(0+car_altura,display_altura-car_altura)
                            obstaculo.x = display_ancho+random.randrange(200,600)
                            esquivado = esquivado + 1
                            escudoBuff = False
            elif obstaculo.tipo == "pila":
                if y < obstaculo.y + obstaculo.altura and y + car_altura > obstaculo.y:
                    if x + car_ancho > obstaculo.x and x < obstaculo.x + obstaculo.ancho:
                    #Si tiene escudo, mata el enemigo, gana un punto y pierde su escudo
                        escudoBuff = True
                        obstaculo.y = random.randrange(0+car_altura,display_altura-car_altura)
                        obstaculo.x = display_ancho+random.randrange(500,2000)
            elif obstaculo.tipo == "hueco":
                if y < obstaculo.y + obstaculo.altura and y + car_altura > obstaculo.y:
                    if x + car_ancho > obstaculo.x and x < obstaculo.x + obstaculo.ancho:
                    #Si tiene escudo, mata el enemigo, gana un punto y pierde su escudo
                    #stun por 2 segundos
                        estadoStun = True
                        timeStun=pygame.time.get_ticks()
                        obstaculo.y = random.randrange(0+car_altura,display_altura-car_altura)
                        obstaculo.x = display_ancho+random.randrange(500,2000)
        #actualizar el display
        pygame.display.update()
        clock.tick(60)
