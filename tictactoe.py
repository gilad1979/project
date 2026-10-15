import sys

def print_board(board):
    """Print the Tic Tac Toe board."""
    for i in range(3):
        row = ' | '.join(board[i])
        print(row)
        if i < 2:
            print('-' * 5)

def check_winner(board, player):
    """Check if the player has won"""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    """Check if the board is full"""
    for row in board:
        if any(cell == ' ' for cell in row):
            return False
    return True

def get_move(player, board):
    """Get a valid move from the user."""
    while True:
        try:
            move = input(f"שחקן {player}, הכנס את המיקום שלך (שורה ועמודה, לדוג' 1 1): ")
            row, col = map(int, move.strip().split())
            row -= 1
            col -= 1
            if row not in range(3) or col not in range(3):
                print("מיקום מחוץ לטווח, נסה שוב.")
                continue
            if board[row][col] != ' ':
                print("התא הזה כבר תפוס, נסה שוב.")
                continue
            return row, col
        except (ValueError, IndexError):
            print("קלט שגוי, נסה שוב.")

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    print("ברוכים הבאים לאיקס עיגול!")
    print_board(board)

    while True:
        player = players[turn % 2]
        row, col = get_move(player, board)
        board[row][col] = player
        print_board(board)
        
        if check_winner(board, player):
            print(f"ברכות! השחקן {player} ניצח!")
            break
        elif is_draw(board):
            print("תיקו!")
            break
        else:
            turn += 1

if __name__ == "__main__":
    main()