import math

def countDigits(num):
  instance = num
  count = 0

  while instance > 0:
    digit = instance % 10
    instance = instance // 10
    if num % digit == 0:
      count += 1
  return count

print(countDigits(1248))
