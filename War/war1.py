import random
class deck:
    def __init__(self):
        self.cards = [i for i in range(2,11)]
        self.cards_upper = ["J", "Q", "K", "A"]
        for i in range(len(self.cards_upper)):
            self.cards.append(self.cards_upper[i])


        self.card_type = ["C", "S", "H", "D"]    
        self.real_cards = [[0 for i in range(2)] for j in range(52)]
    def generatedeck(self):
        counter = 0
        for i in range(4):
            for j in range(13):
                self.real_cards[counter][0] = self.card_type[i]
                self.real_cards[counter][1] = self.cards[j]
                counter += 1
        return self.real_cards

    def compare_cards(self, card1, card2):
        value1 = self.cards.index(card1[1])
        value2 = self.cards.index(card2[1])
        return value1, value2

    def compare_cards_(self, card1, card2):
        value1 = self.cards.index(card1[1])
        value2 = self.cards.index(card2[1])
        if value1 > value2:
            return 1
        elif value2 > value1:
            return -1
        else:
            return 0

    def shuffle_deck(self):
        unshuffed = []
        for i in range(len(self.real_cards)):
            randnum = random.randrange(len(self.real_cards))
            unshuffed.append(self.real_cards.pop(randnum))
        return unshuffed


x = deck()
real_cards = x.generatedeck()
print(real_cards)
print("\n\n")
shuffled_cards = x.shuffle_deck()
print(shuffled_cards)
print(len(shuffled_cards))
card1= shuffled_cards[13]
print(card1)
card2= shuffled_cards[25]
print(card2)
xx, y = x.compare_cards(card1, card2)
print(xx, y)
cards2 = deck()
cards2.generatedeck()
cards2 = cards2.shuffle_deck()

compare_cards = x.compare_cards_(card1, card2)
print(compare_cards)
