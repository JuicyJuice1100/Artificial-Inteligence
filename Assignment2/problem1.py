from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search
from search import UndirectedGraph,GraphProblem,Graph,ManhattanProblem
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
                start = re.sub(r'[^1-9]', " ", line)
                start = map(int, start.split())
            elif(i == 1):
                finish = re.sub(r'[^1-9]', " ", line) #gets the goal point
                finish = map(int, finish.split())
            else:  # reads the map
                line = list(line)
                for j, char in enumerate(line): #reads map char by char
                    dictionary.update(createNode(i, j, int(char)))
    dictionary['start'] = start
    dictionary['finish'] = finish
    return dictionary

def createNode(i, j, char):
    return {(i - 2,j): char}

def createNeighborsHelper(i, j, dictionary):
    n = {}
    if(dictionary[(i-1, j)] != 0):
        n.update({(i-1, j): dictionary[i-1,j]})
    if(dictionary[(i, j-1)] != 0):
        n.update({(i, j-1): dictionary[(i, j-1)]})
    if(dictionary[(i+1, j)] != 0):
        n.update({(i+1, j): dictionary[(i+1, j)]})
    if(dictionary[(i, j+1)] != 0):
        n.update({(i, j+1): dictionary[(i, j+1)]})
    # n = {(i-1,j): dictionary[(i-1, j)], (i, j-1): dictionary[(i, j-1)], (i+1, j): dictionary[(i+1, j)], (i, j+1):dictionary[(i, j+1)]}
    return n

def createNeighbors(dictionary):
    copy = dictionary.copy()
    for key, value in dictionary.items():
        if(value > 0):
            copy[key] = createNeighborsHelper(key[0], key[1], dictionary)
        else:
            copy.pop(key)
    return copy

def graphHelper():
    dictionary = {}
    dictionary = readFile(openFile(), dictionary)
    start = tuple(dictionary.pop('start'))
    goal = tuple(dictionary.pop('finish'))
    # goal = tuple((1,2))
    # dictionary = {k:v for k, v in dictionary.items() if v != 0}
    dictionary = createNeighbors(dictionary)
    return (start, goal, UndirectedGraph(dictionary))

def main():
    
    L1 = graphHelper()
    L2 = graphHelper()
    L3 = graphHelper()

    # TODO: use given utils to answer questions
    compare_searchers(problems=[InstrumentedProblem(ManhattanProblem(L1[0], L1[1], L1[2])), InstrumentedProblem(ManhattanProblem(L2[0], L2[1], L2[2])), InstrumentedProblem(ManhattanProblem(L3[0], L3[1], L3[2]))],
        header=['Algorithm', "L1", "L2", "L3"],
        searchers=[uniform_cost_search, greedy_best_first_graph_search, astar_search]
    )

    # compare_searchers(problems=[ManhattanProblem(start, goal, graph)],
    #     header=['Algorithm', "Problem 1"],
    #     searchers=[uniform_cost_search, greedy_best_first_graph_search, astar_search]
    # )
    
main()