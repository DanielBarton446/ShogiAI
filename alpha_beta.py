import python_shogi.shogi as ps
import material_consts as mc

def main():
    pass

# Traditionally, player 1 is BLACK and player 2 is WHITE
def legal_moves_for_current_player(board : ps.Board):
    legal_moves = []
    for mv in board.generate_legal_moves():
        src = mv.from_square
        piece = board.piece_at(src)
        if piece.color == board.turn:
            legal_moves.append(mv)
    return legal_moves


def count_material(board : ps.Board):
    value = 0
    for sq in ps.SQUARES:
        piece = board.piece_at(sq)
        if piece is not None and piece.piece_type is not ps.KING:
            if piece.color == ps.BLACK:
                value += mc.ON_BOARD_VALUES.get(piece.piece_type)
            else:
                value -= mc.ON_BOARD_VALUES.get(piece.piece_type)
    
    # board.pieces_in_hand gives a counter, Counter.elements() 
    # expands the count of each piece.
    # E.g. c = Counter({1:2}) is 2 pawns(per index defintion)
    #  --- c.elements() evaluates to the list [1,1]
    for piece_index in board.pieces_in_hand[ps.BLACK].elements():
        # piece_index is based on PIECE_TYPES_WITH_NONE.
        piece_type = ps.PIECE_TYPES_WITH_NONE[piece_index] 
        value += mc.IN_HAND_VALUES.get(piece_type)

    for piece_index in board.pieces_in_hand[ps.WHITE]:
        piece_type = ps.PIECE_TYPES_WITH_NONE[piece_index] 
        value -= mc.IN_HAND_VALUES.get(piece_type)
    
    return value


def evaluator(board : ps.Board):
    evaluation = 0
    evaluation += count_material(board)
    return round(evaluation, 3)

if __name__ == "__main__":
    main()
