class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        for num, count in counts.items():
            heapq.heappush(heap,(count,num))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        for num in heap:
            ans.append(num[1])
        return ans
