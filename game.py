
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

# value = roll()
# print(value)

while True:
    players = input("Enter the number of players (2-4):")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid input, try again.")

# print(players)
max_score = 50
player_scores = [0 for _ in range(players)]
print(player_scores)

while max(player_scores)<= max_score:
    for player_indx in range(players):
        print("\nplayer", player_indx + 1 , "turn has just started !\n") 
        # print("Your ")
        print("Your total score is :",player_scores[player_indx])

        current_score= 0
        while True:

            should_roll = input("Would u like to roll (y)?")
            if should_roll.lower() != "y":
                break
            value= roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score= 0
                break

            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)
        player_scores[player_indx] += current_score
        
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number",winning_idx + 1," is the winner with the score of:" , max_score)















