import random


def printDices(num1,num2,num3):
    
    print(" ----------- ----------- -----------")
    #top part of the first dice
    if(num1 == 6 or num1 == 4 or num1 == 5):
        print(" |  o   o  |", end='')
    elif (num1 == 2 or num1 == 3):
        print(" |    o    |", end='')
    elif(num1 == 1):
        print(" |         |", end='')
        

    #top part of the second dice
    if(num2 == 6 or num2 == 4 or num2 == 5):
        print(" |  o   o  |", end='')
    elif (num2 == 2 or num2 == 3):
        print(" |    o    |", end='')
    elif(num2 == 1):
        print(" |         |", end='')

    #top part of the Thrid dice
    if(num3 == 6 or num3 == 4 or num3 == 5):
        print(" |  o   o  |", end='')
    elif (num3 == 2 or num3 == 3):
        print(" |    o    |", end='')
    elif(num3 == 1):
        print(" |         |", end='')

    print()         
    #Second layer   
    if(num1 == 6):  
        print(" |  o   o  |", end='')
    elif(num1 == 5 or num1 == 3 or num1 == 1):
        print(" |    o    |", end='')
    elif(num1 == 4 or num1 == 2):
        print(" |         |", end='')
    #middle
    if(num2 == 6):
        print(" |  o   o  |", end='')
    elif(num2 == 5 or num2 == 3 or num2 == 1):
        print(" |    o    |", end='')
    elif(num2 == 4 or num2 == 2):
        print(" |         |", end='')
    #right
    if(num3 == 6):
        print(" |  o   o  |", end='')
    elif(num3 == 5 or num3 == 3 or num3 == 1):
        print(" |    o    |", end='')
    elif(num3 == 4 or num3 == 2):
        print(" |         |", end='')
        
    print()
    #Thrid Layer
    if(num1 == 6 or num1 == 4 or num1 == 5):
        print(" |  o   o  |", end='')
    elif (num1 == 2 or num1 == 3):
        print(" |    o    |", end='')
    elif(num1 == 1):
        print(" |         |", end='')
    #middle
    if(num2 == 6 or num2 == 4 or num2 == 5):
        print(" |  o   o  |", end='')
    elif (num2 == 2 or num2 == 3):
        print(" |    o    |", end='')
    elif(num2 == 1):
        print(" |         |", end='')
    #right
    if(num3 == 6 or num3 == 4 or num3 == 5):
        print(" |  o   o  |")
    elif (num3 == 2 or num3 == 3):
        print(" |    o    |")
    elif(num3 == 1):
        print(" |         |")
       
    print(" ----------- ----------- -----------")

   

    
    
    
    
    


   



    
    
greet = input("Welcome to the Roll 3 Dice Game!!!\nRoll the Dice? (Y/N) ")
counter = 0
win = 0
lose = 0
while greet == 'Y' or greet == 'y':
    f = random.randrange(1,7)
    s = random.randrange(1,7)
    t = random.randrange(1,7)
    totalMe = f + s + t
    print("Let's roll your dice!!!")
    printDices(f,s,t)
    
  
    print("It's AI's turn to roll the dice!!!")
    ai1 = random.randrange(1,7)
    ai2 = random.randrange(1,7)
    ai3 = random.randrange(1,7)
    totalAi = ai1 + ai2 + ai3
    printDices(ai1,ai2,ai3)

    print(f"YOU ({totalMe}) {f},{s},{t} - {ai1},{ai2},{ai3} ({totalAi}) AI")
    
    counter+=1
    if totalMe > totalAi:
        win+=1
        print(f"You win!!!/nGRAND TOTAL AFTER THE RUN #{counter}: YOU {win} - {lose} AI (Win Ratio: {win/counter:.3f} )")
    elif totalMe < totalAi:
        lose += 1
        print(f"AI wins.../nGRAND TOTAL AFTER THE RUN #{counter}: YOU {win} - {lose} AI (Win Ratio: {win/counter:.3f} )")
    else:
        print(f"Draw?!!/nGRAND TOTAL AFTER THE RUN #{counter}: YOU {win} - {lose} AI (Win Ratio: {win/counter:.3f} )")


    greet = input("Roll the Dice? (Y/N) ")
    



print("See ya!!!")        