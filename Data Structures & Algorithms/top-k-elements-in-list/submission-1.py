class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        store=defaultdict(int)

        for x in nums:
            store[x]+=1
        
        sorted_keys=sorted(store,key=store.get, reverse=True)

        return sorted_keys[:k]
        

        