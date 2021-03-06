import Agent as a
import game as gm 
import generators as gens
import python_shogi.shogi as ps

def simulate_games():
    game_count = 99
    # Adjust these as needed
    board = ps.Board()
    eval_flags_black = [1,1,1,1]
    eval_flags_white = [1,1,1,1]
    agent1 = a.AlphaBetaAgent(gens.generate_qualifying_moves, 3, eval_flags_black)
    agent2 = a.AlphaBetaAgent(gens.generate_attacking_moves, 3, eval_flags_white)
    for _ in range(game_count):
        # record game stats by default. 
        board = ps.Board()
        gm.play_game(board, agent1, agent2)
    

def process_stats():
    try:
        with open("all_Ai_games_stats.txt") as fl:
            match_history = [0,0]
            for line in fl:
                match = line.split(",")
                match_history[0] += int(match[0])
                match_history[1] += int(match[1])
        print("Match History [agent1, agent2]: " + str(match_history))
    except FileNotFoundError:
        print("FILE NOT FOUND")



def main():
    simulate_games()
    while(True):
        inpt = input("Would you like to process stats?")
        if inpt.lower() == "y":
            process_stats()
        elif inpt.lower() == "n":
            break
        else:
            print("INVALID INPUT. (Y/N)")


if __name__ == "__main__":
    main()
