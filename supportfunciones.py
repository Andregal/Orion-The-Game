import pygame
import textcreator
import singletonpausa


def continuar():
    #global pausa
    estadoPausa = singletonpausa.statePause.get_instance()
    estadoPausa.pausa = False
    
def quit_juego():
    pygame.quit()
    quit()

class colorPalette:
    negro = (0,0,0)
    blanco = (255,255,255)
    rojo = (255,0,0)
    verde = (0,255,0)
    azul = (0,0,255)

    rojo_oscuro=(200,0,0)
    verde_oscuro=(0,200,0)
    azul_oscuro=(0,0,200)

class paramBotones:
    def __init__(self, X, Y,ancho, altura, cAct, cIna):
        self.X = X
        self.Y = Y
        self.ancho = ancho
        self.altura = altura
        self.cAct = cAct
        self.cIna = cIna

class MusicManager:

    def tocarMusica(self,ubicacionSound, veces):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.load(ubicacionSound)
        pygame.mixer.music.play(veces)

    def pararMusica(self):
        pygame.mixer.music.stop()

    def pausarMusica(self):
        pygame.mixer.music.pause()

    def resumirMusica(self):
        pygame.mixer.music.unpause()

class Bus:

    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def cargarBus(self, ubic):
        carImg = pygame.image.load(ubic)
        carImg = pygame.transform.scale(carImg, (self.ancho, self.altura))
        return carImg

class Obstaculo:

    def __init__(self, x,y, ancho, altura, tipo):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.altura = altura
        self.tipo = tipo

    

#GESTORES DE SOPORTE

class displayManager:
    
    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay

    #funcion de boton
    #Se pasa el mensaje, valores X e Y, ancho, altura,
    #sus colores en estado activo e inactivo y tipo de accion del boton(debe ser funcion)
    def boton(self,mensaje, params, accion=None):
        #devuelve posicion del mouse en una tupla de 2 valores:
        #(valorX, valorY)
        mouse = pygame.mouse.get_pos()
        #devuelve clicks del mouse en una tupla en valores binarios de 3 valores:
        #(click izquierdo, click rueda, click derecho)
        click = pygame.mouse.get_pressed()
        
        #botones, cambian de color cuando el mouse los toca
        if (params.X+params.ancho) > mouse[0] and params.X < mouse[0] and (params.Y+params.altura) > mouse[1] and params.Y < mouse[1]:
            pygame.draw.rect(self.gameDisplay, params.cAct, (params.X,params.Y,params.ancho, params.altura))
            if click[0] == 1 and accion != None:
                accion()
        else:
            pygame.draw.rect(self.gameDisplay, params.cIna, (params.X,params.Y,params.ancho, params.altura))
        
        #texto para los botones
        textoBotones = pygame.font.Font("freesansbold.ttf", 20)
        textSup, textRect = textcreator.objetos_texto(mensaje, textoBotones)
        textRect.center = ((params.X+(params.ancho/2)), (params.Y+(params.altura/2)))
        self.gameDisplay.blit(textSup, textRect)

    def cargarobstaculo(self,obs, color):
        #draw.rect(ValorX, ValorY, Ancho, Altura)
        pygame.draw.rect(self.gameDisplay, color, [obs.x, obs.y, obs.ancho, obs.altura])

    #clase carro con su valores en eje X y Y
    def car(self,carImg,x,y):
        self.gameDisplay.blit(carImg,(x,y))        

    def obs_esquivados(self,count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Puntaje: " +str(count) + ", presione P para pausar el juego, presione M para pausar/continuar la música", True, (0,0,0))
        self.gameDisplay.blit(text, (0,0))    

    #clase para mostrar el mensaje
    def mostrar_mensaje(self,texto):
        textoFuente = pygame.font.Font("freesansbold.ttf", 115)    
        textSuperficie, textRect = objetos_texto(texto, textoFuente)
        textRect.center = ((display_ancho/2), (display_altura/2))
        self.gameDisplay.blit(textSuperficie, textRect)

        pygame.display.update()
        game_bucle()



