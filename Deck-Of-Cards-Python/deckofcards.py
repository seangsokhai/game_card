import random

score = []
money = []
name = []


class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    # Implementing build in methods so that you can print a card object
    def __unicode__(self):
        return self.show()

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()

    def show(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value

        return "{} of {}".format(val, self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            card.show()

    # Generate 52 cards
    def build(self):
        self.cards = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))

    # Shuffle the deck
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            # This is the fisher yates shuffle algorithm
            for i in range(length - 1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
            # You can also use the build in shuffle method
            # random.shuffle(self.cards)

    # Return the top card
    def deal(self):
        return self.cards.pop()


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
    print("ME POK _________________________________________________")
    print(name[3], "score:", score[3], ",", "total money:", money[3])

myDeck = Deck()
myDeck.shuffle()

while True:
        
    print("==================================")
    print("====== Welcome to jak pok =======")
    print("==================================")
    print("Rule: Allow 3 players vs ME POK\nME POK is last input\nWin +1$ and lose -1$")
    count = 1
    while count <= 4:
        if count == 4:
            a = input("Me POK's name:\n>>> ")
        else:
            a = input("Player {}'s name:\n>>> ".format(count))
        try:
            b = int(input("Money to play:\n>>> "))
            player1 = Player(a, b)
            player1.sayHello()
            player1.draw(myDeck, 2)
            player1.showHand()
            add = input("Do you want to add 1 more card ?[Y/N]\n >>> ")
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
        except:
            ValueError
    winner()

    again = input("Do you want to play again?[Y/N]")
    if again == Y or again == y:
        continue
    else:
        break