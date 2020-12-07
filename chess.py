from pieces import *


class Board:
	def __init__(self):
		self.RANKS = list(range(1, 9))
		self.FILES = list(range(1, 9))
		self.FILES_MAPPING = dict(zip(self.FILES, list('abcdefgh')))
		for rank in self.RANKS:
			for file in self.FILES:
				setattr(self, f"{self.FILES_MAPPING[file]}{rank}", Square(file, rank))
		self.setup()
		self.turn = 1

	def setup(self):
		# # PAWNS
		# for i in list('abcdefgh'):
		# 	self.set_piece(f'{i}2', Pawn, 1)
		# 	self.set_piece(f'{i}7', Pawn, -1)

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

		# # KNIGHTS
		# self.set_piece('b1', Knight, 1)
		# self.set_piece('g1', Knight, 1)
		# self.set_piece('b8', Knight, -1)
		# self.set_piece('g8', Knight, -1)

		# QUEENS
		self.set_piece('d1', Queen, 1)
		self.set_piece('d8', Queen, -1)

		# KINGS
		self.set_piece('e1', King, 1)
		self.set_piece('e8', King, -1)

	def set_piece(self, coord, piece, color):
		piece = piece(self, coord, color)
		piece.square.piece = piece

	def piece_legal_move(self, coord):
		square = getattr(self, f"{coord}")
		if square.piece:
			return square.piece.legal_squares(self)

	def move(self, old_square_coord, new_square_coord):
		if hasattr(self, old_square_coord) and hasattr(self, new_square_coord):
			old_square = getattr(self, new_square_coord)	
			new_square = getattr(self, new_square_coord)	

			if hasattr(self, old_square_coord).piece:
				piece = getattr(self, old_square_coord).piece
				legal_squares = piece.legal_squares(self)

				old_square.piece = None
				new_square.piece = piece
				piece.square = new_square

		print(self)


	def __repr__(self):
		PIECE_COLOR = ''
		LIGHT_SQUARE = '107;30m'
		DARK_SQUARE = '44;30m'
		VALID_SQUARE = ''

		return """
	{0}{1}{2}{3}{4}{5}{6}{7}
	{8}{9}{10}{11}{12}{13}{14}{15}
	{16}{17}{18}{19}{20}{21}{22}{23}
	{24}{25}{26}{27}{28}{29}{30}{31}
	{32}{33}{34}{35}{36}{37}{38}{39}
	{40}{41}{42}{43}{44}{45}{46}{47}
	{48}{49}{50}{51}{52}{53}{54}{55}
	{56}{57}{58}{59}{60}{61}{62}{63}
		""".format(
			('\033[' + LIGHT_SQUARE + ' ' + str(self.a8) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.b8) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.c8) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.d8) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.e8) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.f8) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.g8) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.h8) + ' \033[0m'),

			('\033[' + DARK_SQUARE + ' ' + str(self.a7) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.b7) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.c7) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.d7) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.e7) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.f7) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.g7) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.h7) + ' \033[0m'),

			('\033[' + LIGHT_SQUARE + ' ' + str(self.a6) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.b6) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.c6) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.d6) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.e6) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.f6) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.g6) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.h6) + ' \033[0m'),

			('\033[' + DARK_SQUARE + ' ' + str(self.a5) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.b5) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.c5) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.d5) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.e5) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.f5) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.g5) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.h5) + ' \033[0m'),

			('\033[' + LIGHT_SQUARE + ' ' + str(self.a4) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.b4) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.c4) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.d4) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.e4) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.f4) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.g4) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.h4) + ' \033[0m'),

			('\033[' + DARK_SQUARE + ' ' + str(self.a3) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.b3) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.c3) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.d3) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.e3) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.f3) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.g3) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.h3) + ' \033[0m'),

			('\033[' + LIGHT_SQUARE + ' ' + str(self.a2) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.b2) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.c2) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.d2) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.e2) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.f2) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.g2) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.h2) + ' \033[0m'),

			('\033[' + DARK_SQUARE + ' ' + str(self.a1) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.b1) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.c1) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.d1) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.e1) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.f1) + ' \033[0m'),
			('\033[' + DARK_SQUARE + ' ' + str(self.g1) + ' \033[0m'),
			('\033[' + LIGHT_SQUARE + ' ' + str(self.h1) + ' \033[0m'),
		)



class Square:
	def __init__(self, file, rank):
		self.file = file
		self.rank = rank
		self.FILES_MAPPING = dict(zip(list(range(1, 9)), list('abcdefgh')))
		self.piece = None

	def __repr__(self):
		return f"{self.FILES_MAPPING[self.file]}{self.rank}"

	def __str__(self):
		if self.piece is None:
			return ' '
		return f"{self.piece}"

board = Board()
print(board)
# print(board.a1.piece)
# print(board.a1.piece.legal_squares())



