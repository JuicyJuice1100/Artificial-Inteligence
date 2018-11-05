from search import Problem
from csp import backtracking_search, no_inference, forward_checking, mac
from csp import first_unassigned_variable,mrv,num_legal_values,unordered_domain_values,lcv
from csp import CSP,usa,france,australia,NQueen,UniversalDict
from collections import Counter

import tkinter as tk
from tkinter import filedialog

import itertools

def openFile():
    root = tk.Tk()
    root.withdraw()

    return filedialog.askopenfilename()

def readFile(fileName, dictionary):
    
    with open(fileName) as fileobj:
        createRows(fileobj, dictionary)
        
    createColumns(dictionary, len(dictionary))

def createRows(file, dictionary):
    # rows = {}
    for i, line in enumerate(file):
        row = []
        line = line.rstrip()
        for char in line:
            if(char == '-'):
                row.append(2) # 2 = '-'
            else:
                row.append(int(char))
        dictionary['r' + str(i)] = row
    # dictionary['Rows'] = rows # 0 = row

def createColumns(dictionary, length):
    temp = dictionary.copy()
    for i in range(0, length):
        column = []
        for value in temp.values():
            column.append(value[i])
        dictionary['c' + str(i)] = column
    # dictionary['Columns'] = columns # 1 = columns

def filterUnaryConstraints(domains):
    return {item for item in domains if not (any(len(list(group)) > 2 for k, group in itertools.groupby(item))) and (item.count(1) == item.count(0))}

def createDictionaryWithKeys(dictionary):
    keyDictionary = {}
    for key, value in enumerate(dictionary):
        keyDictionary[key] = value
    return keyDictionary

def createNeighbors(dictionary, length):
    neighbors = {}
    for key in list(dictionary.keys())[:length]:
        neighbors[key] = {k for k in list(dictionary)[:length] if k != key}
    for key in list(dictionary.keys())[length:]:
        neighbors[key] = {k for k in list(dictionary)[length:] if k != key}
    return neighbors

def createDomain(dictionary, domains):
    temp = dictionary.copy()
    for key, value in temp.items():
        temp[key] = {domain for domain in domains if shrinkDomain(value, domain)}
    return temp

def shrinkDomain(value, domain):
    for i, j in enumerate(value):
        if(j != 2):
            if(j != domain[i]):
                return False
    return True

def constraints(A, a, B, b):
    if(A[0] == B[0]):
        return a != b


def printAnswer(result, length):
    for i in range(0, length):
        for j in result['r' + str(i)]:
            print(j, end='')
        print()

def main():
    dictionary = {}
    readFile(openFile(), dictionary)
    length = int(len(dictionary)/2)
    domains = filterUnaryConstraints({i for i in itertools.product([0, 1], repeat=length)})
    neighbors = createNeighbors(dictionary,length)
    dictionary = createDomain(dictionary, domains)

    # setRowDomains(dictionary['Rows'])
    # domain = UniversalDict(domain)

    problem = CSP(list(dictionary.keys()), dictionary, neighbors, constraints)
    result = backtracking_search(problem,select_unassigned_variable=mrv,order_domain_values=lcv,inference=mac) 
    printAnswer(result, length)

main()
