import board

def main():
    pass
    #create board
    game_board = board.Board()
    game_board.draw_board()
    while (not game_board.check_for_end_of_game()):
        move = get_move()
        if not game_board.make_move(move):
            print "Could not make move, try again."
        game_board.draw_board()
        
def get_move():
    move = None
    while not isinstance(move, str): 
        move = raw_input("Write move, start-end (eq e2-e4): ")
    
    print "Got move", move
    return move

if __name__ == "__main__":
    main()