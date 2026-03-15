from gameboardfixed import GameBoardFixed
class Player:
    def __init__(self, letter, board):
        self._symbol = letter
        self._gboard = board  # store a reference to the board 
        
    def get_player_symbol(self):
        return self._symbol
		
    def play(self):
		# play method defines mechanism for playing. It starts by asking the current
		# player about the position at which the the player wishes to place her/his mark on the board.
        print("Player %s turn" %self.get_player_symbol()) 
        r = int(input("please enter row no : "))
        c = int(input("Please enter column no : "))
        while (r < 0 or r > 2 or False == (self._gboard.is_space_free(r,c))):
            print("\r", "Invalid move: Try Again")
            r = int(input("please enter row no : ")) 
            c = int(input("Please enter column no : "))
        self._gboard.make_move(r, c, self.get_player_symbol()) 

       ### print("Player %s turn" %self.get_player_symbol())
    ##    is_free = False
    ##    while (is_free == False):
          ##  r = int(input("please enter row no : "))
        ##    c = int(input("Please enter column no : "))
        ##    while (c < 0 or c > 2 or r < 0 or r > 2 or False == (self.__gboard.is_space_free(r,c))):
          ##      print("\r", "Invalid move: Try Again")
        ##        r = int(input("please enter row no : "))
      ##          c = int(input("Please enter column no : "))
    ##        else:
  ##              is_free = True
##                self.__gboard.make_move(r, c, self.get_player_symbol())
