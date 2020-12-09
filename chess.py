from pieces import *


class Board:
	def __init__(self):
		self.RANKS = list(range(1, 9))
		self.FILES = list(range(1, 9))
		self.FILE_LETTERS = list('abcdefgh')
		self.FILES_MAPPING = dict(zip(self.FILES, self.FILE_LETTERS))
		self.turn = 1
		self.score = {
			1: [],
			-1: []
		}
		self.setup_board()
		self.setup_pieces()

	def setup_board(self):
		for rank in self.RANKS:
			for file in self.FILES:
				setattr(self, f"{self.FILES_MAPPING[file]}{rank}", Square(file, rank))

	def setup_pieces(self):
		# PAWNS
		for i in self.FILE_LETTERS:
			self.set_piece(f'{i}2', Pawn, 1)
			self.set_piece(f'{i}7', Pawn, -1)

		# ROOKS
		self.set_piece('a1', Rook, 1)
		self.set_piece('h1', Rook, 1)
		self.set_piece('a8', Rook, -1)
		self.set_piece('h8', Rook, -1)

		# BISHOPS
		self.set_piece('c1', Bishop, 1)
		self.set_piece('f1', Bishop, 1)
		self.set_piece('c8', Bishop, -1)
		self.set_piece('f8', Bishop, -1)

		# KNIGHTS
		self.set_piece('b1', Knight, 1)
		self.set_piece('g1', Knight, 1)
		self.set_piece('b8', Knight, -1)
		self.set_piece('g8', Knight, -1)

		# QUEENS
		self.set_piece('d1', Queen, 1)
		self.set_piece('d8', Queen, -1)

		# KINGS
		self.set_piece('e1', King, 1)
		self.set_piece('e8', King, -1)

	def __call__(self, coord):
		if hasattr(self, coord):
			return getattr(self, coord)

	def set_piece(self, coord, piece, color):
		if self(coord):
			piece = piece(self, coord, color)
			piece.square.piece = piece

	def piece(self, coord):
		return self(coord).piece if self(coord) else None
	
	def piece_legal_move(self, coord, show=True):
		square = self(coord)
		if square and square.piece and square.piece.color == self.turn:
			piece_legal_moves = [(square.coord, i.coord) for i in square.piece.legal_squares()]
			if show:
				print(self.__repr__(highlighted=piece_legal_moves))
			return piece_legal_moves

	def all_legal_moves(self):
		all_legal_moves = {}
		for rank in self.RANKS:
			for file in self.FILE_LETTERS:
				coord = f"{file}{rank}"
				piece  = self.piece(coord)
				if piece:
					piece_legal_moves = self.piece_legal_move(coord, show=False)
					if piece_legal_moves:
						all_legal_moves[self.piece(coord)] = piece_legal_moves
		return all_legal_moves				 

	def move(self, old_coord, new_coord):
		moves = self.piece_legal_move(old_coord)
		if moves and new_coord in [i[1] for i in moves]:
			piece = self.piece(old_coord)
			self(old_coord).piece = None
			if self(new_coord).piece:
				self.score[self.turn].append(self(new_coord).piece)
			self(new_coord).piece = piece
			piece.square = self(new_coord)
			self.turn *= -1
		print(self)

	def __repr__(self, highlighted=None):
		highlighted_squares = [self(i[1]) for i in highlighted] if highlighted is not None else []
		LIGHT_SQUARE = '107;30m'
		DARK_SQUARE = '44;30m'
		HIGHLIGHT_SQUARE = '41;30m'
		squares = [self(f"{file_letter}{rank}") for rank in self.RANKS[::-1] for file_letter in self.FILE_LETTERS]
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
			WHITE {self.score[1]}
			BLACK {self.score[-1]}
			SCORE {sum([i.value for i in self.score[1]]) - sum([i.value for i in self.score[-1]])}''')
		return board


class Square:
	def __init__(self, file, rank):
		self.file = file
		self.rank = rank
		self.FILES_MAPPING = dict(zip(list(range(1, 9)), list('abcdefgh')))
		self.file_letter = self.FILES_MAPPING[self.file]
		self.coord = f"{self.file_letter}{self.rank}"
		self.piece = None

	def __repr__(self):
		return f"{self.FILES_MAPPING[self.file]}{self.rank}"

	def __str__(self):
		if self.piece is None:
			return ' '
		return f"{self.piece}"

if __name__ == '__main__':
	b = Board()
	print(b)




