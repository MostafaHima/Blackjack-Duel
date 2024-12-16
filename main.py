import pyfiglet
import random

# Print ASCII art at the start of the game
asci_art = pyfiglet.figlet_format("Black Jak")
print(asci_art)

def play():
    """
    Main game logic for the Blackjack game.
    """

    def cards():
        """
        Draws a random card from a predefined deck.
        """
        card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
        random_card = random.choice(card)
        return random_card

    def calculate_score(cards):
        """
        Calculates the total score of a player's cards.
        - Returns 0 if the score is exactly 21 (Blackjack).
        - Adjusts for aces (11) to avoid busting.
        """
        if sum(cards) == 21:
            return 0
        if sum(cards) > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_score, delar_score):
        """
        Compares the scores of the user and the dealer and determines the result.
        Returns a string indicating the outcome.
        """
        if user_score == delar_score:
            return "Draw"
        elif delar_score == 0:
            return "You Lose (Dealer has Blackjack)"
        elif user_score == 0:
            return "You Win (Blackjack!)"
        elif user_score > 21:
            return "You Lose (Busted)"
        elif delar_score > 21:
            return "You Win (Dealer Busted)"
        elif user_score > delar_score:
            return "You Win"
        else:
            return "You Lose"

    # Initialize user and dealer hands
    user = []
    delar = []
    is_game_over = False

    # Each player starts with two cards
    for _ in range(2):
        user.append(cards())
        delar.append(cards())

    # Calculate initial scores
    user_score = calculate_score(user)
    delar_score = calculate_score(delar)

    # Display the dealer's first card
    print(f"Dealer's first card: {delar[0]}")

    # User's turn to hit or stand
    while not is_game_over:
        print(f"Your cards: {user}, current score: {user_score}")

        # Check for Blackjack or bust
        if user_score == 0 or delar_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to hit? (y/n): ").strip().lower()
            if user_should_deal == "y":
                user.append(cards())
                user_score = calculate_score(user)
            else:
                is_game_over = True

    # Dealer's turn to draw cards until reaching 17 or higher
    while delar_score != 0 and delar_score < 17:
        delar.append(cards())
        delar_score = calculate_score(delar)

    # Show final results
    print(f"\nDealer's final hand: {delar}, final score: {delar_score}")
    print(f"Your final hand: {user}, final score: {user_score}\n")

    # Print the result of the game
    print(compare(user_score, delar_score))

def play_again():
    """
    Prompts the user to play again or exit the game.
    """
    play_again = False
    while not play_again:
        user_choice = input("Do you want to start play? (y/n): ").strip().lower()
        if user_choice == "y":
            play()
        else:
            play_again = True
            print("Thank you for playing my game!")


play_again()

