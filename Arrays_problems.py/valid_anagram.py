#LC - 242
'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

#Code:
class Solution:
    def isAnagram(self,s : str,t: str)-> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False

#Optimal Solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s) != len(t):
            return False
        for ch in s:
            seen[ch] = seen.get(ch,0) + 1
        for ch in t:
            if ch not in seen:
                return False
            seen[ch] -= 1
            if seen[ch] == 0:
                del seen[ch]
        return len(seen) == 0
    
#Code Explanation:
'''
we first check if the both string has the same length if not its obviously false
then we use a dictionary to count the characters in s
then we minus the count of each character if we find in t 
if the dictionary becomes 0 we delete the char and finally if the dictionary is empty we return True
'''