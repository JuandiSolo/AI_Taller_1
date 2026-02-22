from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic
from algorithms.utils import Stack, Queue, PriorityQueue


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    stack = Stack()
    start = problem.getStartState()
    stack.push((start, []))
    visited = set()

    while not stack.isEmpty():
        state, path = stack.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.add(state)
            for successor, action, _ in problem.getSuccessors(state):
                if successor not in visited:
                    new_path = path + [action]
                    stack.push((successor, new_path))

    return []


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # TODO: Add your code here
    buttocks = Queue()
    start = problem.getStartState()
    buttocks.push((start, []))
    visited = set()
    while not buttocks.isEmpty():
        state, path = buttocks.pop()
        if problem.isGoalState(state):
            return path
        if state not in visited:
            visited.add(state)
            for successor, action, _ in problem.getSuccessors(state):
                if successor not in visited:
                    new_path = path + [action]
                    buttocks.push((successor, new_path))
    return []


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    # TODO: Add your code here
    inicial = problem.getStartState()
    visitados = set()
    costos = {inicial:0}
    caminos = {inicial:[]}
    pq = utils.PriorityQueue()
    pq.push(inicial, 0)
    while pq.isEmpty() == False:
        nodoActual= pq.pop()
        if nodoActual in visitados:
            continue
        costo1 = costos[nodoActual] 
        if problem.isGoalState(nodoActual):
            return caminos[nodoActual]
        lista = problem.getSuccessors(nodoActual)
        for nodo, accion, costo2 in lista:
            nuevoCosto = costo1 + costo2
            if nodo not in costos or costos[nodo] > nuevoCosto:
                pq.push(nodo, nuevoCosto)
                costos[nodo] = nuevoCosto
                caminos [nodo] = caminos[nodoActual] + [accion]
    return []


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    coordenadaInicial = problem.getStartState()

    structure = {
        "source": coordenadaInicial,
        "visited": {},
        "pq": utils.PriorityQueue(),
    }
    pesoStart = heuristic(coordenadaInicial, problem)
    value = {"marked": True, "edge_to": None, "dist_to": pesoStart, "direction": None}
    structure["visited"][coordenadaInicial] = value
    structure["pq"].push(coordenadaInicial, pesoStart)
    coordFinal = None
    while coordFinal == None and structure["pq"].isEmpty() == False:
        coordActual = structure["pq"].pop()
        coordFinal = scanAStar(problem, structure, coordActual, coordFinal, heuristic)
    listaInstrucciones = []
    vertex_inicial = structure["visited"][coordFinal]
    while vertex_inicial and vertex_inicial["direction"] != None:
        listaInstrucciones.append(vertex_inicial["direction"])
        vertex_inicial = structure["visited"][vertex_inicial["edge_to"]]
    listaInstrucciones.reverse()
    return listaInstrucciones


def scanAStar(problem: SearchProblem, structure, coordActual, coordFinal, heuristic):
    listaSucesoresInicial = problem.getSuccessors(coordActual)
    for nodoHijoActual in listaSucesoresInicial:
        coordenadaHijoActual, Dirección, PesoActual = nodoHijoActual
        if problem.isGoalState(coordenadaHijoActual):
            coordFinal = coordenadaHijoActual
        pesoOrigen = structure["visited"][coordActual]["dist_to"]
        pesoHeuristic = heuristic(coordenadaHijoActual, problem)
        pesoPq = PesoActual + pesoOrigen
        pesoTotal = pesoPq + pesoHeuristic
        if structure["visited"].get(coordenadaHijoActual) == None:
            value = {
                "marked": True,
                "edge_to": coordActual,
                "dist_to": pesoPq,
                "direction": Dirección,
            }
            structure["pq"].push(coordenadaHijoActual, pesoTotal)
            structure["visited"][coordenadaHijoActual] = value
        else:
            distToActual = structure["visited"][coordenadaHijoActual]["dist_to"]
            if distToActual > pesoTotal:
                value = {
                    "marked": True,
                    "edge_to": coordActual,
                    "dist_to": pesoPq,
                    "direction": Dirección,
                }
                structure["visited"][coordenadaHijoActual] = value
                structure["pq"].update(coordenadaHijoActual, pesoTotal)
    return coordFinal


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
# dijk = dijkstra
