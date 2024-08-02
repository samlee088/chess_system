 
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

