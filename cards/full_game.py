import random

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


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self, number=0):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        self.number = number
        for suit in SUITS[::-1]:
            for card in VALUES:
                self.cards.append(Card(card, suit))

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        deck_show = []
        for card in self.cards:
            deck_show.append(str(card))
        print(f'deck[{len(deck_show)}]  {", ".join(deck_show)}')

    def __repr__(self):
        show_cards = []
        for card in self.cards:
            show_cards.append(card.to_str())
        return f'deck[{len(self.cards)}]' + ", ".join(show_cards)

    def __iter__(self):
        return iter(self.cards)

    def __next__(self):
        if self.number <= len(self.cards):
            return self.cards[self.number]
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.cards[index]

    def __str__(self):
        show_cards = []
        for card in self.cards:
            show_cards.append(card.to_str())
        return f'deck[{len(self.cards)}]' + ", ".join(show_cards)

    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        draw_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return draw_cards

    def shuffle(self):
        random.shuffle(self.cards)

if __name__ == '__main__':
   deck = Deck()

   deck.shuffle()
   print(F'Колода {deck}')
   print('расдача')
   player1 = deck.draw(10)
   player2 = deck.draw(10)
   deck.show()
   player1.sort()
   player2.sort()
   print('Сортировка')
   print(F'{player1 = }')
   print(F'{player2 = }')