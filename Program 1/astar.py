from Board import Board
from DFS import GoalNode, MaxFrontier
from bfs import subNode

#the distance to the root
MaxSearch = 0
GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
board_0 = [0,1,2,1,2,3,2,3,4]
board_1 = [1,0,1,2,1,2,3,2,3]
board_2 = [2,1,0,3,2,1,4,3,2]
board_3 = [1,2,3,0,1,2,1,2,3]
board_4 = [2,1,2,1,0,1,2,1,2]
board_5 = [3,2,1,2,1,0,3,2,1]
board_6 = [2,3,4,1,2,3,0,1,2]
board_7 = [3,2,3,2,1,2,1,0,1]
board_8 = [4,3,2,3,2,1,2,1,0]

def heuristic(node):

    global board_0, board_1, board_2, board_3, board_4, board_5, board_6, board_7, board_8
    n0 = board_0[node.index('0')]
    n1 = board_1[node.index('1')]
    n2 = board_2[node.index('2')]
    n3 = board_3[node.index('3')]
    n4 = board_4[node.index('4')]
    n5 = board_5[node.index('5')]
    n6 = board_6[node.index('6')]
    n7 = board_7[node.index('7')]
    n8 = board_8[node.index('8')]
    HeuristicTotal = n0 + n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
    return HeuristicTotal
    


def ast(startState):
    global MaxSearch, GoalNode

    nodesVisted = set()
    Queue = []
    h1 = ''
    for position in startState:
        h1 = h1 + str(position)

    key = heuristic(h1)
    Queue.append(Board(startState, None, None, 0, 0, key))
    nodesVisted.add(h1)

    while Queue:
        Queue.sort(key=lambda j: j.key)
        node = Queue.pop(0)
        if node.state == GoalState:
            GoalNode = node
            return Queue
        numPath = subNode(node)
        for path in numPath:
            currPath = path.map[:]
            if currPath not in nodesVisted:
                key = heuristic[path.map]
                path.key = key + path.depth
                Queue.append(path)
                nodesVisted.add(path.map[:])
                if path.depth > MaxSearch:
                    MaxSearch = 1 + MaxSearch
