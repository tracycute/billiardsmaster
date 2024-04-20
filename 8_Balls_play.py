import pygame
import config
pygame.init()


def draw_background():
    global config
    config.gameDisplay.fill(config.BROWN)
    pygame.draw.rect(config.gameDisplay, config.FELT, (200, 150, 1000, 500))
    for wall in config.walls: 
        pygame.draw.rect(config.gameDisplay, config.BRONZE, wall)
    for hole in config.holes: 
        pygame.draw.circle(config.gameDisplay, config.BLACK, hole, 22)
    
    # Draw players info
    p1_color = config.player_1.color
    p2_color = config.player_2.color
    config.gameDisplay.blit(config.mainFont.render('PLAYER 1', 1, config.P1), (20, 10))
    config.gameDisplay.blit(config.mainFont.render(p1_color.upper(), 1, config.P1), (20, 50))
    config.gameDisplay.blit(config.mainFont.render('PLAYER 2', 1, config.P2), (1260, 10))
    config.gameDisplay.blit(config.mainFont.render(p2_color.upper(), 1, config.P2), (1260, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    draw_background()
    pygame.display.update()
    pygame.time.Clock().tick(60)