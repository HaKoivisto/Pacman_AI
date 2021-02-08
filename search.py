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
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
 

    # We create a stack to store information about the routes explored and
    # set to contain all the explored nodes.
    mStack = util.Stack()
    closed = set()

    # We set the starting node and placeholder for routes
    statestart = problem.getStartState()
    mStack.push((statestart,[]))
    

    while not mStack.isEmpty():

        # We get the most recently pushed item from the stack
        node, route = mStack.pop()

        # If the node is goal state
        if problem.isGoalState(node):
            return route

        # If note hasn't been visited yet, we explore its successors and 
        # add them to the stack
        if node not in closed:
            closed.add(node)
            for state, move, cost in problem.getSuccessors(node):
                if not state in closed:
                        mStack.push((state, route + [move]))



    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    # This time we used FIFO queue instead of LIFO stack. Explored nodes are also
    # stored in a list istead of set as it is easier to hande outside the function 
    # in the harder questions.
    mQueue = util.Queue()
    closed = []

    # Setting starting state/node and adding placeholders for routes and cost.
    statestart = problem.getStartState()
    mQueue.push((statestart,[],0))

    # Basically very similar implementation of handling queue as in DFS, but 
    # cost is a new parameter used.
    while not mQueue.isEmpty():
        node, route, cost = mQueue.pop()

        if problem.isGoalState(node):
            return route

        if node not in closed:
            closed.append(node)
            for state, move, addedcost in problem.getSuccessors(node):
                newcost = cost+addedcost
                if not state in closed:
                    mQueue.push((state, route + [move], newcost))


    util.raiseNotDefined()

def uniformCostSearch(problem):

    # This time we use priorityqueue. We also use set instead of list because this 
    # search method wasn't used in the harder questions so we could keep it as it is.
    mpQueue = util.PriorityQueue()
    closed = set()

    # Compared to BFS, we store similar values to the queue but adding a second
    # parameter to update queue by the costs.
    statestart = problem.getStartState()
    mpQueue.push((statestart,[],0),0)

    while not mpQueue.isEmpty():
        node, route, cost = mpQueue.pop()

        if problem.isGoalState(node):
            return route

        if node not in closed:
            closed.add(node)
            for state, move, addedcost in problem.getSuccessors(node):
                newcost = cost + addedcost
                if not state in closed:
                    mpQueue.update((state, route + [move],newcost), newcost)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """

    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # Again we start by selecting queue and making a list for visited nodes. We tried to 
    # complete this assignment with using priorityqueue with function but we were 
    # unable to get the update mathod to work as we would have wanted. So instead we 
    # calculate the heuristic inside the searchmethod and update the queue as in UCS.

    mpfQueue = util.PriorityQueue()
    closed = []
    
    # Start values and placeholders for node, route, cost and heuristic
    heurstart = heuristic(problem.getStartState(),problem)
    statestart = problem.getStartState()
    mpfQueue.push((statestart,[],0),heurstart)

    while not mpfQueue.isEmpty():
        node, route, cost = mpfQueue.pop()
        if problem.isGoalState(node):
            return route

        if node not in closed:
            closed.append(node)
            for state, move, addedcost in problem.getSuccessors(node):
                newcost = cost + addedcost
                heur = newcost + heuristic(state,problem) # Calculated heur. value for priorityqueue
                if not state in closed:
                    mpfQueue.update((state, route + [move], newcost), heur)


    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
