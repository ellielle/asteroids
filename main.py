import pygame

from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # delta time used for calculating rotation and movement
    dt = 0

    # sprite groups to make updating all objects easier
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # instantiate player object
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, radius=PLAYER_RADIUS)

    while True:
        # Allows the close button to close the game and not hang
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("#000000")
        # loop over items in drawable container and call .draw()
        for d in drawable:
            d.draw(screen)
        # set the fps to 60
        # get the delta time from the last frame
        # by dividing the value returned from tick by 1000
        dt = clock.tick(60) / 1000

        # loop over items in updatable container and call .update()
        for u in updatable:
            u.update(dt)

        # update the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
