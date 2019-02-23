#!/usr/bin/env python3
'''

    Author: Oscar Tovar

    First problem from the first problem set released by Christoph F. Eick
    that tackles various search strategies. The strategies are as follows:

     - breadth-first
     - depth-first
     - best-first (using f == h)
     - A* (using f = g + h)
     - SMA* (using f = g + h and limiting the open-list to just 3 elements)
    
    The problem uses a graph that has a start state, labeled S, and two goal states, G1 and G2.

    The following is a representation of the states:
       Format -> State: State:Cost...
     - S: A:3, F:2, B:7
     - A: C:1, D:6
     - F: D:4
     - B: E:1, G2:9
     - C: S:2, D:4
     - D: G1:6, B:3
     - E: G2:5, H:1
     - H: G2:1
     - G1: Final
     - G2: Final
    
'''
from data_structures import Queue

class State:
    def __init__(self, name, distance):
        self.name = name
        self.reachable = Queue() # Queue full of neighbors that can be reached
        self.estimate = distance # Estimated cost to nearest goal

    def insert(self, state, distance):
        self.reachable.insert(state)

'''
    Define the open and closed lists here.
'''

OPEN = list()
CLOSED = list()

def setup():
    while len(OPEN) > 0:
        OPEN.pop()
    while len(CLOSED) > 0:
        CLOSED.pop()

    OPEN.append(S)

def breadthFirstSearch():
    while (len(OPEN) > 0):
        currentState = OPEN.pop()
        # print("Adding " + currentState.name + " to CLOSED")
        if (currentState.name == "G1" or currentState.name == "G2"):
            return currentState.name
        else:
            CLOSED.append(currentState.name)
            i = 0
            neighbors = currentState.reachable.getList()
            while (i < len(neighbors)):
                state = neighbors[i]
                i += 1
                if (state in CLOSED or state in OPEN):
                    continue
                else:
                    # OPEN.append(state)
                    # print("Adding " + state.name + " to OPEN")
                    OPEN.insert(0, state)
    return "FAILURE"
            
def depthFirstSearch(open):
    for state in OPEN:
        currentState = OPEN.pop(0)

        if (currentState.name == "G1" or currentState.name == "G2"):
            CLOSED.append(currentState.name)
            return CLOSED
        else:
            CLOSED.append(currentState.name)
            i = 0
            neighbors = currentState.reachable.getList()
            while (i < len(neighbors)):
                state = neighbors[i]
                i += 1
                if (state in CLOSED or state in OPEN):
                    continue
                else:
                    OPEN.append(state)
    return "FAILURE"

# def bestFirstSearch(open):
#     pass

# def AStar(open):
#     pass

# def SMAStar(open):
#     pass

if __name__ == "__main__":
    '''
        Define all the states here.
    '''

    S = State("S", 10)

    A = State("A", 5)

    B = State("B", 8)

    C = State("C", 3)

    D = State("D", 2)

    E = State("E", 4)

    F = State("F", 9)

    # Goal nodes
    G1 = State("G1", 0)
    G2 = State("G2", 0)

    H = State("H", 2)

    S.insert(A, 3)
    S.insert(B, 7)
    S.insert(F, 2)
    A.insert(C, 1)
    A.insert(D, 6)

    F.insert(D, 4)

    B.insert(E, 1)
    B.insert(G2, 9)

    C.insert(D, 4)
    C.insert(S, 2)

    D.insert(B, 3)
    D.insert(G1, 6)

    E.insert(G2, 5)
    E.insert(H, 1)

    H.insert(G2, 1)

    # Perform the search algorithms
    print("Solving the problem using the following search algorithms:\n")
    print("Breadth First...")
    setup()
    solution = breadthFirstSearch()
    print("Goal Reached: " + str(solution))
    print("States Expanded: " + str(CLOSED))

    print("Depth First")
    setup()
    # depthFirstSearch()
    # bestFirstSearch()
    # AStar()
    # SMAStar()
    print("Best First")
    print("A*")
    print("SMA*")