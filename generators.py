import python_shogi.shogi as ps


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


def generate_qualifying_moves(board : ps.Board):
    # TODO: Chain multiple gennerators
    return generate_attacking_moves(board)




