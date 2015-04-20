
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
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
        Accion, stepCosto), where 'successor' is a successor to the current
        state, 'Accion' is the Accion required to get there, and 'stepCosto' is
        the incremental Costo of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfAccions(self, Accions):
        """
         Accions: A list of Accions to take

        This method returns the total Cost of a particular sequence of Accions.
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
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of Accions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    visitados = []
    cola = util.Stack()
    cola.push((problem.getStartState(), [], 0))
    while not cola.isEmpty():
        padre = cola.pop()
        if problem.isGoalState(padre[0]):
            return padre[1]
        elif padre[0] in visitados:
            continue
        else:
            hijos = problem.getSuccessors(padre[0]) #formato: ((x,y), direccion, 1)
            for hijo in hijos:
                if hijo[0] not in visitados:
                    cola.push((hijo[0], padre[1] + [hijo[1]], hijo[2] + padre[2]))
            visitados.append(padre[0])
    return []
                
                

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visitados = []
    cola = util.Queue()
    cola.push((problem.getStartState(), [], 0))
    while not cola.isEmpty():
        padreState, padreAccion, padreCosto = cola.pop()
        if problem.isGoalState(padreState):
            return padreAccion
        elif padreState in visitados:
            continue
        else:
            hijos = problem.getSuccessors(padreState)
            for hijoState, hijoAccion, hijoCosto in hijos:
                if hijoState not in visitados:
                    cola.push((hijoState, padreAccion + [hijoAccion], hijoCosto + padreCosto))
            visitados.append(padreState)
    return padreAccion
                
  

def uniformCostSearch(problem):
    """Search the node of least total Costo first."""
    "*** YOUR CODE HERE ***"
    return aStarSearch(problem) #es el mismo con la heuristica en null
    
        

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the Costo from the current state to the nearet
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined Costo and heuristic first."""
    "*** YOUR CODE HERE ***"
    visitados = []
    cola = util.PriorityQueue()
    start = problem.getStartState()
    cola.push((start, [], 0), 0)
    while not cola.isEmpty():
        padreState, padreAccion, padreCosto = cola.pop()
        if problem.isGoalState(padreState):
            return padreAccion
        elif padreState in visitados:
            continue
        else:
            hijos = problem.getSuccessors(padreState)
            for hijoState, hijoAccion, hijoCosto in hijos:
                if hijoState not in visitados:
                    gCosto = padreCosto + hijoCosto
                    hCosto = heuristic(hijoState, problem)
                    fCosto = gCosto + hCosto
                    cola.push((hijoState, padreAccion + [hijoAccion], gCosto), fCosto)
            visitados.append(padreState)
    return padreAccion
        

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


