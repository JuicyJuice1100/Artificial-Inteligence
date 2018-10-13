"""
V1.0
"""
from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search

#______________________________________________________________________________
#An implementation of the  Family Raft Problem
# Tuple format = [<Node (isPoliceAcross, isThiefAcross, isMomAcross, isDadAcross, numberOfSonsAcross, numberOfGirlsAcross, isBoatAcross)>]
class Problem1(Problem):
    #state is a tuple(P, T, M, D, S, G, B) with initial value (0, 0, 0, 0, 0, 0, 0)
    #all value flips between 1(R) and 0(L) except for S & G.  They are an int from between 0-2 inclusive stating how many are on the right.
    P=0; T=1; M=2; D=3; S=4; G=5; B=6 #class "constants"
    
    def __init__(self, goal):
        self.initial = (0,0,0,0,0,0,0)
        self.goalState = goal
    
    def actions(self, state):
        #actions are simply the result states possible in this example
        list=[]
        if state[Problem1.B]: #boat is on right
            #PTL - move Policeman & Thief left
            newState = (state[Problem1.P]-1,state[Problem1.T]-1,state[Problem1.M],state[Problem1.D],state[Problem1.S],state[Problem1.G],0)
            if self.validate(newState):
                list.append(newState)
                
            #MGL - move Mom and 1 daughter Left
            newState = (state[Problem1.P],state[Problem1.T],state[Problem1.M]-1,state[Problem1.D],state[Problem1.S],state[Problem1.G]-1,0)
            if self.validate(newState):
                list.append(newState)   
                
            #DSL - move Dad and 1 son left
            newState = (state[Problem1.P],state[Problem1.T],state[Problem1.M],state[Problem1.D]-1,state[Problem1.S]-1,state[Problem1.G],0)
            if self.validate(newState):
                list.append(newState)
                
            #MDL - move Mom and Dad
            newState = (state[Problem1.P],state[Problem1.T],state[Problem1.M]-1,state[Problem1.D]-1,state[Problem1.S],state[Problem1.G],0)
            if self.validate(newState):
                list.append(newState)     
                
            #PTL -  move Policeman & Mom
            newState = (state[Problem1.P]-1,state[Problem1.T],state[Problem1.M]-1,state[Problem1.D],state[Problem1.S],state[Problem1.G],0)
            if self.validate(newState):
                list.append(newState)   
            
            #PDL -  move Policeman & Dad
            newState = (state[Problem1.P]-1,state[Problem1.T],state[Problem1.M],state[Problem1.D]-1,state[Problem1.S],state[Problem1.G],0)
            if self.validate(newState):
                list.append(newState)   

            #PSL -  move Policeman & Son
            newState = (state[Problem1.P]-1,state[Problem1.T],state[Problem1.M],state[Problem1.D],state[Problem1.S]-1,state[Problem1.G],0)
            if self.validate(newState):
                list.append(newState)   
            
            #PGL -  move Policeman & Daughter
            newState = (state[Problem1.P]-1,state[Problem1.T],state[Problem1.M],state[Problem1.D],state[Problem1.S],state[Problem1.G]-1,0)
            if self.validate(newState):
                list.append(newState)   

            #PL -  move Policeman
            newState = (state[Problem1.P]-1,state[Problem1.T],state[Problem1.M],state[Problem1.D],state[Problem1.S],state[Problem1.G],0)
            if self.validate(newState):
                list.append(newState)   

            #ML -  move Mom
            newState = (state[Problem1.P],state[Problem1.T],state[Problem1.M]-1,state[Problem1.D],state[Problem1.S],state[Problem1.G],0)
            if self.validate(newState):
                list.append(newState)  

            #DL -  move Dad
            newState = (state[Problem1.P],state[Problem1.T],state[Problem1.M],state[Problem1.D]-1,state[Problem1.S],state[Problem1.G],0)
            if self.validate(newState):
                list.append(newState)    
        else:   #boat on the left side
            #PTL - move Policeman & Thief Right
            newState = (state[Problem1.P]+1,state[Problem1.T]+1,state[Problem1.M],state[Problem1.D],state[Problem1.S],state[Problem1.G],1)
            if self.validate(newState):
                list.append(newState)
                
            #MGL - move Mom and 1 daughter Left
            newState = (state[Problem1.P],state[Problem1.T],state[Problem1.M]+1,state[Problem1.D],state[Problem1.S],state[Problem1.G]+1,1)
            if self.validate(newState):
                list.append(newState)   
                
            #DSL - move Dad and 1 son left
            newState = (state[Problem1.P],state[Problem1.T],state[Problem1.M],state[Problem1.D]+1,state[Problem1.S]+1,state[Problem1.G],1)
            if self.validate(newState):
                list.append(newState)
                
            #MDL - move Mom and Dad
            newState = (state[Problem1.P],state[Problem1.T],state[Problem1.M]+1,state[Problem1.D]+1,state[Problem1.S],state[Problem1.G],1)
            if self.validate(newState):
                list.append(newState)     
                
            #PTL -  move Policeman & Mom
            newState = (state[Problem1.P]+1,state[Problem1.T],state[Problem1.M]+1,state[Problem1.D],state[Problem1.S],state[Problem1.G],1)
            if self.validate(newState):
                list.append(newState)   
            
            #PDL -  move Policeman & Dad
            newState = (state[Problem1.P]+1,state[Problem1.T],state[Problem1.M],state[Problem1.D]+1,state[Problem1.S],state[Problem1.G],1)
            if self.validate(newState):
                list.append(newState)   

            #PSL -  move Policeman & Son
            newState = (state[Problem1.P]+1,state[Problem1.T],state[Problem1.M],state[Problem1.D],state[Problem1.S]+1,state[Problem1.G],1)
            if self.validate(newState):
                list.append(newState)   
            
            #PGL -  move Policeman & Daughter
            newState = (state[Problem1.P]+1,state[Problem1.T],state[Problem1.M],state[Problem1.D],state[Problem1.S],state[Problem1.G]+1,1)
            if self.validate(newState):
                list.append(newState)   

            #PL -  move Policeman
            newState = (state[Problem1.P]+1,state[Problem1.T],state[Problem1.M],state[Problem1.D],state[Problem1.S],state[Problem1.G],1)
            if self.validate(newState):
                list.append(newState)   

            #ML -  move Mom
            newState = (state[Problem1.P],state[Problem1.T],state[Problem1.M]+1,state[Problem1.D],state[Problem1.S],state[Problem1.G],1)
            if self.validate(newState):
                list.append(newState)  

            #DL -  move Dad
            newState = (state[Problem1.P],state[Problem1.T],state[Problem1.M],state[Problem1.D]+1,state[Problem1.S],state[Problem1.G],1)
            if self.validate(newState):
                list.append(newState)   
        return list

    def validate(self, state):
        #verify no number is negative
        if state[Problem1.S] < 0 or state[Problem1.G] < 0 or state[Problem1.P] < 0 or state[Problem1.T] < 0 or state[Problem1.M] < 0 or state[Problem1.D] < 0:
            return False
        #verify no number is greater than the max
        if state[Problem1.S] > 2 or state[Problem1.G] > 2 or state[Problem1.P] > 1 or state[Problem1.T] > 1 or state[Problem1.M] > 1 or state[Problem1.D] > 1:
            return False
        #verify if boat is on right, then there must be an adult on the right side
        if state[Problem1.B] == 1 and (state[Problem1.P]+state[Problem1.M]+state[Problem1.D]) == 0:
            return False
        #verify if boat is on left, then there must be an adult on the left side
        if state[Problem1.B] == 0 and (state[Problem1.P]+state[Problem1.M]+state[Problem1.D]) == 3:
            return False
        #verify Policeman is with theif || theif is not with family
        if state[Problem1.P] != state[Problem1.T] and (state[Problem1.S] == 1 or state[Problem1.G] == 1 or state[Problem1.T] == state[Problem1.M] or state[Problem1.D] == state[Problem1.T] or bool(state[Problem1.S]) == bool(state[Problem1.T]) or bool(state[Problem1.G]) == bool(state[Problem1.T])):
            return False
        #verify Mom & Dad are together if so check...
        if state[Problem1.M] != state[Problem1.D]:
            # Dad is not with Daughters
            if state[Problem1.G] == 1 or bool(state[Problem1.D]) == bool(state[Problem1.G]): 
                return False
            #Mom is not with Sons
            if state[Problem1.S] == 1 or bool(state[Problem1.M]) == bool(state[Problem1.S]):
                return False          
        return True  
        
    def result(self, state, action):
        return action #since states are so lightweight, the action is itself the new state

    def goal_test(self, state):
        return state == self.goalState


def main():
    print('Family Dilema: ')
    print(' Tuples are in this format --> [<Node (isPoliceAcross, isThiefAcross, isMomAcross, isDadAcross, numberOfSonsAcross, numberOfGirlsAcross, isBoatAcross)>]')
    goalState = (1,1,1,1,2,2,1)

    problem = Problem1(goalState)
    goal = depth_first_search(problem)
    print("\nPath = ",goal.path(),"\n\nPath cost = ",goal.path_cost)
    #print("      Steps = " + str(goal.path()), "\n      Cost = " + str(goal.path_cost))
    print()

main()