class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = [pair[1] for pair in heap]

        return ans

        

        