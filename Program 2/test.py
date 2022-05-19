import json
import sys
import numpy as np
import random


        
def main():
    print('Connect Four in Python', file=sys.stderr)
    for line in sys.stdin:
        print(line, file=sys.stderr)
        precept = json.loads(line)
        moves = valid_moves(precept)
        print(moves, file=sys.stderr)
        move = np.choice(moves)
        action = {'move': move}
        action_json = json.dumps(action)
        print(action_json, file=sys.stderr)
        print(action_json, flush=True)

if __name__ == '__main__':
    main()