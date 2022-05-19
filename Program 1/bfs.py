
from collections import deque
from Board import Board
from Board import neighbors

GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
NodesExpanded = 0
maxFrontier = 0

def bfs(startState):

    global maxFrontier, GoalNode, maxSearch

    boardVisited = set()
    Queue = deque([Board(startState, None, None, 0, 0, 0)])

    while Queue:
        node = Queue.popleft()
        boardVisited.add(node.map)
        if node.state == GoalState:
            GoalNode = node
            return Queue
        numPath = subNode(node)
        for path in numPath:
            if path.map not in boardVisited:
                Queue.append(path)
                boardVisited.add(path.map)
                if path.depth > maxSearch:
                    maxSearch = maxSearch + 1
        if len(Queue) > maxFrontier:
            QueueSize = len(Queue)
            maxFrontier = QueueSize

def subNode(node):
        
    global NodesExpanded
    NodesExpanded = NodesExpanded + 1

    nextMov = []
    nextMov.append(Board(neighbors(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))
    nextMov.append(Board(neighbors(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))
    nextMov.append(Board(neighbors(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))
    nextMov.append(Board(neighbors(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))
    nodes=[]
    for nextPaths in nextMov:
        if(nextPaths.state!=None):
            nodes.append(nextPaths)
        return nodes