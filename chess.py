from pieces import *
from squares import Square


class Board:
    RANKS = FILES = list(range(1, 9))
    FILE_LETTERS = list('abcdefgh')
    FILES_MAPPING = dict(zip(FILES, FILE_LETTERS))

    def __init__(self):
        self.turn = 1
        self.score = {
            1: [],
            -1: []
        }
        self.moves = {}
        self.n_move = 1
        self.setup_board()
        self.setup_pieces()


        # self.turn_mapping = {
        #   1: {
        #       'side': 'WHITE',
        #       'king': self.white_king
        #   },
        #   -1: {
        #       'side': 'BLACK',
        #       'king': self.black_king
        #   },
        # }

    def setup_board(self):
        '''
        Creating 64 instances of class Squares as self attributes.
        (Another alternative was to create a dictionary)
        '''
        for rank in type(self).RANKS:
            for file in type(self).FILES:
                setattr(self, f"{type(self).FILES_MAPPING[file]}{rank}", Square(file, rank))

    def __call__(self, coord):
        '''
        Callable for square of self.
        '''
        if hasattr(self, coord):
            return getattr(self, coord)

    def add_move(self, move):
        if self.turn == 1:
            self.moves[self.n_move] = {self.turn: move}
        else:
            self.moves[self.n_move][self.turn] = move

    @property
    def pieces(self):
        '''
        Returns all pieces of squares if they exist on the board.
        '''
        pieces = []
        for rank in type(self).RANKS:
            for file_letter in type(self).FILE_LETTERS:
                piece = self(f"{file_letter}{rank}").piece
                if piece:
                    pieces.append(piece)
        return pieces

    def setup_pieces(self):
        # PAWNS
        for i in type(self).FILE_LETTERS:
            Pawn(self, 1).square = self(f'{i}2')
            Pawn(self, -1).square = self(f'{i}7')

        # ROOKS
        Rook(self, 1).square = self.a1
        Rook(self, 1).square = self.h1
        Rook(self, -1).square = self.a8
        Rook(self, -1).square = self.h8

        # BISHOPS
        Bishop(self, 1).square = self.c1
        Bishop(self, 1).square = self.f1
        Bishop(self, -1).square = self.c8
        Bishop(self, -1).square = self.f8

        # KNIGHTS
        Knight(self, 1).square = self.b1
        Knight(self, 1).square = self.g1
        Knight(self, -1).square = self.b8
        Knight(self, -1).square = self.g8

        # QUEENS
        Queen(self, 1).square = self.d1
        Queen(self, -1).square = self.d8

        # KINGS
        King(self, 1).square = self.e1
        King(self, -11).square = self.e8

    def move(self, original_move):
        # PENDING
        # Check whose turn it is. 
        # If checked: are there available moves to get out of check?

        '''
        1. Split the move in:
            - Piece letter
            - Target Square
            - (optional) initial rank or file if two pieces can move to the same square.
        '''
        move = original_move.replace('x', '')
        moving_piece_info, target_square = move[: -2], move[-2:]
        if moving_piece_info == '':
            moving_piece, init_rank_file = ' ', ''
        else:
            moving_piece, init_rank_file = moving_piece_info[0].upper(), moving_piece_info[1:]

        if moving_piece not in Piece.LETTERS:
            raise ValueError('Not a valid piece letter.')

        elif (init_rank_file != '') and \
        ((init_rank_file not in type(self).RANKS) or \
        (init_rank_file.lower() not in type(self).FILE_LETTERS)):
            raise ValueError('Not a valid init square.')

        '''
        2. Check which piece is the one moving.
            - If we have more than one piece, we need to use the init_rank_file square.
            - If we don't get any final pieces, then it is an illegal move. 
        '''
        candidate_pieces = [i for i in self.pieces if type(i) == PIECE_MAPPING[moving_piece] and i.color == self.turn]
        final_pieces = []
        for piece in candidate_pieces:
            if self(target_square) in piece.legal_squares():
                final_pieces.append(piece)
        
        if len(final_pieces) == 0:
            raise ValueError('Not a valid move.')
        elif len(final_pieces) >= 2:
            # MISSING THIS CASE
            raise ValueError('More than one piece can move here.')
        else:
            piece_to_move = final_pieces[0]

        '''
        3. Move
            - Piece changes squares
            - Turn changes
            - Add move
        '''
        piece_to_move.square = self(target_square)
        self.add_move(original_move)

        self.turn *= -1
        if self.turn == 1:
            self.n_move += 1
        print(repr(self))

    def __repr__(self, highlighted=None):
        highlighted_squares = [self(i[1]) for i in highlighted] if highlighted is not None else []
        LIGHT_SQUARE = '107;30m'
        DARK_SQUARE = '44;30m'
        HIGHLIGHT_SQUARE = '41;30m'
        squares = [self(f"{file_letter}{rank}") for rank in type(self).RANKS[::-1] for file_letter in type(self).FILE_LETTERS]
        squares_str = []
        counter = 1
        for square in squares:
            if square in highlighted_squares:
                sq_str = '\033[' + HIGHLIGHT_SQUARE + ' ' + str(square) + ' \033[0m'
            elif counter == 1:
                sq_str = '\033[' + LIGHT_SQUARE + ' ' + str(square) + ' \033[0m'
            else:
                sq_str = '\033[' + DARK_SQUARE + ' ' + str(square) + ' \033[0m'
            squares_str.append(sq_str)

            if square.file_letter != 'h':
                counter *= -1
        board = """
        {0}{1}{2}{3}{4}{5}{6}{7}
        {8}{9}{10}{11}{12}{13}{14}{15}
        {16}{17}{18}{19}{20}{21}{22}{23}
        {24}{25}{26}{27}{28}{29}{30}{31}
        {32}{33}{34}{35}{36}{37}{38}{39}
        {40}{41}{42}{43}{44}{45}{46}{47}
        {48}{49}{50}{51}{52}{53}{54}{55}
        {56}{57}{58}{59}{60}{61}{62}{63}
        """.format(*tuple(squares_str))

        print(f'''
WHITE -  {' '.join([j.get(1) for i, j in self.moves.items() if j.get(1)])}
BLACK -  {' '.join([j.get(-1) for i, j in self.moves.items() if j.get(-1)])}
            ''')

        return board
    

if __name__ == '__main__':
    b = Board()
    b.move('e4')
    b.move('e5')
    b.move('Nf3')
    b.move('Nc6')
    b.move('Bb5')
    b.move('a6')
    b.move('Bxc6')
    # print(b.moves)