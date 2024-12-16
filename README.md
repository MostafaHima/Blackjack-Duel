# Blackjack Duel

## Description
Blackjack Duel is a Python-based card game where players compete against a dealer to reach 21 points or get closer without exceeding it. With strategic choices and dynamic gameplay, this game offers an engaging experience for card game enthusiasts.

## Features
- Player vs. Dealer gameplay.
- Randomized card draws.
- Automatic score calculation.

## How to Play
1. Run the Python script.
2. The dealer will reveal their first card.
3. You will receive two cards and decide whether to "Hit" (draw another card) or "Stand" (end your turn).
4. The dealer will play until their score is 17 or more.
5. The winner is decided based on the final scores:
   - 21 points = **Blackjack!**
   - Higher score than the dealer without exceeding 21 = **You Win!**
   - Exceeding 21 = **Bust! You Lose!**

## Requirements
- Python 3.x
- Random module (built-in)
- pyfiglet

### Example Gameplay

- **Dealer Score**: 7  
- **Your Cards**: [8, 9]  
- **Your Current Score**: 17

**Do You Want to Hit? (y/n)**: `n`

---

**Final Results**:  
- **Dealer Final Hand**: [7, 9]  
- **Dealer Final Score**: 16  

- **Your Final Hand**: [8, 9]  
- **Your Final Score**: 17  

---

**Result**: 🎉 **You Win!** 🎉

