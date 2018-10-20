from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search
from search import UndirectedGraph,GraphProblem,Graph
from search import InstrumentedProblem,compare_searchers
from search import uniform_cost_search,greedy_best_first_graph_search,astar_search
from utils import Dict,euclidean
import re
import tkinter as tk
from tkinter import filedialog


def openFile():
    root = tk.Tk()
    root.withdraw()

    return filedialog.askopenfilename()

def readFile(fileName, dictionary):
    with open(fileName) as fileobj:
        for i, line in enumerate(fileobj):
            line = line.rstrip()
            if(i == 0): # gets the starting point
                # start = re.sub(r'[^1-9]', " ", line)
                # start = map(int, start.split())
                start = line
            elif(i == 1):
                # finish = re.sub(r'[^1-9]', " ", line) #gets the goal point
                # finish = map(int, finish.split())
                finish = line
            else:  # reads the map
                line = list(line)
                for j, char in enumerate(line): #reads map char by char
                    dictionary.update(createNode(i, j, int(char)))
    dictionary['start'] = start
    dictionary['finish'] = finish
    return dictionary

def createNode(i, j, char):
    return {str((i - 2,j)): char}

def createNeighborsHelper(i, j, dictionary):
    n = {}
    if(dictionary[str((i-1, j))] != 0):
        n.update({(i-1, j): dictionary[i-1,j]})
    if(dictionary[str((i, j-1))] != 0):
        n.update({(i, j-1): dictionary[(i, j-1)]})
    if(dictionary[str((i+1, j))] != 0):
        n.update({(i+1, j): dictionary[(i+1, j)]})
    if(dictionary[str((i, j+1))] != 0):
        n.update({(i, j+1): dictionary[(i, j+1)]})
    # n = {(i-1,j): dictionary[(i-1, j)], (i, j-1): dictionary[(i, j-1)], (i+1, j): dictionary[(i+1, j)], (i, j+1):dictionary[(i, j+1)]}
    return n

def createNeighbors(dictionary):
    copy = dictionary.copy()
    for key, value in dictionary.items():
        if(value > 0):
            key = key.split()
            copy[key] = createNeighborsHelper(key[0], key[1], dictionary)
        else:
            copy.pop(key)
    return copy

def main():
    dictionary = {}
    dictionary = readFile(openFile(), dictionary)
    start = tuple(dictionary.pop('start'))
    goal = tuple(dictionary.pop('finish'))
    # goal = tuple((1,2))
    # dictionary = {k:v for k, v in dictionary.items() if v != 0}
    dictionary = createNeighbors(dictionary)
    graph = Graph(dictionary, directed=False)

    # TODO: use given utils to answer questions
    compare_searchers(problems=[GraphProblem(str(start), str(goal), graph)],
        header=['Algorithm', 'problem 1'],
        searchers=[uniform_cost_search]
    )
    
main()