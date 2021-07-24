import sys
from Deck import Deck, Card

class Hand:
    def __init__(self, isDealer):
        self.cards = []
        self.isDealer = isDealer

    def getScore(self, countAll=False):
        self.sortHand()
        score = 0
        for card in self.cards:
            if(card.rank.isnumeric()):
                score += int(card.rank)
            elif(card.rank != 'A'):
                score += 10
            else:
                if(score > 10):
                    score += 1
                else:
                    score += 11
            if(self.isDealer and not countAll):
                return score
        return score

    def printHand(self, showAll=False):
        if(self.isDealer):
            print("Dealer's hand: " + str(self.getScore(countAll=showAll)))
            if(showAll):
                for card in self.cards:
                    card.graphicPrint()
            else:
                self.cards[0].graphicPrint()
        else:
            print("Your hand: " + str(self.getScore()))
            for card in self.cards:
                card.graphicPrint()

    def sortHand(self):
        self.cards.sort(key=Card.getRank)
        if(self.checkForAce()):
            for i in range(4):
                self.cards.append(self.cards.pop(self.findFirstAce()))

    def checkForAce(self):
        for card in self.cards:
            if(card.rank == 'A'):
                return True
        return False

    def findFirstAce(self):
        for i in range(len(self.cards)):
            if(self.cards[i].rank == 'A'):
                return i

class BlackJack:
    def __init__(self):
        self.playerHand = Hand(isDealer=False)
        self.dealerHand = Hand(isDealer=True)
        self.deck = Deck()
    
    def startGame(self):
        self.initialDeal()
        self.showHands()
        self.playerTurn()
        self.dealerTurn()
        self.checkFinalScore()

    def initialDeal(self):
        self.playerHand.cards += self.deck.draw(2)
        self.dealerHand.cards += self.deck.draw(2)

    def showHands(self, showAll=False):
        print()
        self.playerHand.printHand()
        self.dealerHand.printHand(showAll)

    def deal(self, dealer=False):
        if(dealer):
            self.dealerHand.cards += self.deck.draw()
        else:
            self.playerHand.cards += self.deck.draw()

    def playerTurn(self):
        val = input("Type h to hit, or type s to stand: ")
        while(val not in ['s', 'S', 'h', 'H']):
            val = input("Invalid Input. Type h to hit, or type s to stand: ")
        if(val in ['h', 'H']):
            self.playerHand.cards += self.deck.draw(1)
            self.showHands()
            self.checkPlayerScore()
            self.playerTurn()
        else:
            return

    def dealerTurn(self):
        score = self.dealerHand.getScore(countAll=True)
        if(score > 21):
            self.playerWon()
        elif(score < 17):
            self.deal(dealer=True)
            self.dealerTurn()
        else:
            return

    def playerLost(self):
        self.showHands(showAll=True)
        print("You Lose!!")
        sys.exit(0)

    def playerWon(self):
        self.showHands(showAll=True)
        print("You Won!!")
        sys.exit(0)

    def playerTied(self):
        self.showHands(showAll=True)
        print("You Tied!!")
        sys.exit(0)

    def checkPlayerScore(self):
        score = self.playerHand.getScore()
        if(score > 21):
            self.playerLost()
        elif(score == 21):
            self.playerWon()

    def checkFinalScore(self):
        playerScore = self.playerHand.getScore()
        dealerScore = self.dealerHand.getScore(countAll=True)
        if(playerScore > dealerScore):
            self.playerWon()
        elif(playerScore == dealerScore):
            self.playerTied()
        else:
            self.playerLost()
        

BlackJack().startGame()
