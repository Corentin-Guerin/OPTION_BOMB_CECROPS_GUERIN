import pygame


"""
# plein ecran
pygame.FULLSCREEN
# cree une fenetre redimentionnable 
pygame.RESIZABLE
#enleve les frames de la fenetre
pygame.NOFRAME


# rendue
pygame.OPENGL
# accélération materiel
pygame.HWSURFACE
# double memoire tampon pour les cinématiques surtous 
pygame.DOUBLEBUF
"""

pygame.init()

# Titre de la fenetre
pygame.display.set_caption("Bomberman")

# creation de la surface dans la fenetre python
# set_mode = cree une surface avec en parametre la resolution de fenetr
#peut -etre rapeller a tout moment pour changer les parametre 
taillescreen = (640,480)
screen_surface = pygame.display.set_mode(taillescreen, pygame.RESIZABLE)


#afficher des infos dans le terminal 
print(pygame.display.Info())

# ferme la fenetre avec la croix en haut a droite  
launched = True
while launched:

    # Creation ecran d'accueil
    accueil_image = pygame.image.load(accueil_image).convert()
    # superpose une image 
    screen_surface.blit(accueil_image, (0, 0))

    # rafraichie les données
    pygame.display.flip()

    #activation des menus
    fenetre_accueil = True
    fenetre_controle = True
    fenetre_jeu = True
    fenetre_victoirej1 = False
    fenetre_victoirej2 = False
    
    while fenetre_accueil:
        
        
        # limitation de vittesse a 30 image par sec
        pygame.time.Clock().tick(30)
        
        start = "accueil"

        for event in pygame.event.get():
            # Quitter
            if event.type == pygame.QUIT:
                fenetre_accueil = False
                fenetre_controle = False
                fenetre_jeu = False
                launched = False
            # Lancer le jeu
            elif event.key == K_SPACE:
                fenetre_controle = False
                fenetre_accueil = False
                start = "play"
            elif event.key == K_P:
                fenetre_accueil = False

    while fenetre_controle:
        
        if event.type == pygame.QUIT:
            fenetre_controle = False
            fenetre_jeu = False
            launched = False
        elif event.key == K_SPACE:
                fenetre_accueil = True
        controle_image = pygame.image.load(controle_image).convert()
        screen_surface.blit(controle_image, (0, 0))

    # Vérification du lancement du jeu pour ne pas charger les parametre si le joueur quitte
    #if start =="play":

        #entré ici les parametres de construction du niveau
        #Tiled est utilisable 
    
    while fenetre_jeu:
        if event.type == pygame.QUIT:
            fenetre_jeu = False
            launched = False

        #entré ici les parametres d'évenement du jeu 
        
        # conditions de victoire
        if game_over == 1:
            fenetre_jeu = False
            fenetre_victoirej2 = True
       
        if game_over == 2:
            fenetre_jeu = False
            fenetre_victoirej1 = True

    while fenetre_victoirej1:
        vicoitej1_image = pygame.image.load(vicoitej1_image).convert()
        screen_surface.blit(vicoitej1_image, (0, 0))
         
        if event.type == pygame.QUIT:
            fenetre_victoirej1 = False
            launched = False
        # reLancer le jeu
        elif event.key == K_SPACE:
            fenetre_accueil = True
            fenetre_controle = True
            fenetre_jeu = True
            fenetre_victoirej1 = False
            fenetre_victoirej2 = False
         
    while fenetre_victoirej2:
        vicoitej2_image = pygame.image.load(vicoitej2_image).convert()
        screen_surface.blit(vicoitej2_image, (0, 0))

        if event.type == pygame.QUIT:
            fenetre_victoirej2 = False
            launched = False
        # reLancer le jeu
        elif event.key == K_SPACE:
            fenetre_accueil = True
            fenetre_controle = True
            fenetre_jeu = True
            fenetre_victoirej1 = False
            fenetre_victoirej2 = False
         