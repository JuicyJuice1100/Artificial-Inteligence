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

def readFile(fileName):
    with open(fileName) as fileobj:
        for i, line in enumerate(fileobj):
            if(i == 0): # gets the starting point
                start = line
            elif(i == 1):
                finish = line #gets the goal point
                width = len(line) #gets the width of map
            else:  # reads the map
                for j, char in enumerate(line): #reads map char by char
                    #TODO: create a dictionary/json/turn map into an array
                    print (char)

def main():
    readFile(openFile())
    
main()