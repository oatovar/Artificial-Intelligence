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
        self.costs = list()
        self.estimate = distance # Estimated cost to nearest goal

    # TODO implement the usage of the distance cost.
    # Refactoring will be necessary.
    def insert(self, state, distance):
        self.reachable.insert(state)
        self.costs.append(distance)

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

def printOpen():
    result = "["
    for state in OPEN:
        result += "'" + str(state.name) + "', "
    result = result[:-2] + "]"
    return result

def printClosed():
    result = "["
    for state in CLOSED:
        result += "'" + str(state.name) + "', "
    result = result[:-2] + "]"
    return result

# Needs to be fixed.
def sortByHeuristic(states):
    # Uses selection sort to sort states by ascending estimate distance
    i = 0
    while (i < len(states)-1):
        min = i
        j = i + 1
        while (j < len(states)):
            if (states[j].estimate < states[i].estimate):
                min = j
            j+=1
        i+=1
        if (min != i):
            temp = states[min]
            states[min] = states[i]
            states[i] = temp

def sortforAStar(states, costs):
    # Take into account the cost to reach state
    # and the state's estimated cost to nearest goal.
    i = 0
    while (i < len(states)-1):
        min = i
        j = i + 1
        print(states[i].name)
        while (j < len(states)):
            print(str(states[j].estimate + costs[j]))
            print(str(states[i].estimate + costs[i]))
            if (states[j].estimate + costs[j])  < (states[i].estimate + costs[i]):
                min = j
            j+=1
        i+=1
        if (min != i):
            tempState = states[min]
            tempCost = costs[min]
            states[min] = states[i]
            states[i] = tempState
            costs[min] = costs[i]
            costs[i] = tempCost


def breadthFirstSearch():
    while (len(OPEN) > 0):
        # Remove from the front of the list since BFS uses FIFO
        currentState = OPEN.pop(0)
        if (currentState == G1 or currentState == G2):
            return currentState.name
        else:
            CLOSED.append(currentState)
            neighbors = currentState.reachable.getList()
            for neighbor in neighbors:
                if (neighbor in CLOSED or neighbor in OPEN):
                    # Skip any children that have already appeared in OPEN or CLOSED
                    continue
                else:
                    # Insert at the end since BFS uses a queue.
                    OPEN.append(neighbor)
    return "FAILURE"
            
def depthFirstSearch():
    while len(OPEN) > 0:
        # Remove the earliest entry of the list since DFS uses a Stack
        currentState = OPEN.pop(0)
        if (currentState == G1 or currentState == G2):
            # CLOSED.append(currentState.name)
            return currentState.name
        else:
            CLOSED.append(currentState)
            neighbors = currentState.reachable.getList()
            for neighbor in neighbors:
                if (neighbor in CLOSED or neighbor in OPEN):
                    continue
                else:
                    # Append to the end of the list since DFS uses a Stack
                    OPEN.insert(0, neighbor)
    return "FAILURE"
    

def bestFirstSearch():
    # Uses heurstic to make decisions
    # Similar to DFS uses a stack to make decisions.
    while len(OPEN) > 0:
        current_state = OPEN.pop(0)
        if (current_state == G1 or current_state == G2):
            return current_state.name
        else:
            CLOSED.append(current_state)
            neighbors = current_state.reachable.getList()
            sortByHeuristic(neighbors)
            for neighbor in neighbors:
                if (neighbor in OPEN or neighbor in CLOSED):
                    continue
                else:
                    OPEN.insert(0, neighbor)
    return "FAILURE"

def AStar():
    while (len(OPEN) > 0):
        # Requires the usage of the state.distance plus the cost
        # to travel to the that node as well. f(n) = g(n) + h(n)
        currentState = OPEN.pop(0)
        if (currentState == G1 or currentState == G2):
            return currentState.name
        else:
            CLOSED.append(currentState)
            neighbors = currentState.reachable.getList()
            costs = currentState.costs
            sortforAStar(neighbors, costs)
            for neighbor in neighbors:
                OPEN.insert(0, neighbor)
    return "FAILURE"

def SMAStar():
    while (len(OPEN) > 0):
        # Requires the usage of the state.distance plus the cost
        # to travel to the that node as well. f(n) = g(n) + h(n)
        # The OPEN list should also only hold the last three entries.
        currentState = OPEN.pop(0)
        if (currentState == G1 or currentState == G2):
            return currentState.name
        else:
            CLOSED.append(currentState)
            neighbors = currentState.reachable.getList()
            for neighbor in neighbors:
                OPEN.append(neighbor)
    return "FAILURE"

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

    # All nodes are inserted left to right according to the graph.

    S.insert(A, 3)
    S.insert(F, 2)
    S.insert(B, 7)

    A.insert(C, 1)
    A.insert(D, 6)

    F.insert(D, 4)

    B.insert(E, 1)
    B.insert(G2, 9)

    C.insert(S, 2)
    C.insert(D, 4)

    D.insert(G1, 6)
    D.insert(B, 3)

    E.insert(G2, 5)
    E.insert(H, 1)

    H.insert(G2, 1)

    # Perform the search algorithms
    print("Solving the problem using the following search algorithms:\n")
    print("Breadth First...")
    setup()
    OPEN.append(S)
    solution = breadthFirstSearch()
    print("Goal Reached: " + str(solution))
    print("States Expanded: " + printClosed())
    print("Open List: " + printOpen())
    print("Closed List: " + printClosed())
    # Print separating newline
    print
    print("Depth First")
    setup()
    solution = depthFirstSearch()
    print("Goal Reached: " + str(solution))
    print("States Expanded: " + printClosed())
    print("Open List: " + printOpen())
    print("Closed List: " + printClosed())
    print
    setup()

    print("Best First")
    solution = bestFirstSearch()
    print("Goal Reached: " + str(solution))
    print("States Expanded: " + printClosed())
    print("Open List: " + printOpen())
    print("Closed List: " + printClosed())
    print

    print("A*")
    setup()
    solution = AStar()
    print("Goal Reached: " + str(solution))
    print("States Expanded: " + printClosed())
    print("Open List: " + printOpen())
    print("Closed List: " + printClosed())
    print

    print("SMA*")