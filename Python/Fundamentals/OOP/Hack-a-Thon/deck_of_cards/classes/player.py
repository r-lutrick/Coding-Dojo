from .deck import Deck


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total = self.get_total()
        self.turn = True

    def hit(self, card):
        if (card.string_val == "Ace"):
            card.card_info()
            choice = input("[1]Low or [2]High\n> ")
            if (choice == "2"):
                card.point_val = 11

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


class Dealer (Player):
    def __init__(self, name):
        super().__init__(name)

    def hit(self, card):
        # Logic for dealer based on current hand value
        if (card.point_val == 1):
            temp_total = self.total + 11
            if (temp_total <= 21):
                card.point_val = 11

        self.hand.append(card)
        self.turn = True
        return self
