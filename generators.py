import python_shogi.shogi as ps
from itertools import chain

def generate_legal_moves(board : ps.Board, generator, pawns=True, lances=True, 
            knights=True, silvers=True, golds=True,
            bishops=True, rooks=True,
            king=True,
            prom_pawns=True, prom_lances=True, prom_knights=True,
            prom_silvers=True, prom_bishops=True, prom_rooks=True,
            pawns_drop=True, lances_drop=True, knights_drop=True, 
            silvers_drop=True, golds_drop=True,
            bishops_drop=True, rooks_drop=True):
    return (move for move in generator(board,
                pawns, lances, knights, silvers, golds, bishops, rooks, king,
                pawns_drop, lances_drop, knights_drop, silvers_drop, golds_drop, bishops_drop, rooks_drop
            ) if not board.is_suicide_or_check_by_dropping_pawn(move))

def generate_attacking_moves(board : ps.Board,pawns=True, lances=True, 
            knights=True, silvers=True, golds=True,
            bishops=True, rooks=True,
            kings=True,
            prom_pawns=True, prom_lances=True, prom_knights=True,
            prom_silvers=True, prom_bishops=True, prom_rooks=True,
            pawns_drop=True, lances_drop=True, knights_drop=True, 
            silvers_drop=True, golds_drop=True,
            bishops_drop=True, rooks_drop=True):
    move_flags = [False,
                      pawns, lances, knights, silvers,
                      golds, bishops, rooks,
                      kings,
                      prom_pawns, prom_lances, prom_knights, prom_silvers,
                      prom_bishops, prom_rooks]

    drop_flags = [False,
                      pawns_drop, lances_drop, knights_drop, silvers_drop,
                      golds_drop, bishops_drop, rooks_drop]


    # Piece on Board move
    for piece_type in ps.PIECE_TYPES:
        if move_flags[piece_type]:
            movers = board.piece_bb[piece_type] & board.occupied[board.turn]
            from_square = ps.bit_scan(movers)

            while from_square != -1 and from_square is not None:
                # & board.occupied[~board.turn] is to check that 
                # all the attack moves are attacking enemy pieces. 
                moves = ps.Board.attacks_from(piece_type, from_square, 
                                              board.occupied, board.turn) \
                        & board.occupied[not board.turn]
                to_square = ps.bit_scan(moves)
                while to_square != -1 and to_square is not None:
                    if ps.can_move_without_promotion(to_square, piece_type, \
                                                     board.turn):
                        yield ps.Move(from_square, to_square)
                    if ps.can_promote(from_square, piece_type, board.turn):
                        yield ps.Move(from_square, to_square, True)
                    to_square = ps.bit_scan(moves, to_square + 1)
                from_square = ps.bit_scan(movers, from_square + 1)

    # Pieces in Hand dropping and attack enemy pieces
    moves = board.occupied.non_occupied()
    drop_sq = ps.bit_scan(moves)

    # Check having the piece in hand, can move after place
    # and double pawn
    # Also check if dropping move piece attacks enemy piece
    while drop_sq != -1 and drop_sq is not None:
        for piece_type in range(ps.PAWN, ps.KING):
            # Checks for Attacking Enemy Pieces
            attacks_material = False 
            if board.has_piece_in_hand(piece_type, board.turn):
                attacks = ps.Board.attacks_from(piece_type, drop_sq, 
                                    board.occupied, board.turn) \
                                    & board.occupied[not board.turn]

                attacking_squares = ps.bit_scan(attacks)
                if attacking_squares != -1:
                    attacks_material = True

            if drop_flags[piece_type] and \
                board.has_piece_in_hand(piece_type, board.turn) and \
                ps.can_move_without_promotion(drop_sq, piece_type, board.turn)\
                and not board.is_double_pawn(drop_sq, piece_type) \
                and attacks_material:

                yield ps.Move(None, drop_sq, False, piece_type)

        drop_sq = ps.bit_scan(moves, drop_sq + 1)

def generate_checking_moves(board : ps.Board,pawns=True, lances=True, 
            knights=True, silvers=True, golds=True,
            bishops=True, rooks=True,
            kings=True,
            prom_pawns=True, prom_lances=True, prom_knights=True,
            prom_silvers=True, prom_bishops=True, prom_rooks=True,
            pawns_drop=True, lances_drop=True, knights_drop=True, 
            silvers_drop=True, golds_drop=True,
            bishops_drop=True, rooks_drop=True):
    move_flags = [False,
                      pawns, lances, knights, silvers,
                      golds, bishops, rooks,
                      kings,
                      prom_pawns, prom_lances, prom_knights, prom_silvers,
                      prom_bishops, prom_rooks]

    drop_flags = [False,
                      pawns_drop, lances_drop, knights_drop, silvers_drop,
                      golds_drop, bishops_drop, rooks_drop]


    board_copy = ps.Board(board.sfen()) # Needed to view checks
    # Piece on Board move
    for piece_type in ps.PIECE_TYPES:
        if move_flags[piece_type]:
            movers = board.piece_bb[piece_type] & board.occupied[board.turn]
            from_square = ps.bit_scan(movers)

            while from_square != -1 and from_square is not None:
                # & board.occupied[~board.turn] is to check that 
                # all the attack moves are attacking enemy pieces. 
                moves = ps.Board.attacks_from(piece_type, from_square, 
                                              board.occupied, board.turn) \
                        & ~board.occupied[board.turn]
                to_square = ps.bit_scan(moves)
                while to_square != -1 and to_square is not None:
                    # reset board
                    board = ps.Board(board_copy.sfen()) # This is expensive
                    piece = board.piece_at(from_square)

                    board.remove_piece_at(from_square)
                    board.set_piece_at(to_square, piece)

                    board.turn = not board.turn
                    if board.is_check():
                        # must remove so can_move_without_promotion works as 
                        # intended
                        board.remove_piece_at(to_square, False)
                        # reset turn to appropriate turn
                        board.turn = not board.turn
                        if ps.can_move_without_promotion(to_square, piece_type, \
                                                         board.turn):
                            yield ps.Move(from_square, to_square)
                        if ps.can_promote(from_square, piece_type, board.turn):
                            yield ps.Move(from_square, to_square, True)
                    else:
                        board.turn = not board.turn

                    to_square = ps.bit_scan(moves, to_square + 1)
                from_square = ps.bit_scan(movers, from_square + 1)

    # Pieces in Hand dropping and attack enemy pieces
    drop_moves = board.occupied.non_occupied()
    drop_sq = ps.bit_scan(drop_moves)

    # Check having the piece in hand, can move after place
    # and double pawn
    # Also check if dropping move piece attacks enemy piece
    while drop_sq != -1 and drop_sq is not None:
        for piece_type in range(ps.PAWN, ps.KING):
            # Checks for Attacking Enemy Pieces
            attacks = ps.Board.attacks_from(piece_type, drop_sq, 
                                    board.occupied, board.turn) \
                                    & ~board.occupied[board.turn]
            attacked_square = ps.bit_scan(attacks)
            while attacked_square != -1 and attacked_square is not None:
                if drop_flags[piece_type] and \
                    board.has_piece_in_hand(piece_type, board.turn) and \
                    ps.can_move_without_promotion(drop_sq, piece_type, board.turn)\
                    and not board.is_double_pawn(drop_sq, piece_type) \
                    and attacked_square == board.king_squares[not board.turn]:
                        yield ps.Move(None, drop_sq, False, piece_type)

                attacked_square = ps.bit_scan(attacks, attacked_square + 1)

        drop_sq = ps.bit_scan(drop_moves, drop_sq + 1)




def generate_legal_moves_in_check(board : ps.Board):
    if (board.is_check()):
        yield from board.generate_legal_moves()
    else: #stop iteration without yielding, but maintain as generator.
        return
        yield

def generate_tsume_moves(board : ps.Board):
    tsume_generator = generate_checking_moves
    generator = chain(generate_legal_moves(board, tsume_generator), \
                      generate_legal_moves_in_check(board))
    return generator


def generate_qualifying_moves(board : ps.Board):
    attacking_gen = generate_attacking_moves
    tsume_gen = generate_tsume_moves
    generator = chain(tsume_gen(board),
                      generate_legal_moves(board, attacking_gen),
                      generate_legal_moves_in_check(board))
    return generator




