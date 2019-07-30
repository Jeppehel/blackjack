import random
from createDecks import createDeckss

#the betting functions and variables are defined in this class
class Bets:
    
    def __init__(self):
        self.betDollars = 0
        self.totalDollars = 1000
    
    def win(self):
        self.totalDollars += self.betDollars

    def lose(self):
        self.totalDollars -= self.betDollars
#This method makes sure that the hands are reset every new game
def resetHands():
    del dealerHand[:]
    del playerHand[:]

player = Bets()
#instance of the deckcreation functionality
createNewDecks = createDeckss()
#Player The care taker of amounts of  the bets that is to be made in each round of blackjack
def betInGame(player):

    while True:
        try:
            print("To play a game of BlackJack you must bet some money\n")
            print("Your balance is: ", player.totalDollars, "Dollars\n")
            player.betDollars = int(input("Please enter an amount of minimum 1 Dollar : "))  
            print("\n")
        except ValueError:
            print("You should only enter numbers")   
        else:
            if player.betDollars > player.totalDollars:
                print("You should have brought more dollars to the table, please try with an amounts equal to what you have: ", player.totalDollars)
            elif player.betDollars <= 0:
                print("You should enter a positive amount")        
            else:
                break    

gameOnline = True             

#The main loop for the blackjack game itself
while gameOnline == True:

    print("\nWelcome to BlackJack")

    chooseCharacter = str(input("Do you want to play as the Dealer (Enter d) or Player (Enter p) : "))
    print("\n")

    #Dealer cards
    dealerHand = []
    #Player cards
    playerHand = []

    if chooseCharacter == "p":
        betInGame(player)
        randomCard = random.randint(2,11)
        print("=========GAME ON=========\n")
        #here the create deck method is being called, and below it the decks are sat to be equal to them
        createNewDecks.createDealerHand()
        createNewDecks.createPlayerHand()

        dealerHand = createNewDecks.dealerHand
        playerHand = createNewDecks.playerHand

        while sum(playerHand) < 21:
            drawAnother = str(input("Hit (enter h) or Stay (enter s)"))
            if drawAnother == "h":
                playerHand.append(random.randint(1,10)) 
                print("You drew a ", playerHand[-1])
                print("The sum of your hand is : " + str(sum(playerHand)) + " with ", playerHand)
            elif sum(dealerHand) == 21:
                print("The sum of the dealers hand is : " + str(sum(dealerHand)) + " with ", dealerHand)
                print("The sum of your hand is : " + str(sum(playerHand)) + " with ", playerHand) 
                print("The Dealer Wins with blackjack!")   
                Bets.lose(player)
                resetHands()
                break 
            else:   
                if sum(dealerHand) > sum(playerHand):
                    print("The sum of the dealers hand is : " + str(sum(dealerHand)) + " with ", dealerHand)
                    print("The sum of your hand is : " + str(sum(playerHand)) + " with ", playerHand)
                    print("The Dealer wins!")
                    Bets.lose(player)
                    resetHands()
                    break

                else:
                    while sum(dealerHand) <= 17:
                        dealerHand.append(random.randint(1, 11))
                        if (sum(dealerHand) > sum(playerHand) and sum(dealerHand) < 21):  
                            print("The sum of the dealers hand is : " + str(sum(dealerHand)) + " with ", dealerHand)
                            print("The sum of your hand is : " + str(sum(playerHand)) + " with ", playerHand)
                            print("The Dealer wins!")
                            Bets.lose(player)
                            resetHands()
                            break
                        
                        elif sum(dealerHand) == sum(playerHand):   
                            print("The sum of the dealers hand is : " + str(sum(dealerHand)) + " with ", dealerHand)
                            print("The sum of your hand is : "+ str(sum(playerHand)) + " with ", playerHand)
                            print("Both the dealer and the player wins!")
                            Bets.win(player)
                            resetHands()
                            break
                        elif sum(playerHand) > sum(dealerHand) and sum(dealerHand) >= 17:
                            print("The sum of the dealers hand is : " + str(sum(dealerHand)) + " with ", dealerHand)
                            print("The sum of your hand is : " + str(sum(playerHand)) + " with ", playerHand)
                            print("You Win!")
                            Bets.win(player)
                            resetHands() 
                            break 
                        elif sum(dealerHand) == 21:
                            print("The sum of the dealers hand is : " + str(sum(dealerHand)) + " with ", dealerHand)
                            print("The sum of your hand is : " + str(sum(playerHand)) + " with ", playerHand) 
                            print("The Dealer Wins with blackjack!")   
                            Bets.lose(player)
                            resetHands()
                            break
                        elif sum(dealerHand) > 21:
                            print("The sum of the dealers hand is : " + str(sum(dealerHand)) + " with ", dealerHand)
                            print("The Dealer busted!")
                            print("The sum of your hand is : " + str(sum(playerHand)) + " with ", playerHand)
                            print("You Win!")
                            Bets.win(player)
                            resetHands()
                            break   
                             
                    break

                    
        
        if sum(playerHand) > 21:
            print("You Busted! the dealer wins.")
            Bets.lose(player)
            resetHands()
        elif sum(playerHand) == 21:
            print("The sum of your hand is : " + str(sum(playerHand)) + " with ", playerHand)
            print("You got blackjack, you win")  
            Bets.win(player)
            resetHands()


        print("Thanks for playing, your balance is: ", player.totalDollars, "Dollars")


    if chooseCharacter == "d":
        randomCard = random.randint(2,11)
        # sum of player cards

        print("=========GAME ON=========\n")
        createNewDecks.createDealerHand()
        createNewDecks.createPlayerHand()

        dealerHand = createNewDecks.dealerHand
        playerHand = createNewDecks.playerHand
        
        while sum(playerHand) < 21:
            if sum(playerHand) < 15:
                print("Player : Hit")
                playerHand.append(randomCard)
                print("Player drew :",playerHand[-1])
                print("The sum of the players hand is : " + str(sum(playerHand)) + " with ", playerHand)

                if sum(playerHand) == 21:
                    print("The sum of your hand is : " + str(sum(dealerHand)) + " with ", dealerHand)
                    print("The sum of the players hand is : " + str(sum(playerHand)) + " with ", playerHand)
                    print("Player got BLACKJACK! Player Wins!")
                    resetHands()
                    break
                elif sum(playerHand) > 21:
                    print("The sum of your hand is : " + str(sum(dealerHand)) + " with ", dealerHand)
                    print("The sum of the players hand is : " + str(sum(playerHand)) + " with ", playerHand)
                    print("Player busted! You win")
                    resetHands()
                    break
            else:  
            
                if sum(dealerHand) > sum(playerHand):
                    print("The sum of your hand is : " + str(sum(dealerHand)) + " with ", dealerHand)
                    print("The sum of the players hand is : " + str(sum(playerHand)) + " with ", playerHand)
                    print("You, the dealer wins!")
                    resetHands()
                    break    
                else:
                    while sum(dealerHand) < 17:
                        print("Your hand is lower than 17, You must draw another card")
                        dealerHand.append(random.randint(1,10))
                        print("You just drew",dealerHand[-1])
                        print("The sum of your hand is : " + str(sum(dealerHand)) + " with ", dealerHand)

                        if(sum(dealerHand) > sum(playerHand) and sum(dealerHand) < 21):
                            print("The sum of your hand is : "  + str(sum(dealerHand)) + " with ", dealerHand)
                            print("The sum of the players hand is : "+ str(sum(playerHand)) + " with ", playerHand)
                            print("You, the dealer wins!")
                            resetHands()
                            break
                        elif sum(dealerHand) == sum(playerHand):
                            print("The sum of your hand is : "  + str(sum(dealerHand)) + " with ", dealerHand)
                            print("The sum of the players hand is : "+ str(sum(playerHand)) + " with ", playerHand)
                            print("Both the dealer and the player wins!")
                            resetHands()
                            break
                        elif sum(dealerHand) == 21:
                            print("The sum of your hand is : "  + str(sum(dealerHand)) + " with ", dealerHand)
                            print("The sum of the players hand is : "+ str(sum(playerHand)) + " with ", playerHand)
                            print("You, the dealer wins with blackjack!")
                            resetHands()
                            break
                        elif sum(dealerHand) > 21:
                            print("The sum of your hand is : " + str(sum(dealerHand)) + " with ", dealerHand)
                            print("You, the dealer have busted!")
                            print("The sum of the players hand is : "+ str(sum(playerHand)) + " with ", playerHand)
                            print("The player wins!")
                            resetHands()
                            break
                        
                    if sum(playerHand) > sum(dealerHand):
                        print("The sum of your hand is :  " + str(sum(dealerHand)) + " with ", dealerHand)
                        print("The sum of the players hand is : "+ str(sum(playerHand)) + " with ", playerHand)
                        print("The player wins!")
                        resetHands()

                    break

    if player.totalDollars == 0:
        print("No dollars left, Go home, Earn some more, Come back")
        break


    else:
        retry = str(input("Go for another round? (y for yes)"))
        if retry == "y":
            gameOnline = True

        else:
            print("Good luck with your life, Thanks for the lovely games")
            break


    
   