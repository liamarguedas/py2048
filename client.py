import sys, pygame

pygame.init()

# Window settings
WIDTH = 600
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("py2048")

# Game items and colors
BACKGROUND = (250, 248, 239)

TABLE_COLOR = (119, 110, 101)
TABLE_SIZE = 500
TABLE_X = (WIDTH - TABLE_SIZE) // 2
TABLE_Y = (HEIGHT - TABLE_SIZE) // 2

# TILES
DEFAULT_TILE_COLOR = (205,193,180)

TILE_SIZE = 200

TILE_WIDTH = TILE_SIZE // 2
TILE_HEIGHT = TILE_SIZE // 2

TILE_SPACING = TILE_SIZE // 10

TITLE_STARTING_X = TILE_SPACING + TABLE_X
TITLE_STARTING_Y = TILE_SPACING + TABLE_Y

while True:
    # Quit while loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Drawing the main window
    SCREEN.fill(BACKGROUND)

    # 2048 TABLE
    pygame.draw.rect(SCREEN, TABLE_COLOR, (TABLE_X, TABLE_Y, TABLE_SIZE, TABLE_SIZE))

    # TILES
    pygame.draw.rect(SCREEN, DEFAULT_TILE_COLOR, (TITLE_STARTING_X, TITLE_STARTING_Y, TILE_WIDTH, TILE_HEIGHT))
    pygame.draw.rect(SCREEN, DEFAULT_TILE_COLOR, ((TITLE_STARTING_X + TILE_WIDTH + TILE_SPACING), TITLE_STARTING_Y, TILE_WIDTH, TILE_HEIGHT))
    pygame.draw.rect(SCREEN, DEFAULT_TILE_COLOR, (TITLE_STARTING_X + (TILE_WIDTH * 2) + (TILE_SPACING * 2), TITLE_STARTING_Y, TILE_WIDTH, TILE_HEIGHT))
    pygame.draw.rect(SCREEN, DEFAULT_TILE_COLOR, (TITLE_STARTING_X + (TILE_WIDTH * 3) + (TILE_SPACING * 3), TITLE_STARTING_Y, TILE_WIDTH, TILE_HEIGHT))

    # Update the display
    pygame.display.flip()

    # FPS Controller
    pygame.time.Clock().tick(60)  # FPS
