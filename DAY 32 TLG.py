# cook your dish here
# Reading input
N = int(input())  # Number of rounds
player1_score = 0  # Cumulative score of player 1
player2_score = 0  # Cumulative score of player 2

max_lead = 0  # To store the maximum lead
winner = 0  # To store the winner (1 or 2)

# Processing each round
for _ in range(N):
    S, T = map(int, input().split())  # Scores for the current round
    player1_score += S
    player2_score += T

    # Calculate the current lead and the leader
    current_lead = abs(player1_score - player2_score)
    
    if player1_score > player2_score:
        current_winner = 1
    else:
        current_winner = 2

    # Update max_lead and winner if current lead is greater
    if current_lead > max_lead:
        max_lead = current_lead
        winner = current_winner

# Output the winner and the maximum lead
print(winner, max_lead)
