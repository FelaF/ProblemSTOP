import random 
class Game:
    pass
class Player:
    Round_Count = 0
    Game_Display = ""
    def __init__(self, Name, Age, Wallet, Hand = [], Display = ""):
        self.name = Name
        self.Display = Display
        self.age = Age
        self.wallet = Wallet
        self.hand = Hand
    


Cards = {
    'Ace of Spades' : 1,
    'Two of Spades' : 1,
    'Three of Spades' : 1,
    'Four of Spades' : 1,
    'Five of Spades' : 1,
    'Six of Spades' : 1,
    'Seven of Spades' : 1,
    'Eight of Spades' : 1,
    'Nine of Spades' : 1,
    'Ten of Spades' : 1,
    'Jack of Spades' : 1,
    'Queen of Spades' : 1,
    'King of Spades' : 1,
    'Ace of Hearts' : 1,
    'Two of Hearts' : 1,
    'Three of Hearts' : 1,
    'Four of Hearts' : 1,
    'Five of Hearts' : 1, 
    'Six of Hearts' : 1,
    'Seven of Hearts' : 1,
    'Eight of Hearts' : 1,
    'Nine of Hearts' : 1,
    'Ten of Hearts' : 1,
    'Jack of Hearts' : 1,
    'Queen of Hearts' : 1,
    'King of Hearts' : 1,
    'Ace of Diamonds' : 1,
    'Two of Diamonds' : 1,
    'Three of Diamonds' : 1,
    'Four of Diamonds' : 1,
    'Five of Diamonds' : 1,
    'Six of Diamonds' : 1,
    'Seven of Diamonds' : 1,
    'Eight of Diamonds' : 1,
    'Nine of Diamonds' : 1,
    'Ten of Diamonds' : 1,
    'Jack of Diamonds' : 1,
    'Queen of Diamonds' : 1,
    'King of Diamonds' : 1, 
    'Ace of Clubs' : 1,
    'Two of Clubs' : 1,
    'Three of Clubs' : 1,
    'Four of Clubs' : 1,
    'Five of Clubs' : 1,
    'Six of Clubs' : 1,
    'Seven of Clubs' : 1,
    'Eight of Clubs' : 1,
    'Nine of Clubs' : 1,
    'Ten of Clubs' : 1,
    'Jack of Clubs' : 1,
    'Queen of Clubs' : 1,
    'King of Clubs' : 1
}


class Deck:
    def __init__(self, Name, Deck = Cards):
        self.Deck = Deck
        self.Name = Name

    def GetDeck(self):
        return self.Deck
    
    def GetDeckValue(self,value):
        return self.Deck.get(value)
    
    def GetTwoCardsfromDeck(self):
        CalculationDeck = list(self.Deck.keys())
        Cards = random.sample(CalculationDeck, k=2)
        """There are two deck used here, one for random calculations (list) and another for the working directory"""
        for each in Cards:
            self.Deck[each] = 0
            CalculationDeck.remove(each)
        return f"{Cards[0]} and {Cards[1]}"




        
        
    




def main():
    Batman = Deck("AJ")
    Ajani = Player("AJ", 22, 1000)
    Jeff = Player("Jeff", 35, 2000)
    P2 = Player("Jamie", 44, 1500)
    P1 = Player("Charles", 18, 1000)
    x = (Batman.GetTwoCardsfromDeck())
    print(x)

if __name__ == "__main__":
    main()