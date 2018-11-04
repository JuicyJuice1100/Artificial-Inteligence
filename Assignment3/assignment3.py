from search import Problem
from csp import backtracking_search, no_inference, forward_checking, mac
from csp import first_unassigned_variable,mrv,num_legal_values,unordered_domain_values,lcv
from csp import CSP,usa,france,australia,NQueen,UniversalDict
import tkinter as tk
from tkinter import filedialog

def openFile():
    root = tk.Tk()
    root.withdraw()

    return filedialog.askopenfilename()

def readFile(fileName, variable):
    
    with open(fileName) as fileobj:
        createRows(fileobj, variable)
        
    createColumns(variable)

def createRows(file, variable):
    rows = {}
    for i, line in enumerate(file):
        row = []
        line = line.rstrip()
        for char in line:
            if(char == '-'):
                row.append(2) # 2 = '-'
            else:
                row.append(int(char))
        rows[i] = row
    variable[0] = rows # 0 = row

def createColumns(variable):
    columns = {}
    for i in range(0, len(variable[0])):
        column = []
        for value in variable[0].values():
            column.append(value[i])
        columns[i] = column
    variable[1] = columns # 1 = columns

def main():
    variable = {}
    readFile(openFile(), variable)
    print(variable)

main()