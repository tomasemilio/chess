class Piece:
	LETTERS = list('KQRBN ')

	def __init__(self, board, color):
		self.board = board
		self.color = color
		self.active = False
		self._square = None

	@property
	def square(self):
		return self._square

	@square.setter
	def square(self, new_square):
		if self._square:
			del	self._square.piece
		self._square = new_square
		self._square.piece = self
		self.active = True

	@square.deleter
	def square(self):
		self.active = False
		self._square = None

	def legal_squares(self):
		legal_squares = []
		steps = [1] if self.letter == 'K' else range(1, 8)

		if self.letter in ['Q', 'K', 'R']:
			# going up/down on rank
			for direction in [1, -1]:
				for step in steps:
					new_rank = self.square.rank + step * direction
					new_file = self.square.file_letter
					new_square_coord = f"{new_file}{new_rank}"
					new_square = self.board(new_square_coord)
					if new_square:
						if new_square.piece is None:
							print(self.letter, self.color, new_square.__repr__(), 'empty')
							legal_squares.append(new_square)
						else:
							if new_square.piece.color != self.color: 
								print(self.letter, self.color, new_square.__repr__(), 'taking')
								legal_squares.append(new_square)
							break
					else:
						break

			# Going left/right file
			for direction in [1 , -1]:
				for step in steps:
					new_rank = self.square.rank
					new_file = self.board.FILES_MAPPING.get(self.square.file + step * direction)
					new_square_coord = f"{new_file}{new_rank}"
					new_square = self.board(new_square_coord)
					if new_square:
						if new_square.piece is None:
							legal_squares.append(new_square)
							print(self.letter, self.color, new_square.__repr__(), 'empty')
						else:
							if new_square.piece.color != self.color:
								print(self.letter, self.color, new_square.__repr__(), 'taking')
								legal_squares.append(new_square)
							break
					else:
						break
		
		if self.letter in ['Q', 'K' 'B']:
			# diagonals
			for direction in [-1, 1]:
				for direction2 in [1, -1]:
					for step in steps:
						new_rank = self.square.rank + step * direction
						new_file = self.board.FILES_MAPPING.get(self.square.file + step * direction2)
						new_square_coord = f"{new_file}{new_rank}"
						new_square = self.board(new_square_coord)
						if new_square:
							if new_square.piece is None:
								legal_squares.append(new_square)
								print(self.letter, self.color, new_square.__repr__(), 'empty')
							else:
								if new_square.piece.color != self.color:
									print(self.letter, self.color, new_square.__repr__(), 'taking')
									legal_squares.append(new_square)
								break
						else:
							break

		return legal_squares


class Rook(Piece):
	value = 5
	letter = 'R'

	def __repr__(self):
		return '♖' if self.color == 1 else '♜'


class Queen(Piece):
	value = 9
	letter = 'Q'

	def __repr__(self):
		return '♕' if self.color == 1 else '♛'


class Bishop(Piece):
	value = 3
	letter = 'B'

	def __repr__(self):
		return '♗' if self.color == 1 else '♝'


class King(Piece):
	value = 0
	letter = 'K'

	def __repr__(self):
		return '♔' if self.color == 1 else '♚'

	def is_checked(self):
		attackers = []
		opposite_pieces = [piece for piece in self.board.pieces if piece.color != self.color]
		for opposite_piece in opposite_pieces:
			if self.square in opposite_piece.legal_squares():
				attackers.append(opposite_piece)

		return attackers


class Knight(Piece):
	value = 3
	letter = 'N'

	def __repr__(self):
		return '♘' if self.color == 1 else '♞'


	def legal_squares(self):
		legal_squares = []
		steps = [1, -1, 2, -2]
		for direction in steps:
			for direction2 in steps:
				if abs(direction) == abs(direction2):
					continue
				else:
					new_rank = self.square.rank + direction
					new_file = self.board.FILES_MAPPING.get(self.square.file + direction2)
					new_square_coord = f"{new_file}{new_rank}"
					new_square = self.board(new_square_coord)
					if new_square and (new_square.piece is None or new_square.piece.color != self.color):
						legal_squares.append(new_square)

		return legal_squares


class Pawn(Piece):
	value = 1
	letter = None

	def __repr__(self):
		return '♙' if self.color == 1 else '♟︎'

	def legal_squares(self):
		legal_squares = []

		# Move forward
		new_rank = self.square.rank + self.color
		new_file = self.board.FILES_MAPPING.get(self.square.file)
		new_square_coord = f'{new_file}{new_rank}'
		new_square = self.board(new_square_coord)
		if new_square and new_square.piece is None:
			legal_squares.append(new_square)

		# Move forward 2
		if (self.square.rank == 2 and self.color == 1) or ((self.square.rank == 7 and self.color == -1)):
			new_rank = self.square.rank + self.color * 2
			new_file = self.board.FILES_MAPPING.get(self.square.file)
			new_square_coord = f'{new_file}{new_rank}'
			new_square = self.board(new_square_coord)
			if new_square and new_square.piece is None:
				legal_squares.append(new_square)

		# Eat
		for side in [1, -1]:
			new_rank = self.square.rank + self.color
			new_file = self.board.FILES_MAPPING.get(self.square.file + side)
			new_square_coord = f'{new_file}{new_rank}'
			new_square = self.board(new_square_coord)
			if new_square and new_square.piece and new_square.piece.color != self.color:
				legal_squares.append(new_square)			

		# Missing
		# EN PASSANT
		# PROMOTION

		return legal_squares


PIECE_MAPPING = {
	' ': Pawn,
	'K': King,
	'Q': Queen,
	'B': Bishop,
	'R': Rook,
	'N': Knight
}














