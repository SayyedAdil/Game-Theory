import random

players = int(input("Enter number of players: "))
if players<2:
    print("Enter at least 2 players!!!")
    players = int(input("Enter number of players: ")) 

rounds = int(input("Enter number of rounds: "))
if players - rounds !=1:
    print("Number of rounds should be 1 less than the number of players")

amt = int(input("Enter total amount: "))  

powerup = int(amt/10)
powerround = [] 
print("Players now select their power up round")
for i in range(players):
    print("Player",(i+1),"select your powerup round")
    powerround.append(int(input()))

powerplayers = []
print(powerround)    
playeramt = [amt] * players

playerwin  = [0] * players
bid = []
max = 0
for i in range(rounds):
    print("Round ",(i+1)," begins")
    print("")
    for j in range(players):
        print("Player ",(j+1)," enter your bid:-- ")
        bid.append(int(input()))
        playeramt[j] = playeramt[j] - bid[j]
        
    for k in range(len(powerround)):
        if i==k:
            powerplayers.append(k)

    maxbid = 0
    for k in range(len(powerplayers)):
        if bid[k]>maxbid:
            maxbid = k  
    bid[k] = bid[k] + powerup
    
    for i in range(len(bid)):
        if bid[i]>=max:
            max = bid[i]

    for k in range(players):
        if (bid[k]==max):
            playerwin[k] = playerwin[k] + 1
    bid = []
    max = 0      

winner = 0
flag = 0
flag1 = []
for i in range(len(playerwin)):
    if playerwin[i]>=flag:
        flag = playerwin[i]
        flag1.append(i)

'''if len(flag1)==1:
    print()'''

for j in range(len(flag1)):
    if(len(flag1)>1):
        print("Winners are players ",flag1[j]+1)
    else:
        print("Winner is player ",flag1[j]+1)    
