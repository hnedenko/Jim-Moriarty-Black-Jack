import pygame
import sys
from sources import RGB

from screeninfo import get_monitors
for m in get_monitors():
    print(str(m))

FPS = 28

"♥ ♠ ♦ ♣"

screen = pygame.display.set_mode((720, 480))

while True:
    # Redraw display
    screen.fill(RGB.PARCHMENT)
    pygame.time.Clock().tick(FPS)

    # Main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Redraw display
    pygame.display.flip()
