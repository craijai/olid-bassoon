import random

def play_game():
    print("🎯 Welcome to the Number Guessing Game! 🎯")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    print("-" * 40)
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            # Get player's guess
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                print(f"The number was {secret_number}")
                break
            elif guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
                
            # Show remaining attempts
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"You have {remaining} attempts left.")
            
        except ValueError:
            print("❌ Please enter a valid number!")
            attempts -= 1  # Don't count invalid inputs
    
    else:
        print(f"\n💔 Game Over! You've used all {max_attempts} attempts.")
        print(f"The number was {secret_number}")
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again in ['y', 'yes']:
        print("\n" + "="*50)
        play_game()
    else:
        print("Thanks for playing! Goodbye! 👋")

def main():
    print("="*50)
    play_game()

if __name__ == "__main__":
    main()
