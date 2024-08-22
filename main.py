import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # delta time
    dt = 0

    while True:
        # Allows the close button to close the game and not hang
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("#000000")
        pygame.display.flip()
        # set the fps to 60
        # get the delta time from the last frame
        # by dividing the value returned from tick by 1000
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
