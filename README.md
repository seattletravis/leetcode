[Watch Video on Youtube - Link](https://youtu.be/BeS_4efa7-U)

This is an iterative approach to extracting each digit from a multi digit number. In this example we're using pythong but this will work in most languages.

The important lines of code are:

```
while instance > 0:
  divisor = instance % 10
  instance = math.floor(instance / 10)
```




```
import math

def countDigits(num):
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
