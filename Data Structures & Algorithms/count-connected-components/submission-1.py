class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        ans = 0
        seen = set()

        def bfs(root):
            q = deque()
            q.append(root)
            

            while q:
                curr = q.popleft()
                seen.add(curr)
                for nei in graph[curr]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)

        for node in range(n):
            if node not in seen:
                seen.add(node)
                ans += 1
                bfs(node)

        return ans



        