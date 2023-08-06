
# About
`ajar` is a python package that attempts to automate the generation of opening PGNs. It does this by allowing the user to specify a starting position (in FEN notation), as well as parameters such as depth, percent, etc. It then utilizes lichess's database to identify likely responses to moves, and uses Stockfish to generate computer approved moves.

The output pgn can be used in places like lichess/chesstempo/etc for studying. Remember that Stockfish cannot explain it's ideas behind moves, and so your opening PGNs may not always have human moves. If you're looking for explanations of opening systems, it's still better to find a master's course or free opening lessons on lichess.

# Installation
```bash
pip install ajar
```