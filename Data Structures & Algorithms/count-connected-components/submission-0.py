class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0

        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set()

        def dfs(node):
            seen.add(node)

            for nei in graph[node]:
                if nei not in seen:
                    dfs(nei)


        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)

        return ans
                    
                
        