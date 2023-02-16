from classes.deck import Deck
from classes.player import Player

class Game:
    def __init__(self):
        name1 = input("What is your name Player 1?")
        name2 = input("What is your name Player 2?")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self,winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)
    
    def draw_card(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} and {} drew {}"
        d = d.format(p1n,
                     p1c,
                     p2n,
                     p2c)
        print(d)
    
    def play_game(self):
        cards = self.deck.cards
        print("Let the war begin!")
        while len(cards) >= 2:
            m = "q to quit. Any" + "key to play:"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.remove_card()
            p2c = self.deck.remove_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw_card(p1n,
                      p1c,
                      p2n,
                      p2c)
            if p1c > p2c:
                self.p1.wins +=1
                self.wins(self.p1.name)
            else:
                self.p2.wins +=1
                self.wins(self.p2.name)
        win = self.winner(self.p1,
                          self.p2)
        print("War is over. {} wins" .format(win))
    
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

game = Game()
game.play_game()