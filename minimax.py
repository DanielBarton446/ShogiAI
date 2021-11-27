import python_shogi.shogi as ps
import alpha_beta as ab
import material_consts as mc
import random



def minimax(board : ps.Board,depth, maximizingplayer):
    if (depth == 0 or board.is_game_over()):
        return ab.evaluator(board);
    elif(maximizingplayer):
        max_value = -100000;
        moves = board.generate_legal_moves();
        for move in moves:
            board.push_usi(move.usi());
            eval = minimax(board, depth-1, False);
            max_value = max(max_value, eval);
            board.pop();
        return max_value;
    else:
        min_value = 100000;
        moves = board.generate_legal_moves();
        for move in moves:
            board.push_usi(move.usi());
            eval = minimax(board, depth-1,True);
            min_value = min(min_value,eval);
            board.pop();
        return min_value;



def minimax_2(board : ps.Board,depth, maximizingplayer):
    if (depth == 0 or board.is_game_over()):
        return [None,ab.evaluator(board)];
    elif(maximizingplayer):
        max_value = -100000;
        best_move = "";
        moves = board.generate_legal_moves();
        for move in moves:
            current_move = move.usi();
            board.push_usi(current_move);
            eval = minimax_2(board, depth-1, False);
            if (eval[1] > max_value):
                best_move = current_move;
                max_value = eval[1];
            board.pop();
        return [best_move, max_value];
    else:
        min_value = 100000;
        best_move = "";
        moves = board.generate_legal_moves();
        for move in moves:
            current_move = move.usi();
            board.push_usi(current_move);
            eval = minimax_2(board, depth-1,True);
            if (eval[1] < min_value):
                min_value = eval[1];
                best_move = current_move;
            board.pop();
        return [best_move,min_value];



board = ps.Board();
print(minimax_2(board,3,True));