 
class Color(Enum):
    WHITE = 1
    BLACK = 2

class Square:
    def __init__(self, color):
        self.color = color
        self.piece = None
    
    def get_piece(self):
        return self.piece

    def get_color(self):
        return self.color
    
    def set_piece(self, piece):
        self.piece = piece

class Piece(ABC):
    
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color

    @staticmethod
    def is_within_grid(end_row, end_col):
        return 0 <= end_row <= 7 and 0 <= end_col <= 7
    
    @abstractmethod
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        pass

    @abstractmethod
    def get_symbol(self):
        pass

class Pawn(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        if not Piece.is_within_grid(end_row, end_col):
            return False
        row_movement = end_row - start_row
        col_movement = end_col - start_col
        direction = -1 if self.get_color() == Color.WHITE else 1

        if col_movement != 0:
            return False
        
        if row_movement == direction and board[end_row][end_col].get_piece() is None:
            return True
        if (self.is_first_move(start_row) and row_movement == (2 * direction) and 
            board[start_row + direction][start_col].get_piece() is None and 
            board[end_row][end_col].get_piece() is None):
            return True
        
        return False
    
    def get_symbol(self):
            return "P" if self.get_color() == Color.WHITE else "p"
    
    def is_first_move(self, start_row):
        return (self.get_color() == Color.WHITE and start_row == 6) or \
        (self.get_color() == Color.BLACK and start_row == 1)
    

class Knight(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        if not Piece.is_within_grid(end_row, end_col):
            return False
        row_movement = abs(end_row - start_row)
        col_movement = abs(end_col - start_col)

        if row_movement == 2 and col_movement == 1 or \
            row_movement == 1 and col_movement == 2:
        
            if board[end_row][end_col].get_piece() is not None and \
                board[end_row][end_col].get_piece().get_color() == self.get_color():
                return False
            
            return True
        
        return False
    
    def get_symbol(self):
        return "N" if self.get_color() == Color.WHITE else "n"
    


class MovementUtil:

    @staticmethod
    def is_valid_straight_move(start_row, start_col, end_row, end_col, color, board):
        if not Piece.is_within_grid(end_row, end_col):
            return False
        
        row_movement = abs(end_row - start_row)
        col_movement = abs(end_col - start_col)

        if row_movement != 0 and col_movement != 0 or (row_movement == 0 and col_movement == 0):
            return False
        else:
            row_increment = 1 if end_row > start_row else -1
            col_increment = 1 if end_col > start_col else -1

            if row_movement == 0:
                y = start_col + col_increment
                while y != end_col:
                    if board[start_row][y].get_piece() is not None:
                        return False
                    y += col_increment
            else: 
                x = start_row + row_increment
                while x != end_row:
                    if board[x][start_col].get_piece() is not None:
                        return False
                    x += row_increment

                if board[end_row][end_col].get_piece() is not None and \
                    board[end_row][end_col].get_piece().get_color() == color:
                        return False
                return True
            
    @staticmethod
    def is_valid_diagonal_move(start_row, start_col, end_row, end_col, color, board):
        if not Piece.is_within_grid(end_row, end_col):
            return False
        
        row_movement = abs(end_row - start_row)
        col_movement = abs(end_col - start_col)

        if row_movement == 0 or col_movement == 0:
            return False
        
        if row_movement == col_movement:
            row_increment = 1 if end_row > start_row else -1
            col_increment = 1 if end_col > start_col else -1

            x, y = start_row + row_increment, start_col + col_increment

            while x != end_row and y != end_col:
                if board[x][y].get_piece() is not None:
                    return False
                
                x += row_increment
                y += col_increment

            if board[end_row][end_col].get_piece() is not None and \
                board[end_row][end_col].get_piece().get_color() == color:
                return False
            
            return True
        else:   
            return False

class Rook(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        return MovementUtil.is_valid_straight_move(start_row, start_col, end_row, end_col, self.get_color(), board)
    
    def get_symbol(self):
        return "R" if self.get_color() == Color.WHITE else 'r'
    
class Bishop(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        return MovementUtil.is_valid_diagonal_move(start_row, start_col, end_row, end_col, self.get_color(), board)
    
    def get_symbol(self):
        return "B" if self.get_color() == Color.WHITE else 'b'
    

class King(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        if not Piece.is_within_grid(end_row, end_col):
            return False
        
        row_movement = abs(end_row - start_row)
        col_movement = abs(end_col - start_col)

        if row_movement > 1 or col_movement > 1:
            return False
        
        if board[end_row][end_col].get_piece() is not None and \
            board[end_row][end_col].get_piece().get_color() == self.get_color():
            return False
        
        return True
    
    def get_symbol(self):
        return "K" if self.get_color == Color.WHITE else 'k'
    

class Queen(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        return MovementUtil.is_valid_straight_move(start_row, start_col, end_row, end_col, self.get_color(), board) or \
               MovementUtil.is_valid_diagonal_move(start_row, start_col, end_row, end_col, self.get_color(), board)

    def get_symbol(self):
        return "Q" if self.get_color() == Color.WHITE else 'q'