import sys, pygame, random, time
from pygame.locals import *    

display_ancho = 800
display_alto = 600

def crearTexto(screen, pos, text, size=24, color=(0,0,0), bold=False):
    textFont = pygame.font.SysFont(None, size, bold=bold)
    textSurface = textFont.render(text, True, color)
    screen.blit(textSurface, pos)

def crearBoton(screen,text,posx,posy,width,height,background):        
    pygame.draw.rect(screen, background, (posx,posy,width,height))
    crearTexto(screen,((posx+(width/3)),(posy+(height/3))),text)

def crearNombre(screen):
    incompleto = True
    nombre = ""

    while incompleto:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.unicode.isalpha():
                    nombre += event.unicode
                elif event.key == K_RETURN:
                    incompleto = False
                    
    crearBoton(screen,nombre,300,380,200,50,(102, 102, 102))

def main():

    pygame.init()
    pygame.display.set_caption("Orion: The Game")
    screen = pygame.display.set_mode((800,600))

    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.load("musica.mp3")
    pygame.mixer.music.play(-1)

    fondo = pygame.image.load("images/fondo.jpg")
    screen.blit(fondo, (0,0))
    orion = pygame.image.load("images/orion.jpg")
    screen.blit(orion, (250,100))
    config = pygame.image.load("images/config.png")
    screen.blit(config, (20,520))

    crearTexto(screen,(200,20),"Orion: The Game",60,bold=True)
    crearBoton(screen,"Empezar",300,500,200,50,(102, 102, 102))
    crearTexto(screen,(360,350),"Username")
    crearBoton(screen,"Click aqui",300,380,200,50,(102, 102, 102))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    crearNombre(screen)
                
        
        pygame.display.update()

#####################################################

if __name__ == "__main__":
    main()