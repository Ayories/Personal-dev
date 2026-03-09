import random
from gameboardfixed import GameBoardFixed
class ComputerPlayer:
    def __init__(self, letter, board):
        self.__symbol = letter
        self.__gboard = board  # store a reference to the board 
        
    def get_player_symbol(self):
        return self.__symbol
		
    def play(self):
		# play method defines mechanism for playing. It starts by asking the current
		# player about the position at which the the player wishes to place her/his mark on the board.
        print("Player %s turn" %self.get_player_symbol()) 
        r = random.randint(0, 2)
        c = random.randint(0, 2)
        while (r < 0 or r > 2 or  c < 0 or c > 2 or False == (self.__gboard.is_space_free(r,c))):
            print("\r", "Invalid move: Try Again")
            r = random.randint(0, 2)
            c = random.randint(0, 2)

      """
        r = random.randint(0, 2)
        c = random.randint(0, 2)
        while (r < 0 or r > 2 or False == (self.__gboard.is_space_free(r,c))):
            print("\r", "Invalid move: Try Again")
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            for r in range(3):
                for c in range(3):
                    if check_vt

      """
    self.__gboard.make_move(r, c, self.get_player_symbol()) 
