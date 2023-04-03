import pygame
from pygame.locals import *
from random import *
from time import sleep

def change_ecran() :
    global ecran
    global cibles
    global impacts
    global vie
    global score
    global mode2
    global temps
    if ecran == 1 :
        fenetre.blit(fond1,(0,0))
    elif ecran == 2 :
        fenetre.blit(fond2,(0,0))
        myfont = pygame.font.SysFont("Fixedsys",40)
        texte = myfont.render("Record : "+str(record[0]),False,(136,0,21))
        fenetre.blit(texte,(325,268))
        texte = myfont.render("Record : "+str(record[1]),False,(136,0,21))
        fenetre.blit(texte,(325,417))
    elif ecran == 3 :
        pygame.draw.rect(fenetre,(150,94,63),(0,0,800,600))
        fenetre.blit(fond3,(0,0))

        myfont = pygame.font.SysFont("Liberation Serif",40)

        texte = myfont.render(str(cibles[0]),False,(0,0,0))
        fenetre.blit(texte,(177-len(str(cibles[0]))*10,190))

        texte = myfont.render(str(cibles[1]),False,(0,0,0))
        fenetre.blit(texte,(397-len(str(cibles[1]))*10,190))

        texte = myfont.render(str(cibles[2]),False,(0,0,0))
        fenetre.blit(texte,(617-len(str(cibles[2]))*10,190))

        for i in range (0,len(impacts)-1,2) :
            pygame.draw.circle(fenetre,(0,0,0),(impacts[i]-2,impacts[i+1]-2),2,0)

        for i in range (vie) :
            fenetre.blit(coeur,(8+40*i,504))

        texte = myfont.render("Score : "+str(score),False,(255,255,255))
        fenetre.blit(texte,(8,539))

        texte = myfont.render(cibles[4],False,(255,255,255))
        fenetre.blit(texte,(400-int(len(cibles[4])/2+1.5)*10,525))

        pygame.draw.rect(fenetre,(255,201,14),(400-temps*20,10,temps*40,10))

    pygame.display.flip()

    if ecran == 3 :
        if vie == 0 :
            if mode == 1 and score > record[0] :
                record[0] = score
            elif mode == 2 and score > record[1] :
                record[1] = score
            ecran = 1
            change_ecran()

def change_cibles() :
    global cibles
    global mode
    global score
    global temps
    temps = 5

    cibles = ["","","","",""]

    if score < 5 :
        a = 10
    elif score < 20 :
        a = 100
    else :
        a = 1000

    if mode == 1 :
        nb_premiers = [2]
        nb_test = 3
        while nb_premiers[-1] < a :
            non = 0
            for i in range (len(nb_premiers)) :
                if nb_test%nb_premiers[i] == 0 :
                    non = 1
                    break
            if non == 0 :
                nb_premiers += [nb_test]
            nb_test += 1
        del nb_premiers[len(nb_premiers)-1:len(nb_premiers)]

        b = randint(0,2)
        cibles[b] = nb_premiers[randint(0,len(nb_premiers)-1)]
        cibles[3] = b

        if not b == 0 :
            cibles[0] = randint(1,a-1)
            non = 1
            while non == 1 :
                non = 0
                for i in range (len(nb_premiers)) :
                    if nb_premiers[i] == cibles[0] :
                        non = 1
                        break
                if non == 1 :
                    cibles[0] = randint(1,a-1)

        if not b == 1 :
            cibles[1] = randint(1,a-1)
            non = 1
            while non == 1 :
                non = 0
                for i in range (len(nb_premiers)) :
                    if nb_premiers[i] == cibles[1] or cibles[0] == cibles[1] :
                        non = 1
                        break
                if non == 1 :
                    cibles[1] = randint(1,a-1)

        if not b == 2 :
            cibles[2] = randint(1,a-1)
            non = 1
            while non == 1 :
                non = 0
                for i in range (len(nb_premiers)) :
                    if nb_premiers[i] == cibles[2] or cibles[0] == cibles[2] or cibles[1] == cibles[2] :
                        non = 1
                        break
                if non == 1 :
                    cibles[2] = randint(1,a-1)

    else :
        operation = randint(1,3)
        nb1 = randint(1,a-1)
        nb2 = randint(1,a-1)
        b = randint(0,2)
        if operation == 1 :
            cibles[b] = nb1+nb2
            cibles[4] = str(nb1) + " + " + str(nb2) + " = ?"
        elif operation == 2 :
            cibles[b] = nb1-nb2
            cibles[4] = str(nb1) + " - " + str(nb2) + " = ?"
        elif operation == 3 :
            cibles[b] = nb1*nb2
            cibles[4] = str(nb1) + " * " + str(nb2) + " = ?"

        nb1 = randint(cibles[b]-(len(str(a))+1),cibles[b]+(len(str(a))+1))
        while nb1 == cibles[b] :
            nb1 = randint(cibles[b]-(len(str(a))+1),cibles[b]+(len(str(a))+1))
        nb2 = randint(cibles[b]-(len(str(a))+1),cibles[b]+(len(str(a))+1))
        while nb2 == cibles[b] or nb2 == nb1 :
            nb2 = randint(cibles[b]-(len(str(a))+1),cibles[b]+(len(str(a))+1))

        if b == 0 :
            cibles[1] = nb1
            cibles[2] = nb2
        elif b == 1 :
            cibles[0] = nb1
            cibles[2] = nb2
        else :
            cibles[0] = nb1
            cibles[1] = nb2

        cibles[3] = b

    anim_cibles1()

def anim_cibles1() :
    global cibles
    myfont = pygame.font.SysFont("Liberation Serif",40)
    for i in range (67) :
        pygame.draw.rect(fenetre,(185,122,87),(0,0,800,600))

        pygame.draw.rect(fenetre,(150,94,63),(143,246-i,211,246))
        texte = myfont.render(str(cibles[0]),False,(0,0,0))
        fenetre.blit(texte,(177-len(str(cibles[0]))*10,256-i))

        pygame.draw.rect(fenetre,(150,94,63),(363,246-i,430,246))
        texte = myfont.render(str(cibles[1]),False,(0,0,0))
        fenetre.blit(texte,(397-len(str(cibles[1]))*10,256-i))

        pygame.draw.rect(fenetre,(150,94,63),(583,246-i,650,246))
        texte = myfont.render(str(cibles[2]),False,(0,0,0))
        fenetre.blit(texte,(617-len(str(cibles[2]))*10,256-i))

        fenetre.blit(fond3,(0,0))

        for i in range (0,len(impacts)-1,2) :
            pygame.draw.circle(fenetre,(0,0,0),(impacts[i]-2,impacts[i+1]-2),2,0)

        for i in range (vie) :
            fenetre.blit(coeur,(8+40*i,504))

        texte = myfont.render("Score : "+str(score),False,(255,255,255))
        fenetre.blit(texte,(8,539))

        texte = myfont.render(cibles[4],False,(255,255,255))
        fenetre.blit(texte,(400-int(len(cibles[4])/2+1.5)*10,525))

        pygame.display.flip()

def anim_cibles2() :
    global cibles
    global impacts
    remove_imp = []
    for i in range (0,len(impacts)-1,2) :
        if impacts[i] > 142 and impacts[i] < 211 and impacts[i+1] > 177 and impacts[i+1] < 246 or impacts[i] > 362 and impacts[i] < 431 and impacts[i+1] > 177 and impacts[i+1] < 246 or impacts[i] > 582 and impacts[i] < 651 and impacts[i+1] > 177 and impacts[i+1] < 246 :
            remove_imp += [i]

    myfont = pygame.font.SysFont("Liberation Serif",40)
    for i in range (67) :
        pygame.draw.rect(fenetre,(185,122,87),(0,0,800,600))

        pygame.draw.rect(fenetre,(150,94,63),(143,180+i,211,181))
        texte = myfont.render(str(cibles[0]),False,(0,0,0))
        fenetre.blit(texte,(177-len(str(cibles[0]))*10,190+i))

        pygame.draw.rect(fenetre,(150,94,63),(363,180+i,430,181))
        texte = myfont.render(str(cibles[1]),False,(0,0,0))
        fenetre.blit(texte,(397-len(str(cibles[1]))*10,190+i))

        pygame.draw.rect(fenetre,(150,94,63),(583,180+i,650,181))
        texte = myfont.render(str(cibles[2]),False,(0,0,0))
        fenetre.blit(texte,(617-len(str(cibles[2]))*10,190+i))

        fenetre.blit(fond3,(0,0))

        for i in range (len(remove_imp)-1,-1,-1) :
            impacts[remove_imp[i]+1] += 1
            if impacts[remove_imp[i]+1] > 243 :
                del impacts[remove_imp[i]:remove_imp[i]+2]
                del remove_imp[i:i+1]
                for i in range (i,len(remove_imp),1) :
                    remove_imp[i] -= 2

        for i in range (0,len(impacts)-1,2) :
            pygame.draw.circle(fenetre,(0,0,0),(impacts[i]-2,impacts[i+1]-2),2,0)

        for i in range (vie) :
            fenetre.blit(coeur,(8+40*i,504))

        texte = myfont.render("Score : "+str(score),False,(255,255,255))
        fenetre.blit(texte,(8,539))

        texte = myfont.render(cibles[4],False,(255,255,255))
        fenetre.blit(texte,(400-int(len(cibles[4])/2+1.5)*10,525))

        pygame.display.flip()

    change_cibles()

pygame.init()

raccourci = __file__
raccourci = raccourci[0:-8]

fenetre = pygame.display.set_mode((800,600))
pygame.display.set_caption("Mathematics Shooter")

icone = pygame.image.load(raccourci+"sprite\\icone.png")
pygame.display.set_icon(icone)

fond1 = pygame.image.load(raccourci+"sprite\\fond1.png").convert()
fond2 = pygame.image.load(raccourci+"sprite\\fond2.png").convert()
fond3 = pygame.image.load(raccourci+"sprite\\fond3.png").convert()
fond3.set_colorkey((255,255,255))
coeur = pygame.image.load(raccourci+"sprite\\coeur.png").convert()
coeur.set_colorkey((255,255,255))

ecran = 1
record = [0,0]

change_ecran()

b = 1
while b == 1 :
    for event in pygame.event.get() :
        if event.type == QUIT :
            b = 0
            pygame.quit()

        elif event.type == MOUSEBUTTONDOWN :
            if ecran == 1 :
                if event.pos[0] > 283 and event.pos[0] < 514 and event.pos[1] > 354 and event.pos[1] < 441 :
                    ecran = 2
            elif ecran == 2 :
                if event.pos[0] > 7 and event.pos[0] < 791 and event.pos[1] > 299 and event.pos[1] < 385 :
                    ecran = 3
                    mode = 1
                    score = 0
                    impacts = []
                    vie = 3
                    change_cibles()
                elif event.pos[0] > 7 and event.pos[0] < 791 and event.pos[1] > 449 and event.pos[1] < 535 :
                    ecran = 3
                    mode = 2
                    score = 0
                    impacts = []
                    vie = 3
                    change_cibles()
            elif ecran == 3 and event.pos[1] > 95 and event.pos[1] < 403 :
                impacts += [event.pos[0],event.pos[1]]
                if event.pos[0] > 142 and event.pos[0] < 211 and event.pos[1] > 177 and event.pos[1] < 246 :
                    if cibles[3] == 0 :
                        score += 1
                    else :
                        vie -= 1
                    if vie > 0 :
                        anim_cibles2()
                elif event.pos[0] > 362 and event.pos[0] < 431 and event.pos[1] > 177 and event.pos[1] < 246 :
                    if cibles[3] == 1 :
                        score += 1
                    else :
                        vie -= 1
                    if vie > 0 :
                        anim_cibles2()
                elif event.pos[0] > 582 and event.pos[0] < 651 and event.pos[1] > 177 and event.pos[1] < 246 :
                    if cibles[3] == 2 :
                        score += 1
                    else :
                        vie -= 1
                    if vie > 0 :
                        anim_cibles2()

            change_ecran()

    if ecran == 3 :
        temps -= 0.03
        if temps < 0 :
            vie -= 1
            if vie > 0 :
                anim_cibles2()
        change_ecran()
        sleep(0.01)