import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Allows the close button to close the game and not hang
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("#000000")
        pygame.display.flip()

if __name__ == "__main__":
    main()
