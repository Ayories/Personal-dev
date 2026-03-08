class GameBoardFixed:
    def __init__(self, s):
        self.__space = ' '
        self.__size = s
        self.__board = []
        for i in range (self.__size):
            row = [self.__space] * self.__size
            self.__board.append(row)
    
    def make_move(self, row, col, element): 
        self.__board[row][col] = element
    
    def check_winner(self):
        # 1. Check all rows
        for row in self.__board:
            # If all cells in the row match the first cell (and aren't empty)
            if all(cell == row[0] and cell != self.__space for cell in row):
                return True
                
        # 2. Check all columns
        for col in range(self.__size):
            if all(self.__board[row][col] == self.__board[0][col] and self.__board[row][col] != self.__space for row in range(self.__size)):
                return True
                
        # 3. Check the top-left to bottom-right diagonal
        if all(self.__board[i][i] == self.__board[0][0] and self.__board[i][i] != self.__space for i in range(self.__size)):
            return True
            
        # 4. Check the top-right to bottom-left diagonal
        if all(self.__board[i][self.__size - 1 - i] == self.__board[0][self.__size - 1] and self.__board[i][self.__size - 1 - i] != self.__space for i in range(self.__size)):
            return True
            
        return False
        
    def is_board_full(self):
            for i in range (self.__size):
                for j in range (self.__size):
                    if (self.__board[i][j] == self.__space):
                        return False          
            return True 
     # TOD
     # : Return True if every space on the self.__board has been taken. Otherwise return False.
     
    def is_space_free (self, row, col):
        while (self.__board):
            for i in range (self.__size):
                for j in range (self.__size):
                    if (self.__board[row][col] == self.__space):
                        return True
                    elif (self.__board[row][col] is not None and self.__board[row][col] != self.__space):
                        return False
        # TOD: Return true if the passed move is free on the passed self.__board.
        pass

    def show_board_dynamic(self): 
        # Loop through each row based on the dynamic size of the board
        for i in range(self.__size):
            # 1. Join the elements of the row with vertical bars
            print(' ' + ' | '.join(self.__board[i]))
            
            # 2. Print a horizontal divider, but skip it after the very last row
            if i < self.__size - 1:
                # Multiply hyphens based on board size to make it scale automatically
                print('-' * (self.__size * 4 - 1)) 

    def show_board_fixed(self): 
        print(' ' + self.__board[0][0] + ' | ' + self.__board[0][1] + ' | ' 
        + self.__board[0][2]) 
        print(' ----------- ') 
        print(' ' + self.__board[1][0] + ' | ' + self.__board[1][1] + ' | ' 
        + self.__board[1][2]) 
        print(' ----------- ')
        print(' ' + self.__board[2][0] + ' | ' + self.__board[2][1] + ' | ' 
        + self.__board[2][2])

