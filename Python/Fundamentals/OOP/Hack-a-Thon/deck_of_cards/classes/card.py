class Card:

    def __init__( self , suit , point_val , string_val ):
        
        self.suit = suit

        if point_val > 10:
            self.point_val = 10
        else:
            self.point_val = point_val

        self.string_val = string_val

    def card_info(self):
        print(f"{self.string_val} of {self.suit} : {self.point_val} points")

