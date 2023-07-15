def ispalindrome(s):
    x = 0
    string = list(s)
    palindrome = []
    for letter in string:
        x += 1
        if letter == string[-x]:
            palindrome.append(letter)
    if len(palindrome) == len(string):
        return True
    else:
        return False

print(ispalindrome('ахуеть'))