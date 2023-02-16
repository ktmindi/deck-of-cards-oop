class Card:
    #class attributes defined outside of any instance - this attribute is shared among all instances of the class
    suits = "Spades" ,"Clubs", "Diamonds", "Hearts"
    values = None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"

#attributes our class card contains: suit, point_val, and string_val
    
    def __init__( self , value , suit ): #init is our constructor method
        self.value = value
        self.suit = suit
        self.deck = None

    # this method will display the information of the card
    def card_info(self):
        print(f"{Card.values[self.value]} of {Card.suits[self.suit]} ")
    
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] +\
            " of " + \
            self.suits[self.suit]
        return v