# Начнем с создания карты
# ♥ ♦ ♣ ♠
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
        self.suit = suit    # Масть карты

    def to_str(self):
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        return VALUES.index(self.value) > VALUES.index(other_card.value)

    def less(self, other_card):
        pass

# # # Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())
#
# # Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
     print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
     print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")

print(card1.more(card2))