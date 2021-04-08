import pygame

pygame.init()

#creation de la surface dans la fenetre python
#set_mode = cree une surface avec en parametre la resolution de fenetre 
taillescreen = (640,480)
screen = pygame.display.set_mode(taillescreen)

#ferme la fenetre avec la croix en haut a droite  
launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False