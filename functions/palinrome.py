def isPalindrome(s):
  left = 0

  right = len(s) - 1

  while right >= left:
    if s[left] != s[right]:
      return False

    left=left + 1
    right = right - 1

  return True

print("is a palindrome ? ")
print(isPalindrome(input('give a noun to check: '))) # True