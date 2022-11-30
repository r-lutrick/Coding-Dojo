from .deck import Deck
class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total = self.get_total()
        self.turn = True

    def hit(self, card):
        self.hand.append(card)
        self.turn = True
        return self

    def stay(self):
        self.turn = False

    def get_total(self):
        sum = 0
        for i in self.hand:
            sum += i.point_val
        return int(sum)
    
    def display_hand(self):
        for card in self.hand:
            card.card_info()