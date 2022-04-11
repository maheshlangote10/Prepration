list_node = {
    'A': ["B", "D"],
    'B': ['A', 'C'],
    'C': ['B'],
    'D':['A', 'E', 'F'],
    'E':['D', 'F', 'G'],
    'G':[],
    'F':['D', 'E', 'G', 'H'],
    'H':['G', 'F']

}
from queue import Queue

class Solution:
    def bfs(self, list_node, source):
        output = []
        visited = {}
        level = {}
        parent = {}
        queue = Queue()
        for node in list_node.keys():
            visited[node]=False
            level[node] = -1
            parent[node] = None
        print(visited)
        visited[source] = True
        level[source] = 0
        parent[source] = None
        queue.put(source)
        while not queue.empty():
            u = queue.get()
            output.append(u)
            for node in list_node[u]:
                if not visited[node]:
                    visited[node] = True
                    parent[node] = u
                    level[node] = level[u] + 1
                    queue.put(node)
        print(output)
        return queue

obj = Solution()
source = 'A'
obj.bfs(list_node, source)


