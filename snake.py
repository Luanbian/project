import pygame, sys
from pygame.locals import *
from random import randint
PRETO = (0,0,0)
AZUL = (0,0,255)
COMPRIMENTOJANELA=440
ALTURAJANELA=510
CIMA = 8
BAIXO = 2
ESQUERDA=4
DIREITA=6
bloco=[18,18]
snake = [[30,120],[10,120]]
cabeca = [30,120] 
x=randint(0,20)
y=randint(0,19)
comida = 0
while True:
    x1=randint(0,20)
    y1=randint(0,17)
    comidaXY=[int(x1*20)+10,int(y1*20)+120]
    if snake.count(comidaXY)==0:
        comida=1
        break
direccao = DIREITA
morto = 0
pontos=0
fundoJanela=pygame.display.set_mode((COMPRIMENTOJANELA,ALTURAJANELA),0,32)
pygame.display.set_caption('Snake')
pygame.init()
mainClock=pygame.time.Clock()
while not morto:  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if ((event.key == K_LEFT or event.key == ord('o'))  
               and direccao!=DIREITA):
                    direccao=ESQUERDA
            elif ((event.key == K_RIGHT or event.key == ord('p'))  
                 and direccao!=ESQUERDA):
                    direccao=DIREITA
            elif ((event.key == K_UP or event.key == ord('q')) 
                 and direccao!=BAIXO):
                    direccao=CIMA
            elif ((event.key == K_DOWN or event.key == ord('a')) 
                 and direccao!=CIMA):
                    direccao=BAIXO
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    if direccao==DIREITA:
        cabeca[0]+=20
        if cabeca[0] > COMPRIMENTOJANELA-20:
            morto=1
    elif direccao==ESQUERDA:
        cabeca[0]-=20
        if cabeca[0] < 10:
            morto=1
    elif direccao==CIMA:
        cabeca[1]-=20
        if cabeca[1] < 110:
            morto=1
    elif direccao==BAIXO:
        cabeca[1]+=20
        if cabeca[1] > ALTURAJANELA-30:
            morto=1
    if snake.count(cabeca)>0:
         morto=1
    if comida==0:
        while True:
            x1=randint(0,20)
            y1=randint(0,17)
            comidaXY=[int(x1*20)+10,int(y1*20)+120]
            if snake.count(comidaXY)==0:
                comida=1
                break
    snake.insert(0,list(cabeca))
    if cabeca[0]==comidaXY[0] and cabeca[1]==comidaXY[1]:
        comida=0
        pontos+=5
    else:
        snake.pop()
    fundoJanela.fill(PRETO)
    pygame.draw.rect(fundoJanela,AZUL,Rect([10,10],[420,100]),1)
    font = pygame.font.Font(None, 36)
    text = font.render("Pontos: " + str(pontos), 1, (200, 200, 200))
    textpos = text.get_rect()
    textpos.left = 75
    textpos.top = 45
    fundoJanela.blit(text, textpos)
    pygame.draw.rect(fundoJanela,AZUL,Rect([10,120],[420,380]),1)
    for x in snake:
        pygame.draw.rect(fundoJanela,AZUL, Rect(x,bloco))
    pygame.draw.rect(fundoJanela,(100,100,100),Rect(comidaXY,bloco))
    pygame.display.update()
    mainClock.tick(9)
