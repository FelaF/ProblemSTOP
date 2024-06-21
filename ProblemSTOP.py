"""Using this File for potential problem solving with The Odin Project"""
import random


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

class Deck():
    def __init__(self):
        DeckValue = ListOCards
    
    def PassingPreflop(Deck, *Players):
        for each in ListOCards:
            random.shuffle(each)
        random.shuffle(ListOCards)
        """TEST ON LINE 18 ()"""
        
        Card1 = (ListOCards[random.randint(0,3)][random.randint(0,12)])
        for EachSuit in ListOCards:
            for Card in EachSuit:
                if (Card1 == Card):
                    CardIndex = EachSuit.index(Card)
                    
                    print(CardIndex)
        

class Player:
    Players = 0
    def __init__(self, name, chips = 0):
        self.name = name
        self.chips = chips
        self.hand = []
        self.display = ""


    

class Game:
    Table_Hand = []

    def __init__(self,Pot, *Players):
        self.pot = Pot
        self.players = Players


    @staticmethod
    def Play():
        return

    

if __name__ == '__main__':
    AJ = Player("AJ",chips=100)
    Jeff = Player("Jeff", chips=100)
    Jim = Player('Jim', chips=20)
    Christmas = Deck()
    Christmas.PassingPreflop(AJ,Jim,Jeff)



