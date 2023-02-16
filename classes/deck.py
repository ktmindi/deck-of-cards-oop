from classes.card import Card
from random import shuffle

class Deck:


    def __init__( self ):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

    def show_cards(self):
        for card in self.cards:
            card.card_info()
