class Solution:
    def isPalindrome(self, s: str) -> bool:
        lis = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
)
        i = 0
        j = len(s) - 1
        while i <= j:
            while i<j and s[i] not in lis:
                i += 1
            while i<j and s[j] not in lis:
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        
        return True
