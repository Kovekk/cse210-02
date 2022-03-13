from game.director import Director
from game.card import Card

def main():
    """satisfy python"""
    current_card = Card()
    next_card = Card()
    director = Director(current_card, next_card)
    director.start_game()


if __name__ == "__main__":
    main()