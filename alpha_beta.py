import python_shogi.shogi as ps
import evaluator as evlt
import material_consts as mc
import generators as gens

def finale_alpha_beta(board : ps.Board,depth, maximizingplayer, 
                      alpha, beta, generator, evaluator, eval_flags):
    if (depth == 0 or board.is_game_over()):
        return [None,evaluator(board, eval_flags)]
    elif(maximizingplayer):
        max_value = float('-inf')
        best_move = ""
        moves = generator(board)

        try:
            next(generator(board))
            moves = generator(board)
        except StopIteration:
            moves = board.generate_legal_moves(board)

        for move in moves:
            current_move = move.usi()
            board.push_usi(current_move)
            evl = finale_alpha_beta(board, depth-1, False,alpha,beta, generator, evaluator, eval_flags)
            if (evl[1] > max_value):
                best_move = current_move
                max_value = evl[1]            
            board.pop()
            alpha = max(alpha,evl[1])
            if beta <= alpha:
                break

        return [best_move, max_value]
    else:
        min_value = float('inf')
        best_move = ""
        moves = generator(board)

        try:
            next(generator(board))
            moves = generator(board)
        except StopIteration:
            moves = board.generate_legal_moves(board)

        for move in moves:
            current_move = move.usi()
            board.push_usi(current_move)
            evl = finale_alpha_beta(board, depth-1,True,alpha,beta, generator, evaluator, eval_flags)
            if (evl[1] < min_value):
                min_value = evl[1]
                best_move = current_move
            board.pop()
            beta = min(beta,evl[1])
            if beta <= alpha:
                break
        return [best_move,min_value]


