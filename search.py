# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    use a stack to store each state
    """
    # create priority queue with cost function
    RoutePQ = util.Stack()

    # push initial state tuple:(position, list:Route)
    tuStart = problem.getStartState()
    RoutePQ.push((tuStart, []))

    # call genericSearch with problem and data structure
    return genericSearch(problem, RoutePQ)

def breadthFirstSearch(problem):
    """
    use a queue to store each state
    """
    # create priority queue with cost function
    RoutePQ = util.Queue()

    # push initial state tuple:(position, list:Route)
    tuStart = problem.getStartState()
    RoutePQ.push((tuStart, []))

    # call genericSearch with problem and data structure
    return genericSearch(problem, RoutePQ)

def uniformCostSearch(problem):
    """
    uniform cost function = cost of previous action
    """
    # define costFunction
    def costFunction(tuState):
        return problem.getCostOfActions(tuState[1])

    # create priority queue with cost function
    RoutePQ = util.PriorityQueueWithFunction(costFunction)

    # push initial state tuple:(position, list:Route)
    tuStart = problem.getStartState()
    RoutePQ.push((tuStart, []))

    # call genericSearch with problem and data structure
    return genericSearch(problem, RoutePQ)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def genericSearch(problem, dataStructure):
    """
    generic search function by any given data structure
    """

    # a set to store explored position
    setExplored = set()

    # begin search
    while dataStructure.isEmpty() is False:
        tuRoute = dataStructure.pop()

        # return path if popped state is the goal
        if problem.isGoalState(tuRoute[0]):
            return tuRoute[1]

        if tuRoute[0] not in setExplored:
            setExplored.add(tuRoute[0])
            for tuState in problem.getSuccessors(tuRoute[0]):
                # push tuple:(current position, list of route adding latest direction)
                dataStructure.push((tuState[0], tuRoute[1] + [tuState[1]]))
    return []

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    aStar search find a path with least cost
    cost function = cost of previous action + heuristic function of current position to goal
    """
    # define costFunction
    def costFunction(tuState):
        return problem.getCostOfActions(tuState[1]) + heuristic(tuState[0], problem)

    # create priority queue with cost function
    RoutePQ = util.PriorityQueueWithFunction(costFunction)

    # push initial state tuple:(position, list:Route)
    tuStart = problem.getStartState()
    RoutePQ.push((tuStart, []))

    # call genericSearch with problem and data structure
    return genericSearch(problem, RoutePQ)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
