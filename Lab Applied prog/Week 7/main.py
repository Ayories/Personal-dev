from gameboardfixed import GameBoardFixed
from humanplayer import HumanPlayer
from computerplayer import ComputerPlayer

def main():
   while True: 
    gboard = GameBoardFixed(3)
	
    hp = HumanPlayer("X", gboard)    # create player 1 object
    cp = ComputerPlayer("O", gboard)    # create player 2 object
	
	# place players 1 and 2 in tuple for turn based game. 
    players_lst = (cp, hp)
	
    inPlay = True
	
    gboard.show_board_dynamic() # show empty grid at the beginning of the game
	
    while (inPlay == True):
		# This is to allow players to take turns. 
		# The game begins with the player at index zero in the tuple,
		# When the player completes its turn, the next player in the tuple will be asked to play. 
		# If there is no winner, this continue until reaching the end of the players list, and then we start again
		# from teh begging of the list.
		
        for p in players_lst:
            p.play()
            gboard.show_board_dynamic() # After each move, the board is shown on the screen
            
            winner = gboard.check_winner() # The board will check after each move, if any player has won the game
            if winner == True:
				# Show current player's symbol as Winner, 
				# and terminate the game
                print()
                print ("Player %s is the Winner!" % p.get_player_symbol())
                inPlay = False
                break  # end the game and announce the winner.
                
            full = gboard.is_board_full()
            if full == True:
                print()
                print("The board is full, no winner")
                choice = input("Do you want to continue playing? (Y/N): ").strip().upper()
                if choice == 'Y':
                    print("\nRestarting game...\n")
                    inPlay = False # Break inner loop to restart the outer loop
                    break 
                else:
                    print("\nThanks for playing!")
                    return # Exits the main() function entirely, ending the program
                    
        # If the game ended because someone won, we should also ask if they want to play again!
        if gboard.check_winner() == True:
            choice = input("Do you want to play again? (Y/N): ").strip().upper()
            if choice != 'Y':
                print("\nThanks for playing!")
                return
							
main()		
