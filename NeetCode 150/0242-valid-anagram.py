class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # To check first if an anagram is even possible to skip the rest of the code
            return False

        countS, countT = {}, {}
        for i in range(len(s)): # Create hashmaps for both strings
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for char in countS: # Checks hashmap countT for the value of the key iterated from countS
            if countS[char] != countT.get(char, 0):
                return False
        return True
