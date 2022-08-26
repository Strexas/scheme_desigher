import math

import pygame as pg

window = pg.display.set_mode((1000, 500))


class DrawWindow:
    def __init__(self):
        self.surface = pg.surface.Surface((1000, 470))
        self.surface.fill('white')
        self.original_window = window.copy()
        self.button = 'hand'
        self.prev_mouse = (0, 0, 0, 0, 0)
        self.font = pg.font.SysFont('latohairline', 15)
        self.line_begin = False
        self.rect_begin = False
        self.circle_begin = False
        self.draw_objects = []

    def draw(self):
        window.blit(self.surface, (0, 30))

        pos = pg.mouse.get_pos()

        if pos[1] >= 40:
            pg.draw.circle(window, 'black', pos, 2)
            text = self.font.render('  {}, {}  '.format(*pos), False, 'black')
            rect = text.get_rect()
            rect.bottomleft = pos
            window.blit(text, rect)
            pg.draw.rect(window, 'black', rect, 1)

            if self.line_begin and self.button == 'line':
                pg.draw.line(window, 'black', self.line_begin, pos, 1)

            if self.rect_begin and self.button == 'rect':
                w, h = abs(pos[0] - self.rect_begin[0]), abs(pos[1] - self.rect_begin[1])
                x_b, y_b = min(pos[0], self.rect_begin[0]), min(pos[1], self.rect_begin[1])
                pg.draw.rect(window, 'black', (x_b, y_b, w, h), 1)

            if self.circle_begin and self.button == 'circle':
                r = math.sqrt(pow(pos[0] - self.circle_begin[0], 2) + pow(pos[1] - self.circle_begin[1], 2))
                pg.draw.circle(
                    window,
                    'black',
                    (self.circle_begin[0], self.circle_begin[1]),
                    min(self.circle_begin[1] - 30, r),
                    1
                )

    def hand(self):
        pos = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.USEREVENT:
                self.button = event.button

            if self.prev_mouse[0] and not pg.mouse.get_pressed()[0] and pos[1] >= 40:
                if self.button == 'point':
                    pg.draw.circle(self.surface, 'black', (pos[0], pos[1] - 30), 2)

                if self.button == 'line':
                    if self.line_begin:
                        line_begin = (self.line_begin[0], self.line_begin[1] - 30)
                        line_end = (pos[0], pos[1] - 30)
                        pg.draw.line(self.surface, 'black', line_begin, line_end, 1)
                        self.line_begin = False
                    else:
                        self.line_begin = pos

                if self.button == 'rect':
                    if self.rect_begin:
                        w, h = abs(pos[0] - self.rect_begin[0]), abs(pos[1] - self.rect_begin[1])
                        x_b, y_b = min(pos[0], self.rect_begin[0]), min(pos[1], self.rect_begin[1])
                        pg.draw.rect(self.surface, 'black', (x_b, y_b - 30, w, h), 1)
                        self.rect_begin = False
                    else:
                        self.rect_begin = pos

                if self.button == 'circle':
                    if self.circle_begin:
                        r = math.sqrt(pow(pos[0] - self.circle_begin[0], 2) + pow(pos[1] - self.circle_begin[1], 2))
                        pg.draw.circle(
                            self.surface,
                            'black',
                            (self.circle_begin[0], self.circle_begin[1] - 30),
                            min(r, self.circle_begin[1] - 30),
                            1
                        )
                        self.circle_begin = False
                    else:
                        self.circle_begin = pos

        self.prev_mouse = pg.mouse.get_pressed()
