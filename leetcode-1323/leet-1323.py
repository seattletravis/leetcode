def maximum69Number (num):
    place = 10000
    while place > 0:
        digit = (num - num % place) / place
        if digit % 10 == 6:
            result = int(num + (place * 3))
            return result
        place = place / 10
    return num

print(maximum69Number(9669))
print(maximum69Number(9996))
print(maximum69Number(9999))
