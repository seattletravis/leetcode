#Intuitive Way to solve this - 636ms
def isPalindrome1(s):
    stripped = ''
    deppirts = '' 
    for letter in s:
        if letter.isalnum():
            stripped += letter.lower()
            deppirts = letter.lower() + deppirts
    return stripped == deppirts

#slightly better: - 354ms
#Remove string to string comparison and compared string to reverse iteration over string
def isPalindrome2(s):
    stripped = ''
    for letter in s:
        if letter.isalnum():
            stripped += letter.lower()
    return stripped == stripped[::-1] # <--

#slightly better still - 282ms
#instead of changing tolower in the loop, change initial string tolower() before we start.
def isPalindrome3(s):
    s = s.lower()
    stripped = ''
    for letter in s:
        if letter.isalnum():
            stripped += letter
    return stripped == stripped[::-1]

#Even better! - 25ms
def isPalindrome4(s):              
    s = s.lower()
    s = filter(lambda x: x.isalnum(), s)
    return s == s[::-1]

#Best!!! - 18ms
def isPalindrome5(self, s):
    s = filter(lambda x: x.isalnum(), s)
    s = s.lower()
    return s == s[::-1]
