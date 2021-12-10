import python_shogi.shogi as ps
import collections

def read_moves(filename) -> collections.deque:
    moves = collections.deque()
    with open(filename) as f:
        for line in f:
            moves.append(line.rstrip())
    return moves


class Analyze:

    def __init__(self):
        self.board = ps.Board()
        pass

    def load_moves(self, filename):
        for move in read_moves(filename):
            self.board.push_usi(move)
    
    def perform_analysis(self, filename):
        moves = read_moves(filename)
        quit = False
        while(not quit):
            print(self.board)
            print("Input: (N)ext\n" + 
                  "       (B)ack\n" +
                  "       (Q)uit\n" )
            inpt = input("Enter input: ")
            inpt = inpt.lower()
            if inpt == "n":
                move = moves.popleft()
                self.board.push_usi(move)
            elif inpt == "b":
                move = self.board.pop().usi()
                moves.appendleft(move)
            elif inpt == "q":
                quit = True
            else:
                print("INVALID INPUT, TRY AGAIN")


def main():
    while(True):
        filename = input("Enter a Game File Name (Q to quit): ")
        if filename.lower() == "q":
            break
        try:
            read_moves(filename)
        except FileNotFoundError:
            print("File Not Found -- Try again")

        analysis = Analyze()
        analysis.perform_analysis(filename)

if __name__ == "__main__":
    main()
