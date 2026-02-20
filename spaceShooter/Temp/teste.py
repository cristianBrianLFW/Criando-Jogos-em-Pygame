import pygame
 
# Versao com velocidade por frame

# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()
# running = True

# player_pos = pygame.Vector2(
#     screen.get_width() / 2,
#     screen.get_height() / 2
# )

# VELOCIDADE_POR_FRAME = 5  # pixels por frame

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill("purple")

#     pygame.draw.circle(screen, "red", player_pos, 40)

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w]:
#         player_pos.y -= VELOCIDADE_POR_FRAME
#     if keys[pygame.K_s]:
#         player_pos.y += VELOCIDADE_POR_FRAME
#     if keys[pygame.K_a]:
#         player_pos.x -= VELOCIDADE_POR_FRAME
#     if keys[pygame.K_d]:
#         player_pos.x += VELOCIDADE_POR_FRAME

#     pygame.display.flip()

#     clock.tick(60)  # tenta limitar o FPS, mas não garante tempo exato

# pygame.quit()


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()