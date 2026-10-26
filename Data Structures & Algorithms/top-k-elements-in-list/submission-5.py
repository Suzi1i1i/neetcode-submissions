class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        out = []
        count_nums = Counter(nums)
        # print(count_nums)
        for num in count_nums:
            # print(min_heap)
            heapq.heappush(min_heap, (count_nums[num], num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        for i in range(k):
            elem = heapq.heappop(min_heap)
            # print(elem)
            out.append(elem[1])
            # print("out:", out)
        return out

        