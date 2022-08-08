import pygame as pg


window = pg.display.set_mode((1000, 500))


class EventHandler:
    def __init__(self):
        self.live = True
        self.quit_event = pg.event.Event(pg.QUIT)
        self.font = pg.font.SysFont('latohairline', 25)
        self.window = 'MainWindow'
        self.pressed_button = 'Hand'

    def hand(self):
        if pg.key.get_pressed()[pg.K_q]:
            self.live = False
            return
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.live = False
                return

            if self.window == 'MainWindow':
                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        x, y = event.pos
                        if 450 <= x <= 550 and 180 <= y <= 230:
                            self.window = 'DrawWindow'
                        if 450 <= x <= 550 and 260 <= y <= 310:
                            self.live = False
                            return
