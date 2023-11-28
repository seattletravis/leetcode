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


