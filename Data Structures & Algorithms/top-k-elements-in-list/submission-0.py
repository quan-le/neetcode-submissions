class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        sorted_item = sorted(
            frequency.items(),
            key = lambda item: item[1],
            reverse = True
        )

        results = []

        for i in range(k):
            results.append(sorted_item[i][0])

        return results