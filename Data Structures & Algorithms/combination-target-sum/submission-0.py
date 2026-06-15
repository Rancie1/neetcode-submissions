class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(curr,path,i):
            if curr == target:
                ans.append(path[:])
                return

            if curr > target:
                return

            for i in range(i,len(nums)):
                curr += nums[i]
                path.append(nums[i])
                backtrack(curr,path,i)
                curr -= nums[i]
                path.pop()
            

        backtrack(0,[],0)
        return ans
                
        