class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build adjacency list (graph)
        graph = {}
        for i, j in edges:
            graph.setdefault(i, []).append(j)
            graph.setdefault(j, []).append(i)
        
        print(graph)

        # dfs/bfs traverse, count component
        visited = set()
        count = 0
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph.get(node, []):
                dfs(neighbor)
            return
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        
        return count