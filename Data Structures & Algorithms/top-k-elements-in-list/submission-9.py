class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictFrequency = {}
        for n in nums:
            if n in dictFrequency:
                dictFrequency[n]=dictFrequency[n]+1
                #print(f"key: {n}")
                #print(f"value: {dictFrequency[n]}")
            else:
                dictFrequency[n]=1

        result = []
        tempResult = sorted(dictFrequency, key = dictFrequency.get, reverse = True)
        for r in tempResult:
            if len(result)<k:
                result.append(r)
                #print(f"added: {r}")
                #print(result)
        return result








"""
LOGIC:

1- create hashmap
2- key = element in nums, value = number of times it appears
3- sort map
4- take top k values
"""     