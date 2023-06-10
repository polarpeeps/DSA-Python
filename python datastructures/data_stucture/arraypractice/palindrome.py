from rev_array import reverse as f
def is_palindrome(s):
    # start = 0
    # ends = len(s) - 1
    # while start < ends :
    #     start = start + 1
    #     ends = ends - 1
    #     if s[start] == s[ends]:
    #         continue
    #     else:
    #         return False
    #     return True
    rev = f(s)
    if s == rev :
        return True
    else:
        return False
    
    
print(is_palindrome("antgtna"))