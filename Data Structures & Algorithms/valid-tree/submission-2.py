class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set()

        def dfs(node,prev):
            if node in seen:
                return False

            seen.add(node)
        
            for nei in graph[node]:
                if nei == prev:
                    continue
                if not dfs(nei,node):
                    return False


            return True

        if not dfs(0,-1):
            return False

        if len(seen) == n:
            return True
        else:
            return False

        