

class Piece(object):
    def __init__(self, colour, square):
        self.colour = colour
        self.square = square
    
    def get_allowed_squares(self, board):
        #Return board after move. Generator
        raise NotImplementedError()

class King(Piece):
    def __init__(self, colour, square):
        if colour == "w":
            self.character = "K"
        else:
            self.character = "k"

class Queen(Piece):
    def __init__(self, colour, square):
        if colour == "w":
            self.character = "Q"
        else:
            self.character = "q"

class Rook(Piece):
    def __init__(self, colour, square):
        if colour == "w":
            self.character = "R"
        else:
            self.character = "r"

class Bishop(Piece):
    def __init__(self, colour, square):
        if colour == "w":
            self.character = "B"
        else:
            self.character = "b"

class Knight(Piece):
    def __init__(self, colour, square):
        if colour == "w":
            self.character = "N"
        else:
            self.character = "n"
            
    def get_allowed_squares(self, board):
        allowed_squares = []
        
        return allowed_squares

class Pawn(Piece):
    def __init__(self, colour, square):
        super(Pawn, self).__init__(colour, square)
        if colour == "w":
            self.character = "P"
        else:
            self.character = "p"
        self.moved_two_steps_last_turn = False
        
    def get_allowed_squares(self, board):
        allowed_squares = []
        if self.colour == "w":
            if self.square in xrange(8,16):
                #Possibly move two steps
                if board[self.square+8] is None and board[self.square+16] is None:
                    allowed_squares.append(self.square+16)
    
            if board[self.square+8] is None:
                allowed_squares.append(self.square+8)
            
            if self.square % 8 != 0:
                if board[self.square+7] is not None and board[self.square+7].colour == "b":
                    allowed_squares.append(self.square+7)
                elif board[self.square+7] is None and board[self.square-1] is not None and \
                    board[self.square-1].colour == "b" and \
                    isinstance(board[self.square-1], Pawn) and board[self.square-1].moved_two_steps_last_turn:
                    allowed_squares.append(self.square+7)
            
            if self.square % 8 != 7:
                if board[self.square+9] is not None and board[self.square+9].colour == "b":
                    allowed_squares.append(self.square+9)
                elif board[self.square+9] is None and board[self.square+1] is not None and \
                    board[self.square+1].colour == "b" and \
                    isinstance(board[self.square+1], Pawn) and board[self.square+1].moved_two_steps_last_turn:
                    allowed_squares.append(self.square+9)
            
        elif self.colour == "b":
            if self.square in xrange(48,56):
                #Possibly move two steps
                if board[self.square-8] is None and board[self.square-16] is None:
                    allowed_squares.append(self.square-16)
    
            if board[self.square-8] is None:
                allowed_squares.append(self.square-8)
                  
            if self.square % 8 != 0:
                if board[self.square-9] is not None and board[self.square-9].colour == "w":
                    allowed_squares.append(self.square-9)
                elif board[self.square-9] is None and board[self.square-1] is not None and \
                    board[self.square-1].colour == "w" and \
                    isinstance(board[self.square-1], Pawn) and board[self.square-1].moved_two_steps_last_turn:
                    allowed_squares.append(self.square-9)
            
            if self.square % 8 != 7:
                if board[self.square-7] is not None and board[self.square-7].colour == "w":
                    allowed_squares.append(self.square-7)
                elif board[self.square-7] is None and board[self.square+1] is not None and \
                    board[self.square+1].colour == "w" and \
                    isinstance(board[self.square+1], Pawn) and board[self.square+1].moved_two_steps_last_turn:
                    allowed_squares.append(self.square-7)         
            
        #Case 1: e.p
        #Case 2: to back-rank

        print self.square
        print allowed_squares        
        return allowed_squares