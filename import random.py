import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

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
    
    print("🎮 Welcome to Rock-Paper-Scissors!")
    print("Enter 'rock', 'paper', or 'scissors'. Type 'quit' to stop playing.\n")
    
    while True:
        user_choice = input("👉 Your choice: ").lower()
        
        if user_choice == "quit":
            print("\nThanks for playing! Final Score:")
            print(f"🧑 You: {user_score} | 🤖 Computer: {computer_score}")
            break
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("⚠️ Invalid choice. Please enter rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"🤖 Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "tie":
            print("😐 It's a tie!\n")
        elif winner == "user":
            user_score += 1
            print("🎉 You win this round!\n")
        else:
            computer_score += 1
            print("💻 Computer wins this round!\n")
        
        print(f"Score: 🧑 You {user_score} - {computer_score} 🤖\n")

# Run the game
play_game()