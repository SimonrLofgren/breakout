#from config import *
import pygame
import random


class Object:
    def __init__(self, x, y, screen, is_bouncy, is_indestructable):
        self.x = x
        self.y = y
        self.screen = screen
        self.is_indestructable = is_indestructable
        self.is_bouncy = is_bouncy

    def is_bouncy(self):
        if self.is_bouncy == True:
            return True
        else:
            return False
    def is_indestructable(self):
        if self.is_indestructable == True:
            return True
        else:
            return False