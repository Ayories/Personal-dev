from player import Player
import random
class ComputerPlayer(Player):
    def __init__(self, letter, board):
        super().__init__(letter, board)
        
    def play(self):
		# play method defines mechanism for playing. It starts by asking the current
		# player about the position at which the the player wishes to place her/his mark on the board.
        print("Player %s turn" %self.get_player_symbol()) 
        r = random.randint(0, 2)
        c = random.randint(0, 2)
        while (r < 0 or r > 2 or  c < 0 or c > 2 or False == (self._gboard.is_space_free(r,c))):
            #print("\r", "Invalid move: Try Again")
            r = random.randint(0, 2)
            c = random.randint(0, 2)
        self._gboard.make_move(r, c, self.get_player_symbol())
    """
        r = random.randint(0, 2)
        c = random.randint(0, 2)
        while (r < 0 or r > 2 or False == (self._gboard.is_space_free(r,c))):
            print("r", "Invalid move: Try Again")
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            for r in range(3):
                for c in range(3):
                    if check_vt

    """
    