import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen) -> None:
        # sub-classes must override
        pass

    # the update method takes the deltatime from the fps clock
    def update(self, dt) -> None:
        # sub-classes must override
        pass

    # the collide method checks the distance between the
    # radius of 2 CircleShapes
    # if the distance is less than the 2 radii added, they collide
    def collide(self, cs) -> bool:
        distance = self.position.distance_to(cs.position)
        # Collision, return True
        if distance < self.radius + cs.radius:
            return True
        return False
