"""Using this File for potential problem solving with The Odin Project"""
import random
from random import shuffle, randint


Diamonds = ['Ace of Diamonds', 'Two of Diamonds', 'Three of Diamonds', 'Four of Diamonds', 'Five of Diamonds', 'Six of Diamonds', 'Seven of Diamonds', 'Eight of Diamonds', 'Nine of Diamonds', 'Ten of Diamonds' , 'Jack of Diamonds' , 'Queen of Diamonds' , 'King of Diamonds']
Hearts = ['Ace of Hearts', 'Two of Hearts', 'Three of Hearts', 'Four of Hearts', 'Five of Hearts', 'Six of Hearts', 'Seven of Hearts', 'Eight of Hearts', 'Nine of Hearts', 'Ten of Hearts' , 'Jack of Hearts' , 'Queen of Hearts' , 'King of Hearts']
Clubs = ['Ace of Clubs', 'Two of Clubs', 'Three of Clubs', 'Four of Clubs', 'Five of Clubs', 'Six of Clubs', 'Seven of Clubs', 'Eight of Clubs', 'Nine of Clubs', 'Ten of Clubs' , 'Jack of Clubs' , 'Queen of Clubs' , 'King of Clubs']
Spades = ['Ace of Spades', 'Two of Spades', 'Three of Spades', 'Four of Spades', 'Five of Spades', 'Six of Spades', 'Seven of Spades', 'Eight of Spades', 'Nine of Spades', 'Ten of Spades' , 'Jack of Spades' , 'Queen of Spades' , 'King of Spades']
ListOCards = [Diamonds, Hearts, Clubs, Spades]

OGList = ['Ace of Diamonds', 'Two of Diamonds', 'Three of Diamonds', 'Four of Diamonds',
           'Five of Diamonds', 'Six of Diamonds', 'Seven of Diamonds', 'Eight of Diamonds', 
           'Nine of Diamonds', 'Ten of Diamonds' , 'Jack of Diamonds' , 'Queen of Diamonds' , 
           'King of Diamonds','Ace of Hearts', 'Two of Hearts', 'Three of Hearts', 'Four of Hearts', 
           'Five of Hearts', 'Six of Hearts', 'Seven of Hearts', 'Eight of Hearts', 'Nine of Hearts', 
           'Ten of Hearts' , 'Jack of Hearts' , 'Queen of Hearts' , 'King of Hearts','Ace of Clubs', 
           'Two of Clubs', 'Three of Clubs', 'Four of Clubs', 'Five of Clubs', 'Six of Clubs', 
           'Seven of Clubs', 'Eight of Clubs', 'Nine of Clubs', 'Ten of Clubs' , 'Jack of Clubs' , 
           'Queen of Clubs' , 'King of Clubs','Ace of Spades', 'Two of Spades', 'Three of Spades', 
           'Four of Spades', 'Five of Spades', 'Six of Spades', 'Seven of Spades', 'Eight of Spades',
             'Nine of Spades', 'Ten of Spades' , 'Jack of Spades' , 'Queen of Spades' , 'King of Spades']


class Player:
    Playees = 0
    hand = []

    def __init__(self, name, chips = 0):
        self.name = name
        self.chips = chips
        self.display = ""

        
class Game:
    Table_Hand = []
    Players = 0

    def __init__(self,pot, Players):
        self.pot = pot
        self.Players = Players
    

    @staticmethod
    def Play():
        return
    
class Deck():
    Playees = []
    def __init__(self, DeckValue = L):
        self.deckValue = DeckValue
    

    def GetCards(Deck):
        return Deck.deckValue()

    def PassingAnything(Deck, *Playee):
        Playee = []
        for Player in Playee:
            Playee += Player
            continue
        return Playee

        



    

if __name__ == '__main__':
    AJ = Player("AJ",chips=100)
    John = Player("John", chips=150)
    print(AJ.hand)
    print(AJ.chips)
    BatmanDeck = Deck()
    print(BatmanDeck)
    print(BatmanDeck.GetCards)
    print(BatmanDeck.PassingAnything(AJ,John))



