from game import *
import pygame

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
        self.TILE_INITX = self.TILE_SPACING + self.TABLE_X
        self.TILE_INITY = self.TILE_SPACING + self.TABLE_Y
        self.TILES_COLORS = {
            0: self.DEFAULT_TILE,
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 207, 114),
            512: (237, 207, 114),
            1024: (237, 207, 114),
            2048: (237, 207, 114),
        }

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

    def UPDATE_TABLE(self, values: list):
        # FIRST ROW ------------------------------------------------------------------------------
        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[0][0]],
            (self.TILE_INITX, self.TILE_INITY, self.TILE_HEIGHT, self.TILE_WIDTH),
        )

        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[0][1]],
            (
                (self.TILE_INITX + self.TILE_SPACING + self.TILE_WIDTH),
                self.TILE_INITY,
                self.TILE_HEIGHT,
                self.TILE_WIDTH,
            ),
        )

        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[0][2]],
            (
                (self.TILE_INITX + (self.TILE_SPACING * 2) + (self.TILE_WIDTH * 2)),
                self.TILE_INITY,
                self.TILE_HEIGHT,
                self.TILE_WIDTH,
            ),
        )

        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[0][3]],
            (
                (self.TILE_INITX + (self.TILE_SPACING * 3) + (self.TILE_WIDTH * 3)),
                self.TILE_INITY,
                self.TILE_HEIGHT,
                self.TILE_WIDTH,
            ),
        )
        # ---------------------------------------------------------------------------------------
        # SECOND ROW ----------------------------------------------------------------------------
        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[1][0]],
            (
                self.TILE_INITX,
                (self.TILE_INITY + self.TILE_SPACING + self.TILE_HEIGHT),
                self.TILE_HEIGHT,
                self.TILE_WIDTH,
            ),
        )

        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[1][1]],
            (
                (self.TILE_INITX + self.TILE_SPACING + self.TILE_WIDTH),
                (self.TILE_INITY + self.TILE_SPACING + self.TILE_HEIGHT),
                self.TILE_HEIGHT,
                self.TILE_WIDTH,
            ),
        )

        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[1][2]],
            (
                (self.TILE_INITX + (self.TILE_SPACING * 2) + (self.TILE_WIDTH * 2)),
                (self.TILE_INITY + self.TILE_SPACING + self.TILE_HEIGHT),
                self.TILE_HEIGHT,
                self.TILE_WIDTH,
            ),
        )

        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[1][2]],
            (
                (self.TILE_INITX + (self.TILE_SPACING * 3) + (self.TILE_WIDTH * 3)),
                (self.TILE_INITY + self.TILE_SPACING + self.TILE_HEIGHT),
                self.TILE_HEIGHT,
                self.TILE_WIDTH,
            ),
        )
        # ---------------------------------------------------------------------------------------
        # THIRD ROW ----------------------------------------------------------------------------
        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[2][0]],
            (
                self.TILE_INITX,
                (self.TILE_INITY + (self.TILE_SPACING * 2) + (self.TILE_HEIGHT * 2)),
                self.TILE_HEIGHT,
                self.TILE_WIDTH,
            ),
        )

        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[2][1]],
            (
                (self.TILE_INITX + self.TILE_SPACING + self.TILE_WIDTH),
                (self.TILE_INITY + (self.TILE_SPACING * 2) + (self.TILE_HEIGHT * 2)),
                self.TILE_HEIGHT,
                self.TILE_WIDTH,
            ),
        )

        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[2][2]],
            (
                (self.TILE_INITX + (self.TILE_SPACING * 2) + (self.TILE_WIDTH * 2)),
                (self.TILE_INITY + (self.TILE_SPACING * 2) + (self.TILE_HEIGHT * 2)),
                self.TILE_HEIGHT,
                self.TILE_WIDTH,
            ),
        )

        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[2][2]],
            (
                (self.TILE_INITX + (self.TILE_SPACING * 3) + (self.TILE_WIDTH * 3)),
                (self.TILE_INITY + (self.TILE_SPACING * 2) + (self.TILE_HEIGHT * 2)),
                self.TILE_HEIGHT,
                self.TILE_WIDTH,
            ),
        )

        # ---------------------------------------------------------------------------------------
        # FOURTH ROW ----------------------------------------------------------------------------
        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[3][0]],
            (
                self.TILE_INITX,
                (self.TILE_INITY + (self.TILE_SPACING * 3) + (self.TILE_HEIGHT * 3)),
                self.TILE_HEIGHT,
                self.TILE_WIDTH,
            ),
        )

        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[3][1]],
            (
                (self.TILE_INITX + self.TILE_SPACING + self.TILE_WIDTH),
                (self.TILE_INITY + (self.TILE_SPACING * 3) + (self.TILE_HEIGHT * 3)),
                self.TILE_HEIGHT,
                self.TILE_WIDTH,
            ),
        )

        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[3][2]],
            (
                (self.TILE_INITX + (self.TILE_SPACING * 2) + (self.TILE_WIDTH * 2)),
                (self.TILE_INITY + (self.TILE_SPACING * 3) + (self.TILE_HEIGHT * 3)),
                self.TILE_HEIGHT,
                self.TILE_WIDTH,
            ),
        )

        pygame.draw.rect(
            self.SCREEN,
            self.TILES_COLORS[values[3][2]],
            (
                (self.TILE_INITX + (self.TILE_SPACING * 3) + (self.TILE_WIDTH * 3)),
                (self.TILE_INITY + (self.TILE_SPACING * 3) + (self.TILE_HEIGHT * 3)),
                self.TILE_HEIGHT,
                self.TILE_WIDTH,
            ),
        )

    def UPDATE_SCREEN(self, FPS=60):
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
