from pieces import Piece

class Square:
    FILES_MAPPING = dict(zip(list(range(1, 9)), list('abcdefgh')))
    
    def __init__(self, file, rank):
        self.file = file
        self.rank = rank
        self.file_letter = type(self).FILES_MAPPING[self.file]
        self.coord = f"{self.file_letter}{self.rank}"
        self._piece = None

    def __repr__(self):
        return f"{type(self).FILES_MAPPING[self.file]}{self.rank}"

    def __str__(self):
        if self.piece is None:
            return ' '
        return f"{self.piece}"

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, new_piece):
        if isinstance(new_piece, Piece):
            if self._piece:
                del self._piece.square
            self._piece = new_piece
            '''
            We cannot do this line:
            - self._piece.square = self
            Since we have:
            - self._square.piece = self
            This would be an infinite loop
            Decision: We asign a square to a piece (like moving).
            Never: We asign a piece to a square
            '''
        else:
            raise ValueError('Not a valid Piece for square asignment.')

    @piece.deleter
    def piece(self):
        self._piece = None