class Director:
    """controls the flow of the game."""

    def __init__(self, current_card, next_card):
        self._current_card = current_card
        self._next_card = next_card
        self._player_guess = ""
        self._score = 300
        self._continue_game = 'y'

    def start_game(self):
        while self._continue_game.lower() == 'y':
            self.do_updates()
            self.get_inputs()
            self.do_outputs()

    def get_inputs(self):
        print(f"The card is {self._current_card.get_value()}")
        self._player_guess = input("higher or lower? [h/l] ")

    def do_updates(self):
        self._current_card.set_value(self._next_card.get_value())
        while self._current_card.get_value() == self._next_card.get_value():
            self._next_card.randomize_value()

    def do_outputs(self):
        print(f"Next card was {self._next_card.get_value()}")
        self.calculate_player_points()
        print(f"Your score is: {self._score}")
        self._continue_game = input("Play again? [y/n]")
        if self._score < 1:
            self._continue_game = 'n'
        

    def calculate_player_points(self):
        card_comparison = ""
        if self._next_card.get_value() > self._current_card.get_value():
            card_comparison = "h"
        else: card_comparison = "l"
        if self._player_guess.lower() == card_comparison:
            self._score += 100
        else: self._score += -75

