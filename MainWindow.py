import pygame as pg


window = pg.display.set_mode((1000, 500))


class MainWindow:
    def __init__(self):
        font = pg.font.SysFont('latohairline', 30)

        self.surface = pg.surface.Surface((1000, 500))

        self.start_button = [self.surface, 'white', (450, 180, 100, 50), 1]
        self.start_text = font.render('START', False, 'white')
        self.start_rect = self.start_text.get_rect()
        self.start_rect.center = (500, 205)

        self.quit_button = [self.surface, 'white', (450, 260, 100, 50), 1]
        self.quit_text = font.render('QUIT', False, 'white')
        self.quit_rect = self.quit_text.get_rect()
        self.quit_rect.center = (500, 285)
        self.render()

    def render(self):
        pg.draw.rect(*self.start_button)
        self.surface.blit(self.start_text, self.start_rect)

        pg.draw.rect(*self.quit_button)
        self.surface.blit(self.quit_text, self.quit_rect)

        window.blit(self.surface, (0, 0))
