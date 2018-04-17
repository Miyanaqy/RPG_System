import pygame

class DrawSystem():
    def __init__(self, screen, interface):
        self.screen = screen
        self.interface = interface

    def draw(self):
        screen.blit(background, background_rect)
        for ui in self.interface:
            ui.draw(screen)

