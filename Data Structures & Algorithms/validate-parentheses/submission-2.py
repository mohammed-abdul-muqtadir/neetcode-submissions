class Solution:
    def isValid(self, s: str) -> bool:
        stac = []

        for i in s:

            if not stac and (i == ']' or i =='}' or i==')'):
                return False
    
            if i == "[" or i =="{" or i == "(":
                stac.append(i)

            elif stac[-1] == "[" and i == "]":
                stac.pop()
            
            elif stac[-1] == "{" and i == "}":
                stac.pop()
            
            elif stac[-1] == "(" and i == ")":
                stac.pop()
            
            else:
                return False

        return not stac
