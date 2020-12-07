class Piece:
	def __init__(self, board, coord, color):
		self.board = board
		self.color = color
		self.square = getattr(board, coord)


	def legal_squares(self):
		legal_squares = []
		steps = [1] if self.letter == 'K' else range(1, 8)

		if self.letter in ['Q', 'K', 'R']:
			# going up/down on rank
			for direction in steps:
				for step in range(1, 8):
					new_rank = self.square.rank + step * direction
					new_file = self.board.FILES_MAPPING[self.square.file]
					new_square_coord = f"{new_file}{new_rank}"
					if hasattr(self.board, new_square_coord):
						new_square = getattr(self.board, new_square_coord)
						if new_square.piece is None:
							legal_squares.append(new_square)
						elif new_square.piece.color != self.color:
							legal_squares.append(new_square)
							break
						else:
							break
					else:
						break

			# Going left/right file
			for direction in steps:
				for step in range(1, 8):
					new_rank = self.square.rank
					try:
						new_file = self.board.FILES_MAPPING[self.square.file + step * direction]
					except:
						break
					new_square_coord = f"{new_file}{new_rank}"
					if hasattr(self.board, new_square_coord):
						new_square = getattr(self.board, new_square_coord)
						if new_square.piece is None:
							legal_squares.append(new_square)
						elif new_square.piece.color != self.color:
							legal_squares.append(new_square)
							break
						else:
							break
					else:
						break
		
		if self.letter in ['Q', 'K' 'B']:
			# diagonals
			for direction in steps:
				for direction2 in [1, -1]:
					for step in range(1, 8):
						new_rank = self.square.rank + step * direction
						try:
							new_file = self.board.FILES_MAPPING[self.square.file + step * direction2]
						except:
							break
						new_square_coord = f"{new_file}{new_rank}"
						if hasattr(self.board, new_square_coord):
							new_square = getattr(self.board, new_square_coord)
							if new_square.piece is None:
								legal_squares.append(new_square)
							elif new_square.piece.color != self.color:
								legal_squares.append(new_square)
								break
							else:
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
					try:
						new_file = self.board.FILES_MAPPING[self.square.file + direction2]
					except:
						continue
					new_square_coord = f"{new_file}{new_rank}"
					if hasattr(self.board, new_square_coord):
						new_square = getattr(self.board, new_square_coord)
						if new_square.piece is None or new_square.piece.color != self.color:
							legal_squares.append(new_square)
						else:
							continue
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
		try:
			new_file = self.board.FILES_MAPPING[self.square.file]
			new_square_coord = f'{new_file}{new_rank}'
			if hasattr(self.board, new_square_coord):
				new_square = getattr(self.board, new_square_coord)
				if new_square.piece is None:
					legal_squares.append(new_square)
		except:
			pass

		# Move forward 2
		if (self.square.rank == 2 and self.color == 1) or ((self.square.rank == 7 and self.color == -1)):
			new_rank = self.square.rank + self.color * 2
			try:
				new_file = self.board.FILES_MAPPING[self.square.file]
				new_square_coord = f'{new_file}{new_rank}'
				new_square = getattr(self.board, new_square_coord)
				if new_square.piece is None:
					legal_squares.append(new_square)
			except:
				pass

		# Eat
		for side in [1, -1]:
			new_rank = self.square.rank + self.color
			try:
				new_file = self.board.FILES_MAPPING[self.square.file + side]
				new_square_coord = f'{new_file}{new_rank}'
				if hasattr(self.board, new_square_coord):
					new_square = getattr(self.board, new_square_coord)
					if new_square.piece and new_square.piece.color != self.color:
						legal_squares.append(new_square)
			except:
				pass

		# Missing
		# EN PASSANT
		# PROMOTION

		return legal_squares















