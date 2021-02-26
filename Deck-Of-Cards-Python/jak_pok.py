
import random
from deck import Deck
from card import Card

score = []
money = []
name = []

class Player(object):
    def __init__(self, name, money):
        self.store = []
        self.name = name
        self.money = money
        self.hand = []
        self.score = []
        # print("hand: ",self.hand)
        # print("name: ",self.name)

    def sayHello(self):
        print("Player {} is {} ".format(count, self.name))
        print("and have: ${}".format(self.money))
        return self

    # Draw n number of cards from a deck
    # Returns true in n cards are drawn, false if less then that
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False
        return True

    # Display all the cards in the players hand
    def showHand(self):
        print("{}'s hand: {}".format(self.name, self.hand))
        return self

    def discard(self):
        return self.hand.pop()

    def value(self):
        store = []
        for i in self.hand:
            string_card = str(i)
            card_value = string_card.split(" ")
            store.append(card_value[0])
        for n, i in enumerate(store):
            if i == "Jack" or i == "Queen" or i == "King":
                store[n] = 0
            elif i == "Ace":
                store[n] = 1
        for i in range(0, len(store)):
            store[i] = int(store[i])
        # for i in store:
        #     print(i)
        if 10 <= sum(store) < 20:
            points = sum(store) - 10
        elif sum(store) >= 20:
            points = sum(store) - 20
        else:
            points = sum(store)
        score.append(points)
        money.append(self.money)
        name.append(self.name)
        print("{}'s points: {}".format(self.name, points))


def winner():
    increase = -1
    for i in score[:-1]:
        increase = increase + 1
        if score[-1] > i:
            mk = money[increase] - 1
            money[increase] = mk
            mm = money[-1] + 1
            money[-1] = mm
        elif score[-1] < i:
            mk = money[increase] + 1
            money[increase] = mk
            mm = money[-1] - 1
            money[-1] = mm
    print(name[0], "score:", score[0], ",", "total money:", money[0])
    print(name[1], "score:", score[1], ",", "total money:", money[1])

    print(name[2], "score:", score[2], ",", "total money:", money[2])
    print(name[3], "score:", score[3], ",", "total money:", money[3])


# Test making a Card
# card = Card('Spades', 6)
# print card
myDeck = Deck()
myDeck.shuffle()
# deck.show()

print("==================================")
print("====== Welcome to jak pok =======")
print("==================================")
count = 1
while count <= 4:

    a = input("Player{}'s name:\n>>> ".format(count))
    b = int(input("Money to play:\n>>> "))
    player1 = Player(a, b)
    player1.sayHello()
    player1.draw(myDeck, 2)
    player1.showHand()
    add = input("Do you want to add ?[Y/N]\n >>> ")
    if add == "Y" or add == "y":
        # x = draw(myDeck,1)
        player1.draw(myDeck)
        player1.showHand()
        player1.value()
    else:
        player1.showHand()
        player1.value() 

    count += 1  
    print("________________________________")
winner()