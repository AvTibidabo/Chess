import pieces
from __builtin__ import False

class Board(object):
    
    def __init__(self):
        self.lines = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.rows = ["1", "2", "3", "4", "5", "6", "7", "8"]
        
        self.white_to_move = True
        
        self.board = []
        self.board.append(pieces.Rook("w", 0))
        self.board.append(pieces.Knight("w", 1))
        self.board.append(pieces.Bishop("w", 2))
        self.board.append(pieces.Queen("w", 3))
        self.board.append(pieces.King("w", 4))
        self.board.append(pieces.Bishop("w", 5))
        self.board.append(pieces.Knight("w", 6))
        self.board.append(pieces.Rook("w", 7))
        
        for i in xrange(8, 16):
            self.board.append(pieces.Pawn("w", i))
        
        for i in xrange(16, 48):
            self.board.append(None)
            
        for i in xrange(48, 56):
            self.board.append(pieces.Pawn("b", i))    
    
        self.board.append(pieces.Rook("b", 56))
        self.board.append(pieces.Knight("b", 57))
        self.board.append(pieces.Bishop("b", 58))
        self.board.append(pieces.Queen("b", 59))
        self.board.append(pieces.King("b", 60))
        self.board.append(pieces.Bishop("b", 61))
        self.board.append(pieces.Knight("b", 62))
        self.board.append(pieces.Rook("b", 63))
    
    def check_for_end_of_game(self):
        pass
    
    def check_for_mate(self):
        pass
    
    def check_for_stalemate(self):
        pass
    
    def check_for_draw(self):
        pass
    
    def draw_board(self):
        print "_"*24
        
        for row in xrange(7,-1,-1):
            for col in xrange(8):
                if self.board[8*row+col] is None:
                    print "| ",
                else:
                    print "|" + self.board[8*row+col].character,
            print "|"
        
        print "_"*24

    def make_move(self, move):
        try:
            (from_square, to_square) = self.get_move(move)
        except ValueError:
            return False
        
        try:
            from_square_nr = self.lines.index(from_square[0]) + 8*self.rows.index(from_square[1])
            to_square_nr = self.lines.index(to_square[0]) + 8*self.rows.index(to_square[1])
        except ValueError:
            return False 
        
        if not self.check_and_perform_move(from_square_nr, to_square_nr):
            return False
        
        #Change player to move
        self.white_to_move = not self.white_to_move
        return True
        
    def get_move(self, move):
        (from_square, to_square) = move.split("-")
        assert len(from_square) == 2
        assert len(to_square) == 2
        return (from_square, to_square)
            
    def check_and_perform_move(self, from_square_nr, to_square_nr):
        piece = self.board[from_square_nr]
        if piece is None:
            print "No piece to move."
            return False
        
        if not to_square_nr in piece.get_allowed_squares(self.board):
            print "Not valid move"
            return False
        
        self.set_all_pawns_to_not_have_moved_two_squares()
        self.board[from_square_nr] = None
        piece.square = to_square_nr
        
        if self.did_pawn_move_two_squares(piece, from_square_nr, to_square_nr):
            piece.moved_two_steps_last_turn = True
        if self.did_pawn_en_passant(piece, from_square_nr, to_square_nr):
            if self.white_to_move:
                self.board[to_square_nr-8] = None
            else:
                self.board[to_square_nr+8] = None
                
        self.board[to_square_nr] = piece
        
        return True
    
    def set_all_pawns_to_not_have_moved_two_squares(self):
        for i in xrange(len(self.board)):
            if isinstance(self.board[i], pieces.Pawn):
                self.board[i].moved_two_steps_last_turn = False
                
    def did_pawn_move_two_squares(swlf, piece, from_square_nr, to_square_nr):
        if not isinstance(piece, pieces.Pawn):
            return False
        
        if abs(from_square_nr-to_square_nr) == 16:
            print "Did move two squares"
            return True
        else:
            return False
        
    def did_pawn_en_passant(self, piece, from_square_nr, to_square_nr):
        if not isinstance(piece, pieces.Pawn):
            return False
        
        if abs(from_square_nr-to_square_nr) in [7,9]:
            if self.board[to_square_nr] is None:
                return True
        
        return False