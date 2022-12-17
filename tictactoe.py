from random import shuffle
displaybox = [' ']*9
icon = ['X','O']
allow = True
print("welcome to TIC TAC TOE")
print("Name of the player 1")

p1 = str(input("Enter Your Beautiful Name (Player 1)"))
print("Well Done! {}".format(p1))
p2 = str(input("Enter your Awesome Name (Player 2)"))
print("WOW! Great {}".format(p2))
shuffle(icon)
print("{} you are assigned with {}".format(p1,icon[0]))
print("{} you are assigned with {} \n \n".format(p2,icon[1]))

print("The squares are represented by numbers as follow:")
print("  6   |   7   |   8  ")
print("  3   |   4   |   5  ")
print("  0   |   1   |   2  ")

def play(current_player):
    index = int(input("enter the number : "))

    if (displaybox[index]) == ' ':
        displaybox[index] = current_player
        print("{}   |   {}  |   {}".format(displaybox[6],displaybox[7],displaybox[8]))
        print("{}   |   {}  |   {}".format(displaybox[3],displaybox[4],displaybox[5]))
        print("{}   |   {}  |   {}".format(displaybox[0],displaybox[1],displaybox[2]))
        
    else :
        play(current_player)
        
def check():
        #row
        for i in range(0,9,3):
            if(displaybox[i] ==  displaybox [i+1] and displaybox[i+1] ==  displaybox[i+2]):
                winner = displaybox[i]
                if (winner != ' '):
                    if (winner == icon[0]):
                        print(p2 + "won the game")
                    else:
                        print(p1 + "won the game")
                    return True
                
        #column
        for i in range(0,3):
            if(displaybox[i] ==  displaybox [i+3] and displaybox[i+3] ==  displaybox[i+6]):
                winner = displaybox[i]
                if (winner != ' '):
                    if (winner == icon[0]):
                        print(p2 + "won the game")
                    else:
                        print(p1 + "won the game")
                    return True
                
            
                
        #diagonal
        if(displaybox[0] ==  displaybox [4] and displaybox[4] ==  displaybox[8]):
                winner = displaybox[0]
                if (winner != ' '):
                    if (winner == icon[0]):
                        print(p2 + "won the game")
                    else:
                        print(p1 + "won the game")
                    return True
                
        
        if(displaybox[2] ==  displaybox [4] and displaybox[4] ==  displaybox[6]):
                winner = displaybox[2]
                if (winner != ' '):
                    if (winner == icon[0]):
                        print(p2 + "won the game")
                    else:
                        print(p1 + "won the game")
                    return True
                
        

for i in range(9):
    current_player = icon[0]
    icon.reverse()
    play(current_player)
    lauda = check()
    if lauda :
        break
    
    
