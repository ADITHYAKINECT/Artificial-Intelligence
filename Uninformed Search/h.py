#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 01:36:01 2018

@author: Iswariya Manivannan
"""

import sys
import os
import time
from collections import deque
import itertools

class Queue:

    def __init__(self):
        self.queue = deque()

    def isempty(self):
        return len(self.queue)!=0
    
    def push(self,x):
        self.queue.append(x)
    
    def get(self):
        return self.queue.popleft()

    def poplast(self):
        return self.queue.pop() 

    def addFront(self,x):
        self.queue.appendleft(x)     

class squareGrid:

# Class Constructors to initialize all the variables    
    def __init__(self,map):

        self.horizantal_walls = list()
        self.vertical_walls = list()
        self.goals = list()
        self.start = tuple()
        self.path = list()
        self.tree = dict()
        self.mazemap = map
        self.width = len(map[0])
        self.height = len(map)
        self.maxDepth = self.width * self.height 

# Method to check whether the point is in the map    
    def in_bounds(self,i):

        (y,x) = i
        if (0 <= x<= self.width) and (0 <=y<= self.height):
            return True
        else: 
            return False

# Method to generate        
    def neighbors(self,i):
        (x,y) = i
        results = [(x+1,y),(x,y-1),(x-1,y),(x,y+1)]
        results = filter(self.in_bounds,results)
        return results

# Method to Backtrack path from goal to start
    def contruct_path(self,goal):

        current = goal
        local_path = list()
        while current!=self.start:
            local_path.append(current)
            current = self.tree[current]
        local_path.append(self.start)
        local_path.reverse()
        return local_path   

# Metohd to display and wirte the result in specified output file
    def display(self,myFile):
    
        m = open(myFile,"w+")
        s = [['   ']*self.width]*self.height
        for j in range(self.height):
            for i in range(self.width):
                x = (j,i)
                if(x == self.start):
                    s[j][i] = "S"
                elif(x in self.goals):
                    s[j][i]= "G"
                elif(x in self.path): 
                    parent = self.tree[x]
                    if x[0] == parent[0] + 1: s[j][i] = "v"
                    if x[1] == parent[1] + 1: s[j][i] = ">"
                    if x[1] == parent[1] - 1: s[j][i] = "<" 
                    if x[0] == parent[0] - 1: s[j][i] = "Λ"

                elif(x in self.horizantal_walls):
                    s[j][i] = "="
                elif(x in self.vertical_walls):
                    s[j][i] = "|"        
                else:
                    s[j][i] = " "
                m.write(s[j][i])  
                # print(s[j][i],end=" ")      
            # print("\n")
            m.write("\n")    
        m.close()  

# Method to Classify Map symbols as "horizantal walls", "vertical walls", "start" and "goals"
    def maze_map_tree(self):

        for y in range(self.height):
            for x in range(self.width-1):
                if(self.mazemap[y][x] == "="):
                    self.horizantal_walls.append((y,x))
                elif(self.mazemap[y][x] == "|"):
                    self.vertical_walls.append((y,x))    
                elif(self.mazemap[y][x] == "*"):
                    self.goals.append((y,x))
                elif(self.mazemap[y][x] == "s"):
                    self.start = (y,x)  

# Method to find paths for each goal and to invoke the display method 
    def write_file(self,myFile):

        for i in self.goals:
            if (self.tree.get(i)!=None):
                self.path.append(self.contruct_path(i))  
        self.path = list(itertools.chain(*self.path))
        self.display(myFile) 

# Depth Limited Recursive Method for IDDFS
    def DLS(self,end,depth,queue):

        if not queue.isempty():
            return 0
        current = queue.get()

        if(current == end):
            return 1 

        if depth <= 0:
            return 0
        else: 
            for next in self.neighbors(current):
                if next not in self.tree and next not in self.horizantal_walls and next not in self.vertical_walls:
                    self.tree[next] = current 
                    queue.push(next)
            result = self.DLS(end,depth-1,queue)  
            if result ==1:
                return 1  
        return 0        
    

def maze_map_to_tree(maze):
    
    global myGrid 
    myGrid = squareGrid(maze)
    myGrid.maze_map_tree()
    return myGrid

def write_to_file(myFile):
    myGrid.write_file(myFile)
