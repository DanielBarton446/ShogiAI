import python_shogi.shogi as ps
import material_consts as mc
import king_safety as ks

sig_figs = 3
mobility_weight = 3.0

def checkmate_value(board : ps.Board):
    if board.is_checkmate():
        if board.turn == ps.BLACK:
            return float('-inf')
        else:
            return float('inf')
    return 0.0


def count_mobility(board : ps.Board):
    value = 0.0
    count = 0.0
    player_moves = board.generate_legal_moves()
    for _ in player_moves:
        count += 1.0
        if board.turn == ps.BLACK:
            value += 1.0
        else: 
            value -= 1.0

    board.turn = not board.turn # change turn to view other player's legal moves
    opponent_moves = board.generate_legal_moves()
    for _ in opponent_moves:
        count += 1.0
        if board.turn == ps.BLACK:
            value += 1.0
        else: 
            value -= 1.0
    board.turn = not board.turn # reset turn to original
    
    value = mobility_weight * (value / count) # 0 if same number of moves
    return round(value, sig_figs) # Rounds due to floating point errors


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
    
    return round(value, sig_figs) # Rounds due to floating point errors


def evaluator(board : ps.Board, eval_flags):
    # eval_dic = { "count_material" : 1, "count_mobility" : 1,
    #              "checkmate_value" : 1, "king_safety" : 1}

    evaluation = 0
    if (eval_flags[0] == 1):
        evaluation += count_material(board)
    if (eval_flags[1] == 1):
        evaluation += count_mobility(board)
    if (eval_flags[2] == 1):
        evaluation += checkmate_value(board)
    if (eval_flags[3] == 1):
        radius = 1 # arbitrary radius
        evaluation += ks.king_safety(board, radius)

    return round(evaluation, sig_figs)
