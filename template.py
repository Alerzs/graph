
import json
import csv

class Graph:


    def __init__(self ,file) -> None:
        
        pass

    def weight(self):
        #check if graph is weighted or not
        pass

    def yaal_count(self):
        pass

    def ras_count(self):
        pass
    


    def BFS(self, org, des):
        pass

    def DFS(self):
        pass

    def djkstra(self):
        pass
    
class Yaal:
    
    def __init__(self ,org ,des ,weight) -> None:
        self.org = org
        self.des = des
        self.weight = weight

    



grf = Graph("exl.csv")
print(grf.ras_count())
print(grf.yaal_count())