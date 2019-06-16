import random
class createDeckss:

    dealerHand = []
    playerHand = []

    def createDealerHand(self):
        while True:
            
            randomCard = random.randint(2,11)
            if len(self.dealerHand) == 0:
                self.dealerHand.append(randomCard)                
            elif len(self.dealerHand) == 1:
                if self.dealerHand[0] == 11 and randomCard != 11:
                    self.dealerHand.append(randomCard)
                elif self.dealerHand[0] == 11 and randomCard == 11:
                    self.dealerHand.append(1)
                else:
                    self.dealerHand.append(randomCard)
            else:
                
                print("The dealer currently holds : X and {} \n".format(self.dealerHand[1]))
                break
                

    def createPlayerHand(self):
        while True:
        
            randomCard = random.randint(2,11)
            if len(self.playerHand) == 0:
                self.playerHand.append(randomCard)                
            elif len(self.playerHand) == 1:
                if self.playerHand[0] == 11 and randomCard != 11:
                    self.playerHand.append(randomCard)
                elif self.playerHand[0] == 11 and randomCard == 11:
                    self.playerHand.append(1)
                else:
                    self.playerHand.append(randomCard)
            else:
                
                print("The player currently holds :{} \n".format(self.playerHand))
                return self.playerHand
                