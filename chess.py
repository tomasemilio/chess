from pieces import *


class Board:
	def __init__(self):
		self.RANKS = list(range(1, 9))
		self.FILES = list(range(1, 9))
		FILES_MAPPING = dict(zip(self.FILES, list('abcdefgh')))
		for rank in self.RANKS:
			for file in self.FILES:
				setattr(self, f"_{file}{rank}", Square(file, rank))
		self.setup()
		self.turn = 1

	def setup(self):
		# PAWNS
		for i in self.FILES:
			self.set_piece(f'{i}2', Pawn, 1)
			self.set_piece(f'{i}7', Pawn, -1)

		# # ROOKS
		# self.set_piece('a1', Rook(1))
		# self.set_piece('h1', Rook(1))
		# self.set_piece('a8', Rook(-1))
		# self.set_piece('h8', Rook(-1))

		# # BISHOPS
		# self.set_piece('c1', Bishop(1))
		# self.set_piece('f1', Bishop(1))
		# self.set_piece('c8', Bishop(-1))
		# self.set_piece('f8', Bishop(-1))

		# # KNIGHTS
		# self.set_piece('b1', Knight(1))
		# self.set_piece('g1', Knight(1))
		# self.set_piece('b8', Knight(-1))
		# self.set_piece('g8', Knight(-1))

		# # QUEENS
		# self.set_piece('d1', King(1))
		# self.set_piece('d8', King(-1))

		# # KINGS
		# self.set_piece('e1', King(1))
		# self.set_piece('e8', King(-1))

	def set_piece(self, coord, piece, color):
		square = getattr(self, f"_{coord}")
		square.piece = piece(square, color)

	def piece_legal_move(self, coord):
		square = getattr(self, f"_{coord}")
		if square.piece:
			return square.piece.legal_moves(self)

	# def __repr__(self):
	# 	return f'''
	# 	{self.SQUARES['a8']} {self.SQUARES['b8']} {self.SQUARES['c8']} {self.SQUARES['d8']} {self.SQUARES['e8']} {self.SQUARES['f8']} {self.SQUARES['g8']} {self.SQUARES['h8']}
	# 	{self.SQUARES['a7']} {self.SQUARES['b7']} {self.SQUARES['c7']} {self.SQUARES['d7']} {self.SQUARES['e7']} {self.SQUARES['f7']} {self.SQUARES['g7']} {self.SQUARES['h7']}
	# 	{self.SQUARES['a6']} {self.SQUARES['b6']} {self.SQUARES['c6']} {self.SQUARES['d6']} {self.SQUARES['e6']} {self.SQUARES['f6']} {self.SQUARES['g6']} {self.SQUARES['h6']}
	# 	{self.SQUARES['a5']} {self.SQUARES['b5']} {self.SQUARES['c5']} {self.SQUARES['d5']} {self.SQUARES['e5']} {self.SQUARES['f5']} {self.SQUARES['g5']} {self.SQUARES['h5']}
	# 	{self.SQUARES['a4']} {self.SQUARES['b4']} {self.SQUARES['c4']} {self.SQUARES['d4']} {self.SQUARES['e4']} {self.SQUARES['f4']} {self.SQUARES['g4']} {self.SQUARES['h4']}
	# 	{self.SQUARES['a3']} {self.SQUARES['b3']} {self.SQUARES['c3']} {self.SQUARES['d3']} {self.SQUARES['e3']} {self.SQUARES['f3']} {self.SQUARES['g3']} {self.SQUARES['h3']}
	# 	{self.SQUARES['a2']} {self.SQUARES['b2']} {self.SQUARES['c2']} {self.SQUARES['d2']} {self.SQUARES['e2']} {self.SQUARES['f2']} {self.SQUARES['g2']} {self.SQUARES['h2']}
	# 	{self.SQUARES['a1']} {self.SQUARES['b1']} {self.SQUARES['c1']} {self.SQUARES['d1']} {self.SQUARES['e1']} {self.SQUARES['f1']} {self.SQUARES['g1']} {self.SQUARES['h1']}
	# 	'''

	# def move(self, init_square, end_square):
	# 	if self.SQUARES[init_square].piece and \
	# 	self.SQUARES[init_square].piece.color == self.turn:
	# 		self.SQUARES[end_square].piece = self.SQUARES[init_square].piece
	# 		self.SQUARES[init_square].piece = None
	# 		self.turn *= -1
	# 	else:
	# 		print('Illegal move!')
	# 	print(self)

	# def list_square_legal_moves(self, square):
	# 	if isinstance(square.piece, Pawn): 



class Square:
	def __init__(self, file_int, rank_int):
		self.file = file_int
		self.rank = rank_int
		self.piece = None

	def __repr__(self):
		return f"{self.file}{self.rank}"

	def __str__(self):
		if self.piece is None:
			return ' '
		return f"{self.piece}"

board = Board()
print(board)



