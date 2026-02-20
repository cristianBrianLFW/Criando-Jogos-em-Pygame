import pygame

import random

from os.path import join


# informacoes gerais


pygame.init()

pygame.display.set_caption("Space Shooter")

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

displaySurface = pygame.display.set_mode ((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True

clock = pygame.Clock()

# classe Player

class Player ( pygame.sprite.Sprite ):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(join ( "images", "player.png")).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.direction = pygame.math.Vector2()
        self.speed = 300

        # custom cooldown laser

        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown = 400
    def laser_timer (self):

        if self.can_shoot == False:

            current_time = pygame.time.get_ticks()

            if current_time - self.laser_shoot_time >= self.cooldown:
                self.can_shoot = True


    def update ( self, dt ):

        keys = pygame.key.get_pressed()

        self.direction.x = int ( keys [ pygame.K_d] or keys [ pygame.K_RIGHT] ) - int ( keys [ pygame.K_a] or keys [ pygame.K_LEFT])

        self.direction.y = int ( keys [ pygame.K_s] or keys [ pygame.K_DOWN]) - int ( keys [ pygame.K_w] or keys [ pygame.K_UP])

        self.direction = self.direction.normalize() if self.direction else self.direction

        self.rect.center += self.direction * dt * self.speed

        recent_keys = pygame.key.get_just_pressed ()

        if recent_keys [ pygame.K_SPACE] and self.can_shoot == True:
            self.laser_shoot_time = pygame.time.get_ticks()
            self.can_shoot = False
            laser(laser_surf, self.rect.midtop, all_Sprites)

        self.laser_timer()

# classe star

class Star ( pygame.sprite.Sprite):
    def __init__(self, surf, *groups,):
        super().__init__(*groups )
        self.image = surf
        self.x = random.randint(0, WINDOW_WIDTH)
        self.y = random.randint ( 0, WINDOW_HEIGHT)
        self.rect = self.image.get_frect(center = ( self.x, self.y))

# classe laser

class laser ( pygame.sprite.Sprite):

    def __init__(self, surf, pos, groups):
        super().__init__( groups )
        self.image = surf
        self.rect = self.image.get_frect( midbottom = pos )
        self.speed = 400
    def update(self, dt):

        self.rect.centery -= self.speed * dt

        if self.rect.bottom < 0:
            self.kill()



# set dos Sprites

all_Sprites = pygame.sprite.Group()

    # carrangando imagem das estrelas
star_surf = pygame.image.load ( join ("images", "star.png")).convert_alpha()

    # set_stars
stars = [Star ( star_surf, all_Sprites ) for x in range ( 20 ) ]

    # set_player
player = Player (all_Sprites)

    # carregando imagem meteoro
laser_surf = pygame.image.load ( join ("images", "laser.png")).convert_alpha()





while running:

    dt = clock.tick(60) /1000

    # event loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update

    all_Sprites.update(dt)

    # draw
    
    displaySurface.fill ( "darkgrey" )

    all_Sprites.draw(displaySurface)

    pygame.display.update()

pygame.quit()

