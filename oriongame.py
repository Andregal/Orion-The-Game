import pygame
import time
import random


def main():
    pygame.init()

    #VARIABLES
    #
    #
    #
    
    display_ancho = 900
    display_altura = 600
    
    # mezcla de colores : (rojo, verde, azul)
    negro = (0,0,0)
    blanco = (255,255,255)
    rojo = (255,0,0)
    verde = (0,255,0)
    azul = (0,0,255)

    rojo_oscuro=(200,0,0)
    verde_oscuro=(0,200,0)


    #la ventana de juego
    gameDisplay = pygame.display.set_mode((display_ancho,display_altura))    
    pygame.display.set_caption("Orion: The Game")
    #reloj del juego, usado para fps
    clock = pygame.time.Clock()

    car_ancho = 100
    car_altura = 100
    #cargar el bus
    carImg = pygame.image.load("orionbus_nuevo.png")
    carImg = pygame.transform.scale(carImg, (car_ancho, car_altura))

    #FUNCIONES
    #
    #
    #
    
    #puntaje en el gameDisplay
    def obs_esquivados(count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Puntaje: " +str(count) + ", presione P para pausar el juego y presione M para pausar/continuar la música", True, negro)
        gameDisplay.blit(text, (0,0))    

    def obstaculo(obsX, obsY, obsAn, obsAl, color):
        #draw.rect(ValorX, ValorY, Ancho, Altura)
        pygame.draw.rect(gameDisplay, color, [obsX, obsY, obsAn, obsAl])
        
    #clase carro con su valores en eje X y Y
    def car(x,y):
        gameDisplay.blit(carImg,(x,y))

    #algoritmo de choque
    def crash(puntaje):
        while True:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    quit_juego()

            #se puede omitir la funcion fill para ver el estado del juego pausado   
            #gameDisplay.fill(blanco)
            fondo = pygame.image.load("images/crash.png")
            fondo = pygame.transform.scale(fondo, (display_ancho, display_altura))
            gameDisplay.blit(fondo, (0,0))
##            textoFuente = pygame.font.Font("freesansbold.ttf", 50)
##            textSuperficie, textRect = objetos_texto("Te chocaste!", textoFuente)
##            textRect.center = ((display_ancho/2), (0.3*display_altura))
##            gameDisplay.blit(textSuperficie, textRect)
##
##            textoFuente = pygame.font.Font("freesansbold.ttf", 50)
##            textSuperficie, textRect = objetos_texto("Tu puntaje: " + str(puntaje), textoFuente)
##            textRect.center = ((display_ancho/2), (0.5*display_altura))
##            gameDisplay.blit(textSuperficie, textRect)


            boton("Te chocaste!",0.4*display_ancho,0.3*display_altura,0.2*display_ancho,65,blanco,blanco, None)
            boton("Tu puntaje: " + str(puntaje),0.4*display_ancho,0.5*display_altura,0.2*display_ancho,65,blanco,blanco, None)
            boton("Nueva Partida",0.1875*display_ancho,0.6*display_altura,0.1875*display_ancho,65,verde,verde_oscuro, game_bucle)
            boton("Salir",0.625*display_ancho,0.6*display_altura,0.1875*display_ancho,65, rojo, rojo_oscuro, quit_juego)        

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
        #time.sleep(2)
        #despues se reinicia el juego
        game_bucle()

    #se crea el texto 
    def objetos_texto(text, fuente):
        textSuper = fuente.render(text, True, negro)
        return textSuper, textSuper.get_rect()
        
    #funcion de boton
    #Se pasa el mensaje, valores X e Y, ancho, altura,
    #sus colores en estado activo e inactivo y tipo de accion del boton(debe ser funcion)
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

    def loadify(img):
        return pygame.image.load(img).convert_alpha()

    #dj de canciones

    def tocarMusica(ubicacionSound, veces):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.load(ubicacionSound)
        pygame.mixer.music.play(veces)

    def pararMusica():
        pygame.mixer.music.stop()

    def pausarMusica():
        pygame.mixer.music.pause()

    def resumirMusica():
        pygame.mixer.music.unpause()

    
    #JUEGO - INTERFACES
    #
    #
    #

    #menu de pausa
    def pausado():
        
        global pausa
        while pausa == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_juego()

            #se puede omitir la funcion fill para ver el estado del juego pausado   
            gameDisplay.fill(blanco)
            textoFuente = pygame.font.Font("freesansbold.ttf", 50)
            textSuperficie, textRect = objetos_texto("Juego Pausado", textoFuente)
            textRect.center = ((display_ancho/2), (display_altura/2))
            gameDisplay.blit(textSuperficie, textRect)
       
            boton("Continuar",0.1875*display_ancho,0.6*display_altura,0.1875*display_ancho,65,verde,verde_oscuro, continuar)
            boton("Salir",0.625*display_ancho,0.6*display_altura,0.1875*display_ancho,65, rojo, rojo_oscuro, quit_juego)        

            #actualizar pantalla
            pygame.display.update()
            clock.tick(15)

    
    #pantalla de inicio
    
    def game_intro():
        
        nombreUser = ""
        userExiste = False
        
        intro = True
        while intro == True:
            for event in pygame.event.get():
                #agarra el input del usuario y  lo concatena
                if event.type == pygame.KEYDOWN:
                    if event.unicode.isalpha():
                        nombreUser += event.unicode
                if event.type == pygame.QUIT:
                        quit_juego()

            #gameDisplay.fill(blanco)

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

            
            textoFuente = pygame.font.Font("freesansbold.ttf", 50)
            textSuperficie, textRect = objetos_texto("Orion: The Game", textoFuente)
            textRect.center = ((display_ancho/2), (display_altura/2))
            gameDisplay.blit(textSuperficie, textRect)

            #print(nombreUser)
            
            #Logica para ingresar usuario:
            #Va a existir un boton que indique que "ingrese su usuario"
            #Cuando el usuario presione el boton izquierdo del mouse se crea un boton que se va a llenar con el nombre de usuario
            #Para que el usuario no tenga que dejar presionado el mouse, creamos una variable para ver si ya presiono
            #anteriormente el mouse
            boton("Ingresar jugador",0.4*display_ancho,0.55*display_altura,0.2*display_ancho,25,blanco,blanco, None)
            if userExiste == True:
                boton(nombreUser,0.4*display_ancho,0.6*display_altura,0.2*display_ancho,25,blanco,blanco, None)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    boton(nombreUser,0.4*display_ancho,0.6*display_altura,0.2*display_ancho,25,blanco,blanco, None)
                    userExiste = True
            
            boton("Iniciar",0.4*display_ancho,0.65*display_altura,0.2*display_ancho,50,verde,verde_oscuro, game_bucle)
            boton("Salir",0.4*display_ancho,0.75*display_altura,0.2*display_ancho,50, rojo, rojo_oscuro, quit_juego) 

            #actualizar pantalla
            pygame.display.update()
            clock.tick(15)

    #pantalla de juego inicial
    def game_bucle():

        global pausa
        musicaPausa = 0
        #coordenadas iniciales del carro
        x = (display_ancho * 0.45)
        y = (display_altura * 0.8)
        #indica por cuantas coordinadas se mueve en el eje X
        x_cambio = 0
        y_cambio = 0

        #pygame.key.set_repeat(10,10)
        tocarMusica("music/musica.mp3", -1)
        #coordinadas de obstaculos
        obs_startX= random.randrange(0,display_ancho)
        obs_startY= -500
        #modificar la velocidad de obstaculos para aumentar la dificultad
        obs_speed= 20
        obs_ancho= car_ancho
        obs_altura = car_altura

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
                    quit_juego()
                #print(event)
                #keydown = tecla presionada
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_cambio = -30
                        estado_mov = True
                    if event.key == pygame.K_RIGHT:
                        x_cambio = 30
                        estado_mov = True
                    if event.key == pygame.K_UP:
                        y_cambio = -30
                        estado_mov = True
                    if event.key == pygame.K_DOWN:
                        y_cambio = 30
                        estado_mov = True
                    if event.key == pygame.K_p:
                        if estado_mov == False:
                            pausa = True
                            pausado()
                    if event.key == pygame.K_m:
                        if estado_mov == False:
                            if musicaPausa == 0:
                                pausarMusica()
                                musicaPausa = 1
                            elif musicaPausa == 1:
                                resumirMusica()
                                musicaPausa = 0

                #keyup = se deja de presionar tecla
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_cambio = 0
                        estado_mov = False
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_cambio = 0
                        estado_mov = False
            x += x_cambio
            y += y_cambio
            #gameDisplay.fill(blanco)
            fondo = pygame.image.load("images/pista.jpg")
            fondo = pygame.transform.scale(fondo, (display_ancho, display_altura))
            gameDisplay.blit(fondo, (0,0))
            #actualizar las coordinadas del carro y del obstaculo
            obstaculo(obs_startX, obs_startY, obs_ancho, obs_altura, azul)
            #simula velocidad del obstaculo, se mueve en el eje Y
            obs_startY += obs_speed
            car(x,y)
            obs_esquivados(esquivado)

            #verifica si el carro se choca con los bordes
            if x > display_ancho - car_ancho or x < 0:
                pararMusica()
                tocarMusica("music/crash.mp3", 0)
                crash(esquivado)
            if y > display_altura - car_altura:
                y=display_altura - car_altura
            elif y < 0:
                y=0
            #simula obstaculos infinitos al regresarlo al comienzo si desaperece
            #de la pantalla, y se agrega un punto al puntaje
            if obs_startY > display_altura:
                obs_startY = 0 - obs_altura
                obs_startX = random.randrange(0 + obs_ancho, display_ancho-obs_ancho)
                esquivado = esquivado + 1
                obs_speed = obs_speed + 2
                
            #logica de crash:
            #Y de carro es menor que la altura del obstaculo MAS la coordenada
            #del obstaculo, en otras palabras, obstaculo esta dentro del carro
            if y < obs_startY + obs_altura and y + car_altura > obs_startY:
                #Eye X del carro debe rozar con una de las esquinas de X
                #o debe chocar con el borde de inferior del obstaculo
                #SI esquina izquierda del carro es mayor que la esquina izquierda del obstaculo
                #MAS la esquina izquierda del carro es menor que la esquina derecha del obstaculo
                #O la esquina derecha del carro es mayor que la esquina izquierda del obstaculo
                #MAS la esquina derecha del carro es menor que la esquina derecha del obstaculo
                if x + car_ancho > obs_startX and x < obs_startX + obs_ancho:
                #if x > obs_startX and x < obs_startX + obs_ancho or x+car_ancho > obs_startX and x+car_ancho < obs_startX+obs_ancho:
                    pararMusica()
                    tocarMusica("music/crash.mp3", 0)
                    crash(esquivado)
            #actualizar el display
            pygame.display.update()
            clock.tick(60)

    game_intro()
    game_bucle()
    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main()
