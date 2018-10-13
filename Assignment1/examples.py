"""
V1.0
"""
from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search

#______________________________________________________________________________
#An implementation of the Missionary-Cannibal problem
# Tuple format = [<Node (leftMissionaries, rightMissionaries, leftCannibals, rightCannibals, boatSide)>]
class MCP(Problem):
    #state is a tuple(LM,RM,LC,RC,B) with initial value (0,3,0,3,1)
    #last value flips between 1(R) and 0(L)   
    LM=0; RM=1; LC=2; RC=3; B=4 #class "constants"
    
    def __init__(self, goal):
        self.initial = (0,3,0,3,1)
        self.goalState = goal
    
    def actions(self, state):
        #actions are simply the result states possible in this example
        list=[]
        if state[MCP.B]==1: #boat on the right side
            #1ML - move 1 missionary left
            newState = (state[MCP.LM]+1,state[MCP.RM]-1,state[MCP.LC],state[MCP.RC],0)
            if self.validate(newState):
                list.append(newState)
                
            #2ML - move 2 missionaries left
            newState = (state[MCP.LM]+2,state[MCP.RM]-2,state[MCP.LC],state[MCP.RC],0)
            if self.validate(newState):
                list.append(newState)   
                
            #1CL - move one cannibal left
            newState = (state[MCP.LM],state[MCP.RM],state[MCP.LC]+1,state[MCP.RC]-1,0)
            if self.validate(newState):
                list.append(newState)
                
            #2CL - move two cannibals left
            newState = (state[MCP.LM],state[MCP.RM],state[MCP.LC]+2,state[MCP.RC]-2,0)
            if self.validate(newState):
                list.append(newState)     
                
            #1M1CL -  move one missionary and one cannibal left
            newState = (state[MCP.LM]+1,state[MCP.RM]-1,state[MCP.LC]+1,state[MCP.RC]-1,0)
            if self.validate(newState):
                list.append(newState)   
                
        else:   #boat on the left side
            #1MR - move 1 missionary right
            newState = (state[MCP.LM]-1,state[MCP.RM]+1,state[MCP.LC],state[MCP.RC],1)
            if self.validate(newState):
                list.append(newState)
                
            #2MR - move 2 missionaries right
            newState = (state[MCP.LM]-2,state[MCP.RM]+2,state[MCP.LC],state[MCP.RC],1)
            if self.validate(newState):
                list.append(newState)    
                
            #1CR - move 1 cannibal right
            newState = (state[MCP.LM],state[MCP.RM],state[MCP.LC]-1,state[MCP.RC]+1,1)
            if self.validate(newState):
                list.append(newState)
                
            #2CR - move 2 cannibals right
            newState = (state[MCP.LM],state[MCP.RM],state[MCP.LC]-2,state[MCP.RC]+2,1)
            if self.validate(newState):
                list.append(newState)    
                
            #1M1CL-  move one missionary and one cannibal right
            newState = (state[MCP.LM]-1,state[MCP.RM]+1,state[MCP.LC]-1,state[MCP.RC]+1,1)
            if self.validate(newState):
                list.append(newState)   
                
        return list

    def validate(self, state):
        #verify no number is negative
        if state[MCP.LM] < 0 or state[MCP.RM] < 0 or state[MCP.LC] < 0 or state[MCP.RC] < 0:
            return False
        #verify no number is greater than the max
        if state[MCP.LM] > 3 or state[MCP.RM] > 3 or state[MCP.LC] > 3 or state[MCP.RC] > 3:
            return False
        #verify if boat is on right, then there must be someone on the right side
        if state[MCP.B] == 1 and (state[MCP.RM]+state[MCP.RC])==0:
            return False
        #verify if boat is on left, then there must be someone on the left side
        if state[MCP.B] == 0 and (state[MCP.LM]+state[MCP.LC])==0:
            return False
        #verify left missionaries are >= left cannibals, unless there are no missionaries on the left
        if state[MCP.LM] < state[MCP.LC] and state[MCP.LM]!=0:
            return False
        #verify right missionaries are >= right cannibals, unless there are no missionaries on the right
        if state[MCP.RM] < state[MCP.RC] and state[MCP.RM]!=0:
            return False
        return True  
        
    def result(self, state, action):
        return action #since states are so lightweight, the action is itself the new state

    def goal_test(self, state):
        return state == self.goalState


def main():
    #Runs the Cannibals and Missionary problem, will provide a solution to getting all missionaries
    #and all cannibals to the other side, without missionaries ever being outnumbered by cannibals
    #on either side.
    print('Missionaries/Cannibals Problem: ')
    print(' Tuples are in this format --> [<Node (leftMissionaries, rightMissionaries, leftCannibals, rightCannibals, boatSide)>]')
    goalState = (3,0,3,0,0)

    problem = MCP(goalState)
    goal = depth_first_search(problem)
    print("\nPath = ",goal.path(),"\n\nPath cost = ",goal.path_cost)
    #print("      Steps = " + str(goal.path()), "\n      Cost = " + str(goal.path_cost))
    print()

main()