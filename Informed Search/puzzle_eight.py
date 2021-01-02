
from itertools import chain 
import copy

class Node:

    def __init__(self,data,level,fval):
        self.data = data
        self.level = level
        self.fval = fval
        self.parent = None

    def find(self,x):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if(self.data[i][j] == x):
                    return i,j

    def in_boundary(self,position):
        x,y = position
        if(0 <= x <= 2 and 0 <= y <= 2):
            return True
        else:
            return False

    def generate_child(self):
        x,y = self.find('0')
        val_list = [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]
        val_list = filter(self.in_boundary,val_list)
        children = []

        for child in val_list:
            child_X,child_Y = child
            duplicate = copy.deepcopy(self.data) 
            # temp = duplicate[child_X][child_Y]
            # duplicate[child_X][child_Y] = duplicate[x][y]
            # duplicate[x][y] = temp
            duplicate[child_X][child_Y], duplicate[x][y] = duplicate[x][y], duplicate[child_X][child_Y]
            child_node = Node(duplicate,self.level+1,0)  
            children.append(child_node)  
            child_node.parent = self
        return children
  



class Puzzle:

    def __init__(self,size):
        self.n = size
        self.open = list()
        self.path = list()

    def accept(self):
        puz = list()
        for i in range(self.n):
            temp = input().split(",")
            puz.append(temp) 
            # puz = list(chain.from_iterable(puz))   
        return puz    
    
    def f(self,start,goal):
        return self.hueristics(start.data,goal)+start.level

    def hueristics(self,start,goal):
        temp = 0
        for i in range(self.n):
            for j in range(self.n):
                if(goal[i][j]!=0 and start[i][j]!=goal[i][j]):
                    temp = temp +1
        return temp

    
    def manhattan(self,start,goal):
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                if(goal[i][j]!=0 and start[i][j]!=goal[i][j]):
                    goal_node = Node(goal,0,0)
                    x,y = goal_node.find(start[i][j])
                    distance += abs(x-i) + abs(y - j)
        return distance    

    def display(self):
        print("\n")
        for x in self.path:
            for y in x.data:
                for z in y:
                    print(y)
            print("\n")
        print("\n")


    def AStar(self):
        print("Enter the Start Matrix \n")
        start = self.accept()
        print("Enter the Goal Matrix \n")
        goal = self.accept() 

        start = Node(start,0,0)
        start.fval = self.hueristics(start.data,goal)
        # start.fval = self.manhattan(start.data,goal)
        self.open.append(start)
        start.parent = None
   
        while len(self.open) > 0:
            cur = self.open[0]
            print(cur.level,"\n")

            if(self.hueristics(cur.data,goal) == 0):  
                print("Goal Node Reached!")
                break       

            self.open.remove(cur)
            # self.closed.append(cur)
            children = cur.generate_child()
            for next in children:
                next.fval = self.f(next,goal)
                self.open.append(next)        
            
            self.open.sort(key = lambda x:x.fval,reverse=False)
            
        
        while cur.parent != None:
            self.path.append(cur)
            cur = cur.parent
        self.path.append(cur) 
        self.path.reverse() 
        #     print("\n")
        #     for x in cur.data:
        #         for y in x:
        #             print(y,end=" ")
        #         print("\n")
        #     cur =cur.parent
        #     print("\n")
        # for x in cur.data:
        #     for y in x:
        #         print(y,end=" ")
        #     print("\n")

myPuzzle = Puzzle(3)
myPuzzle.AStar()
myPuzzle.display()
# start = Node([[0,1,8],[3,4,6],[2,5,7]],0,0)
# goal = [[0,1,2],[3,4,5],[6,7,8]]
# print(myPuzzle.manhattan(start.data,goal))