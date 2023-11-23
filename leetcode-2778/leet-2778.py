def sumOddLengthSubarrays(arr):
  result = 0
  for start in range(len(arr)):
    for end in range(start + 1, len(arr) + 1, 2):
      result += sum(arr[start:end])
  return result

example1 = [1, 4, 2, 5, 3]
example2 = [1, 2]
example3 = [10, 11, 12]

print(sumOddLengthSubarrays(example1))
print(sumOddLengthSubarrays(example2))
print(sumOddLengthSubarrays(example3))


