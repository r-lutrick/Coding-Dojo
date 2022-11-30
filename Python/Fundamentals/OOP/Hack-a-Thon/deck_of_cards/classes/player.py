from .deck import Deck
class Player:
    players = []

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total = 0
        self.turn = False

    def hit(self):
        card = Deck.deal_card()
        self.hand.append(card)
        return self

    def stay(self):
        self.turn = False

    def get_total(self):
        sum = 0
        for i in self.hand:
            sum += i.point_val
        return sum