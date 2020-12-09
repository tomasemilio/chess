# Object Oriented Chess Program

The goal of this program is to implement OOP principles for a chess application.

## Basic Usage

Unicode chars
♖  ♘  ♗  ♕  ♔  ♙
♜  ♞  ♝  ♛  ♚  ♟︎

```python
b = Board()
print(b)
```
![Board Set up](/docs/board.png?raw=true "Board")

```python
b.move('e2', 'e4')
b.move('d7', 'd5')
```
![Moves](/docs/move.png?raw=true "Moves")

We can show leval moves highlighting squares depending on whose turn it is.
```python

b.piece_legal_move('e4')

```
![Legal](/docs/legal.png?raw=true "Moves")


We can also show all legal moves (for white since it is its move).
```python
b.all_legal_moves()

{
	♘: [('b1', 'c3'), ('b1', 'a3')],
	♕: [('d1', 'e2'), ('d1', 'f3'), ('d1', 'g4'), ('d1', 'h5')],
	♔: [('e1', 'e2')],
	♘: [('g1', 'e2'), ('g1', 'h3'), ('g1', 'f3')],
	♙: [('a2', 'a3'), ('a2', 'a4')],
	♙: [('b2', 'b3'), ('b2', 'b4')],
	♙: [('c2', 'c3'), ('c2', 'c4')],
	♙: [('d2', 'd3'), ('d2', 'd4')],
	♙: [('f2', 'f3'), ('f2', 'f4')],
	♙: [('g2', 'g3'), ('g2', 'g4')],
	♙: [('h2', 'h3'), ('h2', 'h4')],
	♙: [('e4', 'e5'), ('e4', 'd5')]
}
```
Evaluation after taking
```python

b.move('e4', 'd5')

```
![Takes](/docs/takes.png?raw=true "Takes")

## Things missing
1. Promotion
2. Check
3. Checkmate
4. En Passant
5. Engine to evaluate position

