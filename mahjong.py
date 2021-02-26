import datetime as dt
import os

print("Mahjong Calculator \ny: start a new game \nn: quit\n")
game = input("Option: ")
#quits the game if n is chosen and starts the game if y is chosen
if game == 'n':
    exit()
elif game == 'y':
    print()
    stime = dt.datetime.now()
    #enter the name of the players and ask for the price of one tai
    players = []
    playertaicounts = [0,0,0,0]
    number1 = 1
    while number1 <= 4:
        print("Enter the name of Player " + str(number1))
        player = input("Player " + str(number1) + ": ")
        players.append(player)
        number1 += 1
    # print(players)
    taino = float(input("\nHow much is one tai?: "))
    
    roundno = 1 #this variable "roundno" is just a round counter and doesnt do much else, however it does help loop the code in the while statement below
    while roundno <= 10000:
        #asks for the winner and losers of the round
        while True:
            print("\n\nRound: " + str(roundno))
            print("Who won?")
            option1 = 1
            for player in players:
                print(str(option1) + ": " + player)
                option1 += 1
            winner = input("Winner: ")

            print("\nWho threw the losing tile?")
            option2 = 1
            for player in players:
                print(str(option2) + ": " + player)
                option2 += 1
            print("5: zimo")
            loser = input("Thrower: ")

            #loops as winner cannot be the same as the loser so the code asks again
            if winner == loser:
                print("\nThe winner and losers are not allowed to be the same people! Please try again.")
            elif winner != loser:
                break

        print("\nHow many tai were won?")
        points = int(input("tai: "))

        if loser == '1':
            playertaicounts[0] -= (points * 2)
            if winner == '2':
                playertaicounts[1] += (points * 4)
                playertaicounts[2] -= points
                playertaicounts[3] -= points
            elif winner == '3':
                playertaicounts[1] -= points
                playertaicounts[2] += (points * 4)
                playertaicounts[3] -= points
            elif winner == '4':
                playertaicounts[1] -= points
                playertaicounts[2] -= points
                playertaicounts[3] += (points * 4)
        elif loser == '2':
            playertaicounts[1] -= (points * 2)
            if winner == '1':
                playertaicounts[0] += (points * 4)
                playertaicounts[2] -= points
                playertaicounts[3] -= points
            elif winner == '3':
                playertaicounts[0] -= points
                playertaicounts[2] += (points * 4)
                playertaicounts[3] -= points
            elif winner == '4':
                playertaicounts[0] -= points
                playertaicounts[2] -= points
                playertaicounts[3] += (points * 4)
        elif loser == '3':
            playertaicounts[2] -= (points * 2)
            if winner == '1':
                playertaicounts[0] += (points * 4)
                playertaicounts[1] -= points
                playertaicounts[3] -= points
            elif winner == '2':
                playertaicounts[0] -= points
                playertaicounts[1] += (points * 4)
                playertaicounts[3] -= points
            elif winner == '4':
                playertaicounts[0] -= points
                playertaicounts[1] -= points
                playertaicounts[3] += (points * 4)
        elif loser == '4':
            playertaicounts[3] -= (points * 2)
            if winner == '1':
                playertaicounts[0] += (points * 4)
                playertaicounts[1] -= points
                playertaicounts[2] -= points
            elif winner == '2':
                playertaicounts[0] -= points
                playertaicounts[1] += (points * 4)
                playertaicounts[2] -= points
            elif winner == '3':
                playertaicounts[0] -= points
                playertaicounts[1] -= points
                playertaicounts[2] += (points * 4)
        elif loser == '5':
            if winner == '1':
                playertaicounts[0] += (points * 6)
                playertaicounts[1] -= (points * 2)
                playertaicounts[2] -= (points * 2)
                playertaicounts[3] -= (points * 2)
            if winner == '2':
                playertaicounts[0] -= (points * 2)
                playertaicounts[1] += (points * 6)
                playertaicounts[2] -= (points * 2)
                playertaicounts[3] -= (points * 2)
            if winner == '3':
                playertaicounts[0] -= (points * 2)
                playertaicounts[1] -= (points * 2)
                playertaicounts[2] += (points * 6)
                playertaicounts[3] -= (points * 2)
            if winner == '4':
                playertaicounts[0] -= (points * 2)
                playertaicounts[1] -= (points * 2)
                playertaicounts[2] -= (points * 2)
                playertaicounts[3] += (points * 6)
        # print(playertaicounts)

        o = 1
        while o <= 4:
            print("\nWhich player had kang(s), or flower pair(s)?")
            number2 = 1
            while number2 <= 4:
                for player in players:
                    print(str(number2) + ": " + player)
                    number2 += 1
            print("5: None \n6: No more")
            kfp = input("Option: ")
            if kfp == '5' or kfp == '6':
                break
            else:
                kfpno = int(input("\nHow many did they have?: "))
                if kfp == '1':
                    playertaicounts[0] += (kfpno * 6)
                    playertaicounts[1] -= (kfpno * 2)
                    playertaicounts[2] -= (kfpno * 2)
                    playertaicounts[3] -= (kfpno * 2)
                elif kfp == '2':
                    playertaicounts[0] -= (kfpno * 2)
                    playertaicounts[1] += (kfpno * 6)
                    playertaicounts[2] -= (kfpno * 2)
                    playertaicounts[3] -= (kfpno * 2)
                elif kfp == '3':
                    playertaicounts[0] -= (kfpno * 2)
                    playertaicounts[1] -= (kfpno * 2)
                    playertaicounts[2] += (kfpno * 6)
                    playertaicounts[3] -= (kfpno * 2)
                elif kfp == '4':
                    playertaicounts[0] -= (kfpno * 2)
                    playertaicounts[1] -= (kfpno * 2)
                    playertaicounts[2] -= (kfpno * 2)
                    playertaicounts[3] += (kfpno * 6)

        print("\nEnd Game? \ny: Yes \nn: No")
        end = input("Option: ")
        if end == 'y':
            break
        elif end == 'n':
            roundno += 1
    
print("\nEach player has gained/lost this amount of money: ")
number3 = 1
while number3 <= 4:
    for player in players:
        print(player + ": $" + str("{:.2f}".format(playertaicounts[number3-1] * taino)) + ".")
        number3 += 1

now = dt.datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
lastprompt = "Game finished at: " + str(dt_string) + "! This mahjong session was completed in " + str(roundno) + " round, and it took " + str(dt.datetime.now() - stime) + " (including breaks and other activities in between)."  
print(lastprompt)
mof = open("mahjong.txt","a")
mof.write(str(playertaicounts) + " " + str(players) + " " + str(dt_string) + "\n")
mof.close()
os.system("pause")