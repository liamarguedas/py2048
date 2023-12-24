import pygame, sys


class GameClass:
    def __init__(self, window_name) -> None:
        pygame.init()
        pygame.display.set_caption(window_name)

        # Window settings
        self.WIDTH = 600
        self.HEIGHT = 600
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.BACKGROUND = (250, 248, 239)

        # Game items and colors
        self.TABLE_COLOR = (119, 110, 101)
        self.TABLE_SIZE = 500
        self.TABLE_X = (self.WIDTH - self.TABLE_SIZE) // 2
        self.TABLE_Y = (self.HEIGHT - self.TABLE_SIZE) // 2

        # TILES
        self.DEFAULT_TILE = (205, 193, 180)
        self.TILE_SIZE = 200
        self.TILE_WIDTH = self.TILE_SIZE // 2
        self.TILE_HEIGHT = self.TILE_SIZE // 2
        self.TILE_SPACING = self.TILE_SIZE // 10

    def GAMESTATUS(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def SET_SCREEN(self):
        self.SCREEN.fill(self.BACKGROUND)

    def GAMETABLE(self):
        pygame.draw.rect(
            self.SCREEN,
            self.TABLE_COLOR,
            (self.TABLE_X, self.TABLE_Y, self.TABLE_SIZE, self.TABLE_SIZE),
        )

    def TILE(self):
        pass

    def UPDATE_SCREEN(self, FPS=60):
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
