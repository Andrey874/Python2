import random
from pprint import pprint
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
        'Spades': '♠',
        'Clubs': '♣',
        'Diamonds': '♦',
        'Hearts': '♥'
}

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def __str__(self):
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def __repr__(self):
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        if self.value == other_card.value:
            return SUITS.index(self.suit) > SUITS.index(other_card.suit)
        return VALUES.index(self.value) > VALUES.index(other_card.value)

    def __gt__(self, other_card):
        return self.more(other_card)

    def less(self, other_card):
        if self.value == other_card.value:
            return SUITS.index(self.suit) < SUITS.index(other_card.suit)
        return VALUES.index(self.value) < VALUES.index(other_card.value)

    def __lt__(self, other_card):
        return self.less(other_card)

class Deck():
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(value, suit))

    def __str__(self):
        cards_list = []
        for card in self.cards:
            cards_list.append(str(card))
        return f'{", ".join(cards_list)}'

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        deck_show = []
        for card in self.cards:
            deck_show.append(str(card))
        print(f'deck[{len(deck_show)}]  {", ".join(deck_show)}')

    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        draw_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return draw_cards

    def shuffle(self):
        random.shuffle(self.cards)

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):
        return f'cards {self.hand}'

    def take(self, defl, attl):
        self.hand.extend(defl)
        self.hand.extend(attl)
        return self.hand

    def take_from_deck(self, obj, how):
        return self.hand.extend(obj.draw(how))

class Game:
    def __init__(self):
        self.player1 = Player('player1')
        self.player2 = Player('player2')
        self.deck = Deck()

    def seeding(self):
        self.deck.shuffle()
        self.player1.take_from_deck(self.deck, 10)
        self.player2.take_from_deck(self.deck, 10)
        self.player1.hand.sort()
        self.player1.hand.sort()
        print(f'Карты player1: {self.player1.hand} , карты player2: {self.player2.hand}')

    def game(self):
        attacker = self.player1
        defender = self.player2

        while len(attacker.hand) > 0 and len(defender.hand) > 0:
              print(f"Attacker's turn {attacker}")
              att_lst = []
              def_lst = []
              hod_1 = min(attacker.hand)
              att_lst.append(hod_1)
              attacker.hand.remove(hod_1)
              def_cards = [card for card in defender.hand if card.equal_suit(hod_1) and card > hod_1]
              if len(def_cards):
                 def_lst.append(min(def_cards))
                 defender.hand.remove(min(def_cards))
                 while len(att_lst) > len(def_lst) or len(def_lst):
                       yet_card = [card for card in attacker.hand if def_lst[0].value == card.value or att_lst[0].value == card.value]
                       print(f'{yet_card =}')
                       if len(yet_card):
                          att_lst.extend(yet_card)
                          for card in yet_card:
                              attacker.hand.remove(card)
                              yet_card.clear()
                              step = 0
                              while step < len(att_lst) - 1:
                                    step += 1
                                    defending_cards = [card for card in defender.hand if card.equal_suit(att_lst[step]) and card > att_lst[step]]
                                    if len(defending_cards) > 0:
                                       print(f'атакер докидывает {att_lst[step]}')
                                       def_lst.append(min(defending_cards))
                                       print(f'дефендер пробует бить {min(defending_cards)}')
                                       defender.hand.remove(min(defending_cards))
                                       print(f'Лист атаки {att_lst}')
                                       print(f'лист защиты {def_lst}')
                                       one_more_card = [card for card in attacker.hand if def_lst[step - 1].value == card.value]
                                       print(f'{one_more_card = }')
                                       if 0 < len(one_more_card) <= 10 and (len(att_lst) + len(one_more_card)) <= len(defender.hand) or len(att_lst) <= 10:
                                          att_lst.extend(one_more_card)
                                          print(one_more_card)
                                          for card in one_more_card:
                                              attacker.hand.remove(card)
                                    elif len(defender.hand) < 1 and len(att_lst) == len(def_lst):
                                         def_lst.clear()
                                         att_lst.clear()
                                         attacker.take_from_deck(self.deck, (10 - len(attacker.hand)))
                                         defender.take_from_deck(self.deck, (10 - len(defender.hand)))
                                         attacker, defender = defender, attacker
                       att_lst.clear()
                       def_lst.clear()
                       attacker.take_from_deck(self.deck, (10 - len(attacker.hand)))
                       defender.take_from_deck(self.deck, (10 - len(defender.hand)))
                       attacker, defender = defender, attacker
              defender.hand.extend(att_lst)
              defender.hand.extend(def_lst)
              attacker.take_from_deck(self.deck, (10 - len(attacker.hand)))
              att_lst.clear()
              def_lst.clear()

        if len(self.player1.hand) == 0:
            print("Player 1 wins!")
        elif len(self.player2.hand) == 0:
            print("Player 2 wins!")
        else:
           print("Draw")

game = Game()
game.seeding()
game.game()