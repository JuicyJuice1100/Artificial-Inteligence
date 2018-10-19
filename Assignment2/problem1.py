from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search
from search import UndirectedGraph,GraphProblem,Graph
from search import InstrumentedProblem,compare_searchers
from search import uniform_cost_search,greedy_best_first_graph_search,astar_search
from utils import Dict,euclidean
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
                start = line
            elif(i == 1):
                finish = line #gets the goal point
            else:  # reads the map
                line = list(line)
                # width = len(line) #gets the width of map
                for j, char in enumerate(line): #reads map char by char
                    # if(j < width):
                    dictionary.update(createNode(i, j, char))
    dictionary['start'] = start
    dictionary['finish'] = finish
    return dictionary

def createNode(i, j, char):
    return {(i - 2,j): char}

def createNeighborsHelper(i, j, dictionary):
    n = {(i-1,j): dictionary[(i-1, j)], (i, j-1): dictionary[(i, j-1)], (i+1, j): dictionary[(i+1, j)], (i, j+1):dictionary[(i, j+1)]}
    return n

def createNeighbors(dictionary):
    copy = dictionary.copy()
    for key, value in dictionary.items():
        print(value)
        if(key == 'start' or key == 'finish'):
            copy[key] = value
        elif(int(value) > 0):
                copy[key] = createNeighborsHelper(key[0], key[1], dictionary)
    return copy

def main():
    dictionary = {}
    dictionary = readFile(openFile(), dictionary)
    dictionary = createNeighbors(dictionary)
    
    print(dictionary)
    
main()