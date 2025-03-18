import random

score = 0
rounds = 0
wins = 0
draws = 0
losses = 0

def roll_die():
    return random.randint(1, 6)

def roll_multiple_dice(num_dice):
    return sum(roll_die() for _ in range(num_dice))

def get_round_result(player_total, computer_total):
    if player_total > computer_total:
        return "Win"
    elif player_total < computer_total:
        return "Loss"
    return "Draw"

def shop(score):
    print("1. Extra die (5 points)")
    print("2. Double points next win (10 points)")
    print("3. Exit shop")
    
    choice = input("Choose an option: ")
    
    if choice == "1" and score >= 5:
        return score - 5, 1, False
    elif choice == "2" and score >= 10:
        return score - 10, 0, True
    elif choice == "3":
        return score, 0, False
    print("Invalid choice or not enough points.")
    return score, 0, False

def display_statistics():
    print("Game Over!")
    print("Rounds:", rounds)
    print("Wins:", wins)
    print("Draws:", draws)
    print("Losses:", losses)
    print("Final Score:", score)


while True:
    extra_dice, double_points = 0, False
    
    if input("Do you want to visit the shop? (yes/no): ") == "yes":
        score, extra_dice, double_points = shop(score)
    
    player_total = roll_multiple_dice(2 + extra_dice)
    computer_total = roll_multiple_dice(2)
    result = get_round_result(player_total, computer_total)
    
    rounds += 1
    if result == "Win":
        score += 10 if double_points else 5
        wins += 1
    elif result == "Draw":
        score += 2
        draws += 1
    else:
        losses += 1
    
    print(f"Round {rounds}: You rolled {player_total}, Computer rolled {computer_total}")
    print(f"Result: {result}\nCurrent Score: {score}")
    
    if input("Do you want to play another round? (yes/no): ")  != "yes":
        break

display_statistics()