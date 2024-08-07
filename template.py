
import csv
import json
from collections import defaultdict, deque
import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v, weight=1):
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight)) # برای گراف غیرجهت‌دار
        self.vertices.add(u)
        self.vertices.add(v)

    @classmethod
    def from_csv(cls, filename):
        graph = cls()
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                for j in range(len(row)):
                    if int(row[j]) > 0: # اگر وزن یال بیشتر از 0 باشد
                        graph.add_edge(row[0], row[j], int(row[j]))
        return graph

    @classmethod
    def from_nested_list(cls, nested_list):
        graph = cls()
        for i in range(len(nested_list)):
            for j in range(len(nested_list)):
                if nested_list[i][j] > 0: # اگر وزن یال بیشتر از 0 باشد
                    graph.add_edge(i, j, nested_list[i][j])
        return graph

    @classmethod
    def from_json(cls, json_data):
        graph = cls()
        edges = json.loads(json_data)
        for edge in edges:
            graph.add_edge(edge['source'], edge['target'], edge['weight'])
        return graph

    def to_csv(self):
        with open('graph.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
        for vertex in self.vertices:
            row = [vertex] + [0] * len(self.vertices)
        for neighbor, weight in self.adjacency_list[vertex]:
            row[list(self.vertices).index(neighbor)] = weight
            writer.writerow(row)

    def to_nested_list(self):
        size = len(self.vertices)
        nested_list = [[0] * size for _ in range(size)]
        for vertex in self.vertices:
            for neighbor, weight in self.adjacency_list[vertex]:
                nested_list[list(self.vertices).index(vertex)][list(self.vertices).index(neighbor)] = weight
        return nested_list

    def to_json(self):
        edges = []
        for vertex in self.vertices:
            for neighbor, weight in self.adjacency_list[vertex]:
                edges.append({'source': vertex, 'target': neighbor, 'weight': weight})
        return json.dumps(edges)

    def number_of_vertices(self):
        return len(self.vertices)

    def number_of_edges(self):
        return sum(len(neighbors) for neighbors in self.adjacency_list.values()) // 2

    def get_vertices(self):
        return list(self.vertices)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(neighbor for neighbor, _ in self.adjacency_list[vertex] if neighbor not in visited)

        return result

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_recursive(vertex):
            visited.add(vertex)
            result.append(vertex)
            for neighbor, _ in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

            dfs_recursive(start)
        return result

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.adjacency_list[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances