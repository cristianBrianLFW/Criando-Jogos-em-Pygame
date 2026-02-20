import pygame

import random

from os.path import join

# general setup

pygame.init()

pygame.display.set_caption("Space Shooter")

# main surface

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

displaySurface = pygame.display.set_mode ((WINDOW_WIDTH, WINDOW_HEIGHT))


# clock of the game

clock = pygame.time.Clock()

# player_surf

player_surf = pygame.image.load(join ( "images", "player.png")).convert_alpha()

player_rect = player_surf.get_frect(center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

player_direction = pygame.math.Vector2(0, 0)

player_speed = 300


# star

star = pygame.image.load ( join ( "images", "star.png")).convert_alpha()

starPositons = [(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT)) for i in range ( 20 )]
 
running = True

# meteor

meteor_surf = pygame.image.load( join ("images", "meteor.png")).convert_alpha()

meteor_rect = meteor_surf.get_frect (center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 ))

# laser

laser_surf = pygame.image.load ( join ("images", "laser.png")).convert_alpha()

laser_rect = laser_surf.get_frect (bottomleft = (20, WINDOW_HEIGHT - 20))

i = 0

while running:

    dt = clock.tick(60)/ 1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     i += 1
        #     print ("fire laser ", i)


            

    keys = pygame.key.get_pressed()

    player_direction.x = int ( keys [ pygame.K_RIGHT] or keys [ pygame.K_d]) - int ( keys [ pygame.K_LEFT] or keys [pygame.K_a])
    player_direction.y = int ( keys [ pygame.K_DOWN] or keys [ pygame.K_s ] ) - int ( keys [ pygame.K_UP] or keys [ pygame.K_w])
    player_direction = player_direction.normalize( ) if player_direction else player_direction
    player_rect.center += player_direction * dt * player_speed

    oneTime = pygame.key.get_just_pressed()

    

    if oneTime [ pygame.K_SPACE]:
        print ( "fire laser ", i )
        i+=1


    displaySurface.fill ( "darkgrey" )
    for pos in starPositons:
        displaySurface.blit( star, pos)
    displaySurface.blit (meteor_surf, meteor_rect)
    displaySurface.blit ( laser_surf, laser_rect )
    displaySurface.blit(player_surf, player_rect.topleft)    



    pygame.display.update ()

pygame.quit()

