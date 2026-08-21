class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        unique_elements = list(counts.items())
        unique_elements.sort(key=lambda x : x[1], reverse = True)
        result = []
        for i in range(k):
            result.append(unique_elements[i][0])
        return result

        