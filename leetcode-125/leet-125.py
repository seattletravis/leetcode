#Intuitive Way to solve this

def isPalindrome(s):
    stripped = ''
    deppirts = '' 
    for letter in s:
        if letter.isalnum():
            stripped += letter.lower()
            deppirts = letter.lower() + deppirts
    print(stripped, deppirts)
    return stripped == deppirts

#slightly better:
#Remove string to string comparison and compared string to reverse iteration over string
def isPalindrome(s):
    stripped = ''
    for letter in s:
        if letter.isalnum():
            stripped += letter.lower()
    return stripped == stripped[::-1] # <--

#slightly better still




