from turtle import Turtle,Screen
import time

class Pause():
    def __init__(self):
        self.paused = False
        self.paused
        self.pause_game()

    def pause_game(self):
        if not self.paused:
            self.paused = True
        elif self.paused:
            self.paused = False

