import heapq


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        res = heapq.nlargest(k, nums)
        return res[k-1]


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(sol.findKthLargest(nums, k))
