#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
import time
import math
from heapq import *

PUZZLE_TYPE = 8
ROW_SIZE = int(math.sqrt(PUZZLE_TYPE + 1))

class Node:

    def __init__(self,data,level,fval):
        self.data = data
        self.level = level
        self.fval = fval
        self.parent = None

    def find(self,x):
        for i in range(ROW_SIZE):
            for j in range(ROW_SIZE):
                if(self.data[i][j] == x):
                    return i,j

    def in_boundary(self,position):
        x,y = position
        if(0 <= x <= ROW_SIZE - 1 and 0 <= y <= ROW_SIZE - 1):
            return True
        else:
            return False

    def generate_child(self):
        x,y = self.find(0)
        val_list = [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]
        val_list = filter(self.in_boundary,val_list)
        children = []

        for child in val_list:
            child_X,child_Y = child
            duplicate = copy.deepcopy(self.data) 
            duplicate[child_X][child_Y], duplicate[x][y] = duplicate[x][y], duplicate[child_X][child_Y]
            child_node = Node(duplicate,self.level+1,0)  
            child_node.parent = self
            children.append(child_node)  
        return children
  

class Puzzle:

    def __init__(self,start_list,goal_list):
        self.open = list()
        self.path = list()
        self.no_of_nodes = 0
        self.execution_time = 0
        self.start = Node(self.convet_list(start_list),0,0)
        self.goal =  Node(self.convet_list(goal_list),0,0)
        self.priority_queue = []
        self.closed = list()

    def convet_list(self,input_list):
        x = []
        for i in range(ROW_SIZE):
            temp = []
            for j in range(ROW_SIZE):
                temp.append(input_list[ROW_SIZE * i + j])
            x.append(temp)
        return x       
    


    def hueristics(self,start,goal):
        temp = 0
        for i in range(ROW_SIZE):
            for j in range(ROW_SIZE):
                if(goal[i][j]!=0 and start[i][j]!=goal[i][j]):
                    temp = temp +1
        return temp

    
    def manhattan(self,start,goal):
        distance = 0
        for i in range(ROW_SIZE):
            for j in range(ROW_SIZE):
                if(goal[i][j]!=0 and start[i][j]!=goal[i][j]):
                    goal_node = Node(goal,0,0)
                    x,y = goal_node.find(start[i][j])
                    distance += abs(x-i) + abs(y - j)
        return distance    

    def display(self,myFile):
        print("\n")
        m = open(myFile,"w+")
        m.write("Number of States Explored: ")
        m.write(str(self.no_of_nodes))
        m.write("\n")
        m.write("Execution Time: ")
        m.write(str(self.execution_time))
        m.write("\n")

        for x in self.path:
            for y in x.data:
                for z in y:
                    print(z,end=" ")
                    m.write(str(z))
                    m.write(" ")
                m.write("\n")        
                print("\n")
            m.write("\n")        
            print("\n")
        m.close()
    

    def AStar(self):

        index = 0
        
        # self.start.fval = self.hueristics(self.start.data,self.goal.data)
        self.start.fval = self.manhattan(self.start.data,self.goal.data)
        heappush(self.priority_queue, (self.start.fval, index,self.start))

        start_time = time.time()
        while len(self.priority_queue):

            current = heappop(self.priority_queue)[2]
            print(current.level)
            self.no_of_nodes += 1
            self.closed.append(current)
            if(self.manhattan(current.data,self.goal.data) == 0):  
            # if(self.hueristics(current.data,self.goal.data) == 0):
                self.execution_time = time.time() - start_time  
                print("Goal Node Reached!")
                break       
            
            for next in current.generate_child():
                if next not in self.closed:
                    next.fval = self.hueristics(next.data,self.goal.data)
                    index += 1
                    heappush(self.priority_queue, (next.fval, index, next))        
            
        while current.parent != None:
            self.path.append(current)
            current = current.parent
        self.path.append(current) 
        self.path.reverse() 


puzzle_8 = [0, 1, 2, 3, 4, 5,8, 6, 7]
goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
myPuzzle = Puzzle(puzzle_8,goal)
myPuzzle.AStar()
myPuzzle.display("./Solutions/results41")
