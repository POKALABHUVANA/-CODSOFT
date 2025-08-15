import random
def get_user_choice():
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        while choice not in ['rock', 'paper', 'scissors']:
            choice=input("invalid input.please choose rock,paper,or scissors:")
            return choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"
def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}")
        result = determine_winner(user, computer)
        if result == "tie":
              print("It's a tie!")
        elif result == "user":
              print("You won this round!")
              user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        print(f"\nscore -> You: {user_score},computer: {computer_score}")
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
           print("\nThanks for playing!")
           break
play_game()
    
