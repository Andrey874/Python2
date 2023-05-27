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

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        return VALUES.index(self.value) > VALUES.index(other_card.value)


cards = []
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
for card in VALUES:
    for suit in SUITS:
        tmp_card = Card(card, suit)
        cards.append(tmp_card.to_str())

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ....
count = 0
for i in cards:
    count += 1
print(f'cards{[count]}' + ", ".join(cards))