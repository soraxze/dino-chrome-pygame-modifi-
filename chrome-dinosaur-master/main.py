import pygame
import os
import random

pygame.init()

# Constantes globales
HAUTEUR_ECRAN = 600
LARGEUR_ECRAN = 1100
ECRAN = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
pygame.display.set_caption('Dino Game')

# Charger les images pour les différentes actions du dinosaure
COURIR = [pygame.transform.scale(pygame.image.load(os.path.join("Assets", "perso", "run-1.png")), (84, 109)).convert_alpha(),
          pygame.transform.scale(pygame.image.load(os.path.join("Assets", "perso", "run-4.png")), (84, 109)).convert_alpha()]
SAUTER = pygame.image.load(os.path.join("Assets", "Dino", "DinoJump.png"))
S_ACCROUPIR = [pygame.image.load(os.path.join("Assets", "Dino", "DinoDuck1.png")),
               pygame.image.load(os.path.join("Assets", "Dino", "DinoDuck2.png"))]

# Charger les images pour les cactus et les oiseaux
PETIT_CACTUS = [pygame.image.load(os.path.join("Assets", "Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets", "Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets", "Cactus", "SmallCactus3.png"))]
GRAND_CACTUS = [pygame.image.load(os.path.join("Assets", "Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets", "Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets", "Cactus", "LargeCactus3.png"))]

OISEAU = [pygame.image.load(os.path.join("Assets", "Bird", "Bird1.png")),
          pygame.image.load(os.path.join("Assets", "Bird", "Bird2.png"))]

# Charger l'image du nuage et de l'arrière-plan
NUAGE = pygame.image.load(os.path.join("Assets", "Other", "Cloud.png"))
AR_PLAN = pygame.image.load(os.path.join("Assets", "Other", "Track.png"))

# Position et état initial du dinosaure
POS_X = 80
POS_Y = 310
POS_Y_ACCROUPI = 340
VIT_SAUT = 8.5

# Variables globales pour le jeu
vitesse_jeu = 20
pos_x_ar_plan = 0
pos_y_ar_plan = 380
points = 0
obstacles = []
compte_mort = 0

# Initialiser les nuages
nuages = [{'x': LARGEUR_ECRAN + random.randint(800, 1000), 'y': random.randint(50, 100), 'image': NUAGE}]

def init_dinosaure():
    return {
        'accroupir_img': S_ACCROUPIR,
        'courir_img': COURIR,
        'sauter_img': SAUTER,
        'dino_accroupir': False,
        'dino_courir': True,
        'dino_sauter': False,
        'index_etape': 0,
        'vit_saut': VIT_SAUT,
        'image': COURIR[0],
        'rect': COURIR[0].get_rect(topleft=(POS_X, POS_Y))
    }

def mettre_a_jour_dinosaure(dino, entree_utilisateur):
    if dino['dino_accroupir']:
        dino = accroupir(dino)
    if dino['dino_courir']:
        dino = courir(dino)
    if dino['dino_sauter']:
        dino = sauter(dino)

    if dino['index_etape'] >= 10:
        dino['index_etape'] = 0

    if entree_utilisateur[pygame.K_UP] and not dino['dino_sauter']:
        dino['dino_accroupir'] = False
        dino['dino_courir'] = False
        dino['dino_sauter'] = True
    elif entree_utilisateur[pygame.K_DOWN] and not dino['dino_sauter']:
        dino['dino_accroupir'] = True
        dino['dino_courir'] = False
        dino['dino_sauter'] = False
    elif not (dino['dino_sauter'] or entree_utilisateur[pygame.K_DOWN]):
        dino['
