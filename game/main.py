import random
class Card():
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def show_card(self):
        print("{} of {}".format(self.color, self.value))

class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def drawCard(self):
        return self.cards.pop()
class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    def show_hand(self):
        for card in self.hand:
            card.show_card()

    def discard(self):
        return self.hand.pop()


