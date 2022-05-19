
from collections import deque
from Board import Board

from bfs import subNode

GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
NodesExpanded = 0
maxSearch = 0
MaxFrontier = 0

def dfs(startState):

    global MaxFrontier, GoalNode, maxSearch

    nodesVisited = set()
    stack = list([Board(startState, None, None, 0, 0 ,0)])
    while stack:
        node = stack.pop()
        nodesVisited.add(node.map)
        if node.state == GoalState:
            GoalNode = node
            return stack
        numPath  = reversed(subNode(node))
        for path in numPath:
            if path.map not in nodesVisited:
                stack.append(path)
                nodesVisited.add(path.map)
                if path.depth > maxSearch:
                    maxSearch = 1 + maxSearch
        if len(stack) > MaxFrontier:
            MaxFrontier = len(stack)