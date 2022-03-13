import random

class Card:
    """satisfy python"""

    def __init__(self):
        self._value = 0

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def randomize_value(self):
        self._value = random.randint(1, 13)