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
    def __init__(self, transitions, distance):
        self.reachable = Queue(transitions) # Queue full of neighbors that can be reached
        self.estimate = distance # Estimated cost to nearest goal
    
def depthFirstSearch():
    pass

if __name__ == "__main__":
    '''
        Define all the states here.
    '''
    S = State(
        [
            {"A": 3},
            {"F": 2},
            {"B": 7}
        ],
        10
    )

    A = State(
        [
            {"C": 1},
            {"D": 6}
        ],
        5
    )

    F = State(
        [
            {"D": 4}
        ],
        9
    )

    B = State(
        [
            {"E": 1},
            {"G2": 9}
        ],
        8
    )

    C = State(
        [
            {"S": 2},
            {"D": 4}
        ],
        3
    )

    D = State(
        [
            {"G1": 6},
            {"B": 3}
        ],
        2
    )

    E = State(
        [
            {"G2": 5},
            {"H": 1}
        ],
        4
    )

    H = State(
        [
            {"G2": 1}
        ],
        2
    )

    G1 = State(
        [
            {"G1": 0}
        ],
        0
    )

    G2 = State(
        [
            {"G2": 0}
        ],
        0
    )

    print("Solving the problem using the following search algorithms:")
    print("Breadth First...")
    print("Depth First")
    print("Best First")
    print("A*")
    print("SMA*")