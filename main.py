import pygame as pg

pg.init()

from MainWindow import MainWindow
from EventHandler import EventHandler
from ToolBox import ToolBox
from DrawWindow import DrawWindow


window = pg.display.set_mode((1000, 500), vsync=1)
pg.display.set_caption('strexas')

main_window = MainWindow()
event_handler = EventHandler()
clock = pg.time.Clock()


while event_handler.live:
    clock.tick(60)
    event_handler.hand()
    if event_handler.window == 'DrawWindow':
        window.fill('black')
        tool_box = ToolBox()
        draw_window = DrawWindow()
        event_handler.window = 'Drawing'
    elif event_handler.window == 'Drawing':
        tool_box.hand()
        draw_window.draw()
    pg.display.flip()
pg.quit()
