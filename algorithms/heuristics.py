import math
from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem, SearchProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem: SearchProblem):
    """
    The Manhattan distance heuristic.
    """
    # TODO: Add your code here
    XcoordState, YcoordState = state
    endState = problem.goal
    XcoordEnd, YcoordEnd = endState
    
    resultadoManhattan = abs(XcoordState-XcoordEnd)+abs(YcoordState-YcoordEnd)
    return resultadoManhattan


def euclideanHeuristic(state, problem: SearchProblem):
    """
    The Euclidean distance heuristic.
    """
    # TODO: Add your code here
    XcoordState, YcoordState = state
    endState = problem.goal
    XcoordEnd, YcoordEnd = endState
    
    resultadoEuclidian = math.sqrt(((XcoordState-XcoordEnd)**2)+((YcoordState-YcoordEnd)**2))
    return resultadoEuclidian


def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Your heuristic for the MultiSurvivorProblem.

    state: (position, survivors_grid)
    problem: MultiSurvivorProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider: distance to nearest survivor + MST of remaining survivors
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    # TODO: Add your code here
    utils.raiseNotDefined()
