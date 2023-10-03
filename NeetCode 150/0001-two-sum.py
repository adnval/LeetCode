class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {} # Dictionary, value as the key and index as value
        for i, v in enumerate(nums): # i is index, v is value with enumerate
            if target - v in hmap: # Checks if there is something with the key target - value for two sum
                return [hmap[target - v], i]
            hmap[v] = i # If not, adds the key pair into the dictionary
        return
