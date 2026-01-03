import pygame

# general setup

pygame.init()

pygame.display.set_caption("Space Shooter")

surf = pygame.Surface ((100, 200))

surf.fill ("black")

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

displaySurface = pygame.display.set_mode ((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    displaySurface.fill ("darkgray")
    displaySurface.blit (surf, (640,360))
    pygame.display.update ()

pygame.quit()

