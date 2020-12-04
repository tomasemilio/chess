class Piece:
	def __init__(self, square, color):
		self.color = color
		self.square = square
		self.moves = []


class Pawn(Piece):
	value = 1
	letter = None

	def __repr__(self):
		return '♙' if self.color == 1 else '♟︎'

	def legal_moves(self, board):
		legal_squares = []

		# Move forward
		new_square_coord = f'_{self.square.file}{self.square.rank + self.color}'
		if hasattr(board, new_square_coord):
			new_square = getattr(board, new_square_coord)
			if new_square.piece is None:
				legal_squares.append(new_square)

		# Move forward 2
		if (self.square.rank == 2 and self.color == 1) or ((self.square.rank == 7 and self.color == -1)):
			new_square_coord = f'_{self.square.file}{self.square.rank + self.color * 2}'
			new_square = getattr(board, new_square_coord)
			if new_square.piece is None:
				legal_squares.append(new_square)

		# Eat
		for side in [1, -1]:
			new_square_coord = f'_{self.square.file + side}{self.square.rank + self.color}'
			if hasattr(board, new_square_coord):
				new_square = getattr(board, new_square_coord)
				if new_square.piece and new_square.piece.color != self.color:
					legal_squares.append(new_square)

		# Missing
		# EN PASSANT
		# PROMOTION

		return legal_squares


class Queen(Piece):
	value = 9
	letter = 'Q'

	def __repr__(self):
		return '♕' if self.color == 1 else '♛'

	def legal_moves(self, board):
		legal_squares = []




class Bishop(Piece):
	value = 3
	letter = 'B'

	def __repr__(self):
		return '♗' if self.color == 1 else '♝'


class Knight(Piece):
	value = 3
	letter = 'N'

	def __repr__(self):
		return '♘' if self.color == 1 else '♞'


class Rook(Piece):
	value = 5
	letter = 'R'

	def __repr__(self):
		return '♖' if self.color == 1 else '♜'


class King(Piece):
	value = 0
	letter = 'K'

	def __repr__(self):
		return '♔' if self.color == 1 else '♚'

