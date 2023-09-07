import random

# Initialize players' funds
player1_funds = 1000
player2_funds = 1000

# Initialize the amount of money in each box
box_money = list(range(1, 11))

# Initialize scores for each player
player1_score = 0
player2_score = 0

# Number of boxes to bid on
num_box = 10

# Simulate the bidding rounds
for round_num in range(1, num_box + 1):
    # Randomly generate bids for each player
    player1_bid = random.randint(0, player1_funds)
    player2_bid = random.randint(0, player2_funds)
    
    # Deduct the bids from players' funds
    player1_funds -= player1_bid
    player2_funds -= player2_bid
    
    # Determine the winner of the current box
    if player1_bid > player2_bid:
        player1_score += box_money[round_num - 1]
    elif player2_bid > player1_bid:
        player2_score += box_money[round_num - 1]
    else:
        # In case of a tie, no one wins the box
        pass

# Determine the game winner
if player1_score > player2_score:
    print("Player 1 wins with a score of", player1_score)
elif player2_score > player1_score:
    print("Player 2 wins with a score of", player2_score)
else:
    print("It's a tie!")

# Print the final funds of each player
print("Player 1's final funds:", player1_funds)
print("Player 2's final funds:", player2_funds)
