class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_win(self):
        # Verifică linii, coloane și diagonale pentru victorie
        lines = self.board + list(zip(*self.board)) + [[self.board[i][i] for i in range(3)], [self.board[i][2-i] for i in range(3)]]
        return any(all(cell == self.current_player for cell in line) for line in lines)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)