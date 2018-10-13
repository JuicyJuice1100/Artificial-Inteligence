"""
V1.0
"""
from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search

#______________________________________________________________________________
#An implementation of the  Family Raft Problem
# Tuple format = [<Node (isPoliceAcross, isThiefAcross, isMomAcross, isDadAcross, numberOfSonsAcross, numberOfGirlsAcross, isBoatAcross)>]
class Problem2(Problem):
    #state is a tuple(S, F, T) with initial value (7, 0, 0)
    #S >= 0 and <= 7; F >= 0 and <= 4; T >= 0 and <= 3; 
    P7=0; P4=1; P3=2 #class "constants"
    
    def __init__(self, goal):
        self.initial = (7, 0, 0)
        self.goalState = goal
    
    def actions(self, state):
        #actions are simply the result states possible in this example
        list=[]
        #74 Pour P7 to P4 
        newState = (state[Problem2.P7] - min(state[Problem2.P7], 4 - state[Problem2.P4]), min(state[Problem2.P7], 4), state[Problem2.P3])
        if self.validate(newState):
            list.append(newState)
        #73 Pour P7 to P3
        newState = (state[Problem2.P7] - min(state[Problem2.P7], 3 - state[Problem2.P3]), state[Problem2.P4], min(state[Problem2.P7], 3))
        if self.validate(newState):
            list.append(newState)
        #47 Pour P4 to P7
        newState = (state[Problem2.P7] + state[Problem2.P4], 0, state[Problem2.P3])
        if self.validate(newState):
            list.append(newState)
        #43 Pour P4 to P3
        newState = (state[Problem2.P7], state[Problem2.P4] - min(state[Problem2.P4], 3 - state[Problem2.P3]), min(state[Problem2.P4], 3))
        if self.validate(newState):
            list.append(newState)
        #37 Pour P3 to P7
        newState = (state[Problem2.P7] + state[Problem2.P3], state[Problem2.P4], 0)
        if self.validate(newState):
            list.append(newState)
        newState = (state[Problem2.P7], min(state[Problem2.P4] + state[Problem2.P3], 4), state[Problem2.P3] - min(state[Problem2.P3], 4 - state[Problem2.P4]))
        if self.validate(newState):
            list.append(newState)
        #34 Pour P3 to P4
        return list

    def validate(self, state):
        #verify no number is negative
        if state[Problem2.P7] < 0 or state[Problem2.P4] < 0 or state[Problem2.P3] < 0:
            return False
        if state[Problem2.P7] > 7 or state[Problem2.P4] > 4 or state[Problem2.P3] > 3:
            return False      
        return True  
        
    def result(self, state, action):
        return action #since states are so lightweight, the action is itself the new state

    def goal_test(self, state):
        return state == self.goalState


def main():
    print('Water Jugs: ')
    print(' Tuples are in this format --> [<Node (litersOfWaterInPot1, litersOfWaterInPot2, litersOfWaterInPot3)>]')
    goalState = (2, 2, 3)

    problem = Problem2(goalState)
    goal = depth_first_search(problem)
    print("\nPath = ",goal.path(),"\n\nPath cost = ",goal.path_cost)
    #print("      Steps = " + str(goal.path()), "\n      Cost = " + str(goal.path_cost))
    print()

main()