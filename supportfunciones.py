import pygame
import textcreator
import singletonpausa
import singletonsesion
import peticiones
import queryfactory
import tkinter as tk

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

    verde_claro = (139,195,74)
    verde_osc = (85, 139, 47)
    azul_claro = (33,150, 243)
    azul_osc = (21,101,192)
    rojo_claro= (244,67,54)
    rojo_osc= (198,40,40)

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
        carImg = pygame.transform.rotate(carImg, 270)
        carImg = pygame.transform.scale(carImg, (self.ancho, self.altura))
        return carImg

class Obstaculo:

    def __init__(self, x, y, ancho, altura, tipo, dificultad, velocidad):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.altura = altura
        self.tipo = tipo
        self.dificultad = dificultad
        self.velocidad = velocidad
        self.estadoTerminado = False

#GESTORES DE SOPORTE

class displayManager:
    
    sesion = singletonsesion.datosSesion.get_instance()
    
    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay

    def onSuperClick(self, params, click, mouse, bdquery, accion):
        if (params.X+params.ancho) > mouse[0] and params.X < mouse[0] and (params.Y+params.altura) > mouse[1] and params.Y < mouse[1]:
            pygame.draw.rect(self.gameDisplay, params.cAct, (params.X,params.Y,params.ancho, params.altura))
            if click[0] == 1 and accion != None:
                if bdquery == None:
                    accion()
                else:
                    qResult = queryfactory.queryFactory(bdquery[1], bdquery[2])
                    sesion.qResultado = qResult
                    if bdquery[1] == "validarUser" and bdquery[2] == False:
                        self.cargar_ventanaUser(qResult, accion)
        else:
            pygame.draw.rect(self.gameDisplay, params.cIna, (params.X,params.Y,params.ancho, params.altura))        

    def boton(self,mensaje, params, bdquery,accion=None):
        #devuelve posicion del mouse en una tupla de 2 valores:
        #(valorX, valorY)
        mouse = pygame.mouse.get_pos()
        #devuelve clicks del mouse en una tupla en valores binarios de 3 valores:
        #(click izquierdo, click rueda, click derecho)
        click = pygame.mouse.get_pressed()

        self.onSuperClick(params, click, mouse, bdquery, accion)
        
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

    def obs_esquivados(self,count, buff, stage):
        font = pygame.font.SysFont(None, 25)
        text = font.render("PUNTAJE: " +str(count), True, (0,0,0))
        self.gameDisplay.blit(text, (0,0))
        if buff == True:
            estado2 = "PROTEGIDO"
        else:
            estado2 = "NO PROTEGIDO"
        text1 = font.render("ESTADO DE ESCUDO: " +estado2, True, (0,0,0))
        self.gameDisplay.blit(text1, (0,30))
        text1 = font.render("DIFICULTAD: " +stage, True, (0,0,0))
        self.gameDisplay.blit(text1, (0,60))
        
    #clase para mostrar el mensaje
    def mostrar_mensaje(self,texto):
        textoFuente = pygame.font.Font("freesansbold.ttf", 115)    
        textSuperficie, textRect = objetos_texto(texto, textoFuente)
        textRect.center = ((display_ancho/2), (display_altura/2))
        self.gameDisplay.blit(textSuperficie, textRect)

        pygame.display.update()
        game_bucle()


    def cargar_ventanaUser(result, accion):
        window = Tk()
        window.title("Confirmar usuario")
        window.geometry("400x400")
        title = tk.Label(text ="Ingrese su contraseña")
        title.grid(column = 0, row = 0)

        b1 = tk.Button(text = "Aceptar")
        b1.grid(column = 0, row = 2)

        b2 = tk.Button(text = "Cancelar")
        b2.grid(column = 1, row = 2)

        input1 = tk.Entry()
        input1.grid(column = 0, row = 1)
        
        window.mainloop()

        
        
##        popup = tk.TK()
##
##        if result == True
##            body = "Ingrese su contraseña."
##            popup.wm_title("Confirmar usuario")
##            
##            b1 = ttk.Button(popup, "OK", command = popup.destroy)
##    

