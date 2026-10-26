class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        out = []
        count_nums = Counter(nums)
        # print(count_nums)
        for num in count_nums:
            # print(max_heap)
            heapq.heappush(max_heap, (count_nums[num], num))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        for i in range(k):
            elem = heapq.heappop(max_heap)
            # print(elem)
            out.append(elem[1])
            # print("out:", out)
        return out

        