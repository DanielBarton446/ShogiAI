import python_shogi.shogi as ps
import material_consts as mc

def main():
    game = ps.Board()
    print(evaluator(game))

def count_material(board : ps.Board):
    # This runs pretty slow -- around 0.0004 seconds per call
    value = 0
    for sq in ps.SQUARES:
        mask = ps.BB_SQUARES[sq]
        piece = str(board.piece_at(sq))
        for piece_type in ps.PIECE_TYPES_WITHOUT_KING:
            if mask & board.piece_bb[piece_type]:
                if piece.isupper():
                    value += mc.ON_BOARD_VALUES.get(piece_type)
                elif piece.islower():
                    value -= mc.ON_BOARD_VALUES.get(piece_type)
    return value



def evaluator(board : ps.Board):
    evaluation = 0
    evaluation += count_material(board)
    return round(evaluation, 3)

if __name__ == "__main__":
    main()
