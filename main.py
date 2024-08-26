import pygame

from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # delta time
    dt = 0

    # instantiate player object
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, radius=PLAYER_RADIUS)

    while True:
        # Allows the close button to close the game and not hang
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("#000000")
        player.draw(screen)
        # set the fps to 60
        # get the delta time from the last frame
        # by dividing the value returned from tick by 1000
        dt = clock.tick(60) / 1000

        # update player's rotation/position etc
        player.update(dt)

        # update the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
