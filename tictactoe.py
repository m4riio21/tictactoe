import pygame
import time
import random
import numpy as np

pygame.init()
pygame.font.init()
POSICIONES = [(22,22), (172,22), (322,22), (22,172), (172,172), (322,172), (22,322), (172,322), (322,322)]
WIDTH, HEIGHT = 462,460
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
IMAGEN_CRUZ = pygame.image.load('cruz.png')
IMAGEN_CIRCULO = pygame.image.load('circulo.png')
CRUZ = pygame.transform.scale(IMAGEN_CRUZ,(120,120))
CIRCULO = pygame.transform.scale(IMAGEN_CIRCULO,(120,120))
START_TEXT = pygame.font.SysFont('comicsans', 100)
ENTER_TEXT = pygame.font.SysFont('comicsans', 50)
TURN_TEXT = pygame.font.SysFont('comicsans', 20)
pygame.display.set_caption("Tres en raya")


def initScreen():
    WINDOW.fill((255, 255, 255))
    start = START_TEXT.render("Comenzar", 0, (0, 0, 0))
    enter = ENTER_TEXT.render("Pulsa FLECHA ARRIBA", 0, (0, 0, 0))
    WINDOW.blit(start, (60, 200))
    WINDOW.blit(enter, (40, 320))
    pygame.display.update()

def drawNextOne(posiciones,index,turno,ocupadas,tablero):
    x = posiciones[index].x
    y = posiciones[index].y
    ocupadas[index] = 1
    switcher = {
        0: (0,0),
        1: (0,1),
        2: (0,2),
        3: (1,0),
        4: (1,1),
        5: (1,2),
        6: (2,0),
        7: (2,1),
        8: (2,2),
    }
    tablero[switcher[index]] = turno
    compruebaWin(tablero,turno)
    if turno == 1:
        WINDOW.blit(CIRCULO,(x+12,y+12))
    else:
        WINDOW.blit(CRUZ, (x + 12, y + 12))


def compruebaWin(tablero,num):
    for fila in tablero:
        for pos in fila:
            if pos == num:
                continue
            else:
                break
        else:
            return True

    for columna in range(3):
        for fila in tablero:
            if fila[columna] == num:
                continue
            else:
                break
        else:
            return True

    for pos in range(3):
        if tablero[pos][pos] == num:
            continue
        else:
            break
    else:
        return True

    for pos in range(3):
        if tablero[pos][2-pos] == num:
            continue
        else:
            break
    else:
        return True

def startM():
    WINDOW.fill((0,0,0))
    TOPLEFT = pygame.draw.rect(WINDOW, (255, 255, 255), (10, 10, 142, 142))
    TOPMID = pygame.draw.rect(WINDOW, (255, 255, 255), (162, 10, 142, 142))
    TOPRIGHT = pygame.draw.rect(WINDOW, (255, 255, 255), (312, 10, 142, 142))
    MIDLEFT = pygame.draw.rect(WINDOW, (255, 255, 255), (10, 162, 142, 142))
    MIDMID = pygame.draw.rect(WINDOW, (255, 255, 255), (162, 162, 142, 142))
    MIDRIGHT = pygame.draw.rect(WINDOW, (255, 255, 255), (312, 162, 142, 142))
    BOTLEFT = pygame.draw.rect(WINDOW, (255, 255, 255), (10, 312, 142, 142))
    BOTMID = pygame.draw.rect(WINDOW, (255, 255, 255), (162, 312, 142, 142))
    BOTRIGHT = pygame.draw.rect(WINDOW, (255, 255, 255), (312, 312, 142, 142))
    list = [TOPLEFT,TOPMID,TOPRIGHT,MIDLEFT,MIDMID,MIDRIGHT,BOTLEFT,BOTMID,BOTRIGHT]
    return True, list

def draw_window():
    pygame.display.update()

def winner(num):
    WINDOW.fill((0, 0, 0))
    if num == 1:
        win = ENTER_TEXT.render("CIRCULO GANA", 0, (255,255,255))
        WINDOW.blit(win, (92, 200))
    if num == 0:
        win = ENTER_TEXT.render("CRUZ GANA", 0, (255,255,255))
        WINDOW.blit(win, (120, 200))


    pygame.display.update()

def checkPosicion(posiciones,turno,ocupadas,tablero):
    pos = pygame.mouse.get_pos()
    for index, posicion in enumerate(posiciones):
        if posicion.collidepoint(pos):
            if ocupadas[index] == 0:
                drawNextOne(posiciones,index,turno,ocupadas,tablero)

    if turno == 1:
        turno = 0
    else:
        turno = 1
    return turno

def tableroFull(tablero):
    if 9 not in tablero:
        return True


def main():
    tablero = 9 * np.ones((3,3))
    initScreen()
    run = True
    started = False
    posiciones = []
    ocupadas = [0,0,0,0,0,0,0,0,0]
    turno = random.randint(0,1)
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if not started:
                if event.type == pygame.KEYUP:
                    started, posiciones = startM()
            if started:
                if event.type == pygame.MOUSEBUTTONUP:
                    turno = checkPosicion(posiciones,turno,ocupadas,tablero)
                    if compruebaWin(tablero,0) == True:
                        winner(0)
                    if compruebaWin(tablero,1) == True:
                        winner(1)
                    if tableroFull(tablero) == True:
                        pygame.quit()


            pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()