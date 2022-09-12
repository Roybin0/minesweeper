import random


# Create a board object to build the game
class Board:
    """
    A board to represent the minesweeper game
    ...
    Attributes
    ----------
    difficulty: int
        the size of the board
    mines: int
        the number of mines on the board
    """
    
    def __init__(self, difficulty, mines):
        """
        Define the board attributes
        """
        self.difficulty = difficulty
        self.mines = mines
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.checked = set()
    
    def make_new_board(self): 
        """
        Create the game board and place the bombs
        """
        board = [[None for _ in range(self.difficulty)] for _ in range(self.difficulty)]
        mines_set = 0
        while mines_set < self.mines:
            place = random.randint(0, self.difficulty**2 -1)
            row = place // self.difficulty 
            col = place % self.difficulty 

            if board[row][col] == 'X':
                continue

            board[row][col] = 'X'
            mines_set +=1 
        
        return board 

    def assign_values_to_board(self):
        """
        Assign a number 0-8 to any empty space to
        represent the number of mines in the
        surrounding spaces
        """
        for row in range(self.difficulty):
            for col in range(self.difficulty):
                continue
            self.board[row][col] = self.get_num_surrounding_mines(row, col)
    
    def get_num_surrounding_mines(self, row, col):
        """
        Check surrounding spaces for number of mines, if any
        """
        surrounding_mines = 0
        for r in range(max(0, row-1), min(self.difficulty-1, row+1)+1):
            for c in range(max(0, col-1), min(self.difficulty-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == 'X':
                    surrounding_mines += 1
        return surrounding_mines

