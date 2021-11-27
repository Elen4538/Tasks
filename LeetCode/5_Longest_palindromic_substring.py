# Given a string s, return the longest palindromic substring in s.
def longestPalindrome(s: str) -> str:
    res = ''

    def helper(l,r):
        while l >=0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r +=1

        return s[l+1:r]

    for i in range(len(s)):
        attempt = helper(i,i)    
        if len(attempt) > len(res):
            res = attempt
        attempt = helper(i,i+1)  
        if len(attempt) > len(res):
            res = attempt
            
    return res


print(longestPalindrome('ac'))
print(longestPalindrome('babad'))
