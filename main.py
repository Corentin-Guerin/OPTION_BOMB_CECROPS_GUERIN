import pygame
from pygame.locals import *
from datetime import datetime, timedelta


from classes import *

# initialisation de pygame
pygame.display.init()

# initialisation de la fenetre  nombre de sprite par cote * taille du sprite


fenetre = pygame.display.set_mode((taillefenetre, taillefenetre))
pygame.display.set_caption("Bomberman")

# afficher des infos dans le terminal 
print(pygame.display.Info())

# variable de debut/fin de la boucle infinie
launched = 1

# boucle d'actualisation de la fenetre
while launched:

    # chargement de l'accueil
    accueil = pygame.image.load('images/image_accueil.png').convert()
    fenetre.blit(accueil, (0, 0))

    # rafraichissement
    pygame.display.flip()

    launched_jeu = 1
    launched_accueil = 1

    # boucle d'accueil
    while launched_accueil:

        # limitation de vittesse de la boucle
        pygame.time.Clock().tick(30)
        start = 0

        # evemements clavier du menu
        for event in pygame.event.get():
            # quitter le jeu
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                launched_accueil = 0
                launched_jeu = 0
                launched = 0
            # lancer la jeu
            elif event.type == KEYDOWN and event.key == K_SPACE:
                launched_accueil = 0
                start = "start"

    # Vérification du choix du niveau
    if start != 0:
    

        # generation du niveau à partir du fichier
        niveau = Niveau("level.txt")
        niveau.generer()
        niveau.afficher(fenetre)

        # création des deux avatars
        perso = Perso("images/player1d.png", "images/player1g.png", "images/player1h.png", "images/player1b.png", niveau)
        perso2 = Perso2("images/player2d.png", "images/player2g.png", "images/player2h.png", "images/player2b.png", niveau)
        # création des deux bombes
        bombe = Bomb("images/bombe.png", niveau, perso, perso2)
        bombe2 = Bomb("images/bombe.png", niveau, perso, perso2)
        # création des flammes
        flamme = Flammes("images/explod.png", "images/explog.png", "images/exploh.png", "images/explob.png")

    # boucle jeu
    while launched_jeu:

        # limitation de la vitesse
        pygame.time.Clock().tick(30)
        

        # boucle evenement 
        for event in pygame.event.get():

            # quitter le jeu
            if event.type == QUIT:
                launched_jeu = 0
                launched = 0
            elif event.type == KEYDOWN:
                # menu
                if event.key == K_ESCAPE:
                    launched_jeu = 0
                # pose de la bombe
                if event.key == K_SPACE:
                    bombe.poser(perso.x, perso.y, "images/bombe.png")

                # déplacement perso1
                elif event.key == K_RIGHT:
                    perso.deplacer("droite")
                elif event.key == K_LEFT:
                    perso.deplacer("gauche")
                elif event.key == K_DOWN:
                    perso.deplacer("bas")
                elif event.key == K_UP:
                    perso.deplacer("haut")

                # déplacement perso2

                if event.key == K_e:
                    bombe2.poser(perso2.x, perso2.y, "images/bombe.png")
                elif event.key == K_d:
                    perso2.deplacer("droite")
                elif event.key == K_q:
                    perso2.deplacer("gauche")
                elif event.key == K_s:
                    perso2.deplacer("bas")
                elif event.key == K_z:
                    perso2.deplacer("haut")

        # Affichages des nouvelles positions

        niveau.afficher(fenetre)
        fenetre.blit(perso.direction, (perso.x, perso.y))
        fenetre.blit(perso2.direction, (perso2.x, perso2.y))
        fenetre.blit(bombe.bomb, (bombe.x, bombe.y))
        fenetre.blit(bombe2.bomb, (bombe2.x, bombe2.y))

        # affichage explosion
        if bombe.explosion == 1:
            fenetre.blit(flamme.fflamme_b, (bombe.x, bombe.y + taille_sprite))
            fenetre.blit(flamme.fflamme_h, (bombe.x, bombe.y - taille_sprite))
            fenetre.blit(flamme.fflamme_g, (bombe.x - taille_sprite, bombe.y))
            fenetre.blit(flamme.fflamme_d, (bombe.x + taille_sprite, bombe.y))

        if bombe2.explosion == 1:
            fenetre.blit(flamme.fflamme_b, (bombe2.x, bombe2.y + taille_sprite))
            fenetre.blit(flamme.fflamme_h, (bombe2.x, bombe2.y - taille_sprite))
            fenetre.blit(flamme.fflamme_g, (bombe2.x - taille_sprite, bombe2.y))
            fenetre.blit(flamme.fflamme_d, (bombe2.x + taille_sprite, bombe2.y))

        # affichage de la frame
        pygame.display.flip()

        # verification des conditions de victoire
        game_over = bombe.exploser()
        if game_over == 1:
            launched_jeu = 0
            print("Joueur 2 win")

        game_over = bombe2.exploser()
        if game_over == 1:
            launched_jeu = 0
            print("Joueur 1 win")

      
