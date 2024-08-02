 
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

