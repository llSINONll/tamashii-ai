'''
A mini console game where the player tries to match hidden pairs on a 4x4 board.

✅ Features:
Randomly shuffled hidden card grid

Player selects two cards per turn

If they match → marked as found

If not → hidden again

Win once all pairs are matched
'''

import random
import os
import time

# Create a 4x4 board with 8 pairs of letters
letters = list("AABBCCDDEEFFGGHH")
random.shuffle(letters)
board = [letters[i:i+4] for i in range(0, 16, 4)]
revealed = [[False]*4 for _ in range(4)]

def print_board():
    print("    0   1   2   3")
    print("  -----------------")
    for i, row in enumerate(board):
        row_display = f"{i} | "
        for j in range(4):
            if revealed[i][j]:
                row_display += f"{board[i][j]} | "
            else:
                row_display += "  * | "
        print(row_display)
        print("  -----------------")

def get_input():
    while True:
        try:
            x, y = map(int, input("Enter row and column (e.g. 1 3): ").split())
            if 0 <= x < 4 and 0 <= y < 4 and not revealed[x][y]:
                return x, y
            else:
                print("Invalid or already revealed. Try again.")
        except:
            print("Invalid input. Try again.")

def game_loop():
    pairs_found = 0
    total_pairs = 8

    while pairs_found < total_pairs:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board()

        print("Pick first card:")
        x1, y1 = get_input()
        revealed[x1][y1] = True
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board()

        print("Pick second card:")
        x2, y2 = get_input()
        revealed[x2][y2] = True
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board()

        if board[x1][y1] == board[x2][y2]:
            print("✅ It's a match!")
            pairs_found += 1
        else:
            print("❌ Not a match...")
            time.sleep(1.5)
            revealed[x1][y1] = False
            revealed[x2][y2] = False

    print("🎉 You found all pairs! Well done!")

if __name__ == "__main__":
    game_loop()
