class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = []

        for _ in range(len(nums)+1):
            buckets.append([])

        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        for num, freq in count.items():
            buckets[freq].append(num)

        ans = []
     

        for i in range(n, -1, -1):
            for n in buckets[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        