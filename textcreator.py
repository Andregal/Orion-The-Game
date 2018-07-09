import pygame

#se crea el texto 
def objetos_texto(text, fuente):
    textSuper = fuente.render(text, True, (0,0,0))
    return textSuper, textSuper.get_rect()
