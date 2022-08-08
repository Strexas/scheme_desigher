import pygame as pg

window = pg.display.set_mode((1000, 500))


class ToolBox:
    def __init__(self):
        self.surface = pg.Surface((500, 30))
        font = pg.font.SysFont('latohairline', 20)
        self.texts = ['hand', 'point', 'line']
        self.text_buttons = [font.render(i.ljust(6, ' '), False, 'white') for i in self.texts]
        self.text_rects = [i.get_rect() for i in self.text_buttons]
        self.text_rects[0].topleft = (5, 0)
        for i in range(1, len(self.text_rects)):
            self.text_rects[i].topleft = self.text_rects[i - 1].topright
        self.render()

        self.pressed_button = pg.event.Event(pg.USEREVENT, {'button': 'hand'})

    def render(self):
        for i in range(3):
            self.surface.blit(self.text_buttons[i], self.text_rects[i])
            window.blit(self.surface, (0, 0))

    def hand(self):
        mp = pg.mouse.get_pressed()
        if mp[0]:
            pp = pg.mouse.get_pos()
            for i in range(3):
                if self.text_rects[i].collidepoint(pp):
                    self.pressed_button.button = self.texts[i]
                    pg.event.post(self.pressed_button)
                    window.blit(self.surface, (0, 0))
                    pg.draw.rect(window, 'blue', self.text_rects[i], 1)
                    return
        pg.event.post(self.pressed_button)
