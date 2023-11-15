```
import math

def countDigits(num):
  num = 1248
  instance = num
  count = 0

  while instance > 0:
    divisor = instance % 10
    instance = math.floor(instance / 10)
    if num % divisor == 0:
      count += 1
  return count

print(countDigits(1248))
```