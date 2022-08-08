import pygame as pg

window = pg.display.set_mode((1000, 500))


class DrawWindow:
    def __init__(self):
        self.surface = pg.surface.Surface((1000, 470))
        self.surface.fill('white')
        self.original_window = window.copy()
        self.button = 'hand'
        self.prev_mouse = (0, 0, 0, 0, 0)

    def draw(self):
        window.blit(self.surface, (0, 30))

        pos = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.USEREVENT:
                self.button = event.button
            if self.prev_mouse[0] and not pg.mouse.get_pressed()[0] and pos[1] > 30:
                if self.button == 'point':
                    pg.draw.circle(self.surface, 'black', (pos[0], pos[1] - 30), 2)

        self.prev_mouse = pg.mouse.get_pressed()

        if self.button == 'point' and pos[1] >= 40:
            pg.draw.circle(window, 'black', pos, 2)