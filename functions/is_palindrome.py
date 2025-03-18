def is_palindrome_simple(s):
    s = str(s)
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def is_palindrome_complex(s):
    s = str(s)
    s = s.lower().replace(" ", "")
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True