#blackjack 
import random 
cards = ["Ace", "King" , "Queen" , "Jack" ,"2" , "3" , "4" ,"5" , "6" , "7" , "8" , "9" , "10"]
def drawcard(cards):
    drawcard = random.choice(cards)
    if drawcard == "Ace":
        print("You have drawn an ace would you like to use it as 1 or 11?")
        choice = input()
        if choice == "1":
            return "1"
        else:
            return "11"
    elif drawcard == "King" or drawcard == "Queen" or drawcard == "Jack":
        return "10"
    elif drawcard == "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10":
        return drawcard
print("Welcome to BlackJack\n")
print("The aim of this game is to get the closest in card value to 21 without going over\n")
print("You can either draw or stick(take another card or stick with yout current ones.")
card1 = str(drawcard(cards))
print("Your first card is : " , card1)
def again1():
    global i
    i = 2
    again = input("Would you like to draw another Card? Y/N")
    card2 = str(drawcard(cards))
    if again == "y" or "Y":
        print("Card", i , " = " , card2)
        if int(card1) + int(card2) >= 21:
            print("BUST. You're Out.")
            exit()
        else:
            print("Value of card 1 = " , card1 , "Value of card 2 = " , card2)
            print("Total = " , int(card1)+int(card2))
            i+=1
            again2()
    else:
        print("Your card add to" , int(card1) + int(card2))
def again2():
    again = input("Would you like to draw another Card? Y/N")
    card3 = str(drawcard(cards))
    if again == "y" or "Y":
        print("Card", i , " = " , card3)
        if int(card1) + int(card2) + int(card3) >= 21:
            print("BUST. You're Out.")
            exit()
        else:
            print("Value of card 1 = " , card1 , "Value of card 2 = " , card2 , "Value of card 3 =" , card3)
            print("Total = " , int(card1)+int(card2)+int(card3))
            i+=1
    else:
        print("Your card add to" , int(card1) + int(card2))
def again3():
    again = input("Would you like to draw another Card? Y/N")
    card3 = str(drawcard(cards))
    if again == "y" or "Y":
        print("Card", i , " = " , card3)
        if int(card1) + int(card2) + int(card3) > 21:
            print("BUST. You're Out.")
            exit()
        else:
            print("Value of card 1 = " , card1 , "Value of card 2 = " , card2)
            print("Total = " , int(card1)+int(card2+int(card3)))
            again4()
    else:
        print("Your card add to" , int(card1) + int(card2))
again1()


