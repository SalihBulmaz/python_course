fruits = ['apple', 'banana', 'orange', 'strawberry']

#While loops iterating a list
i = 0
while i < 4:
  print(fruits[i])
  i += 1

#While loops helping to calculate squares of numbers.
squares = []
num = 0
while num < 15:
  squares.append(num ** 2)
  num += 1

#While loops to create Fibonacci number series
fibonacci_nums = []
n = 1
while n < 15:
  if n == 1 or n == 2:
    a = 1
    b = 1
  else:
    a, b = b, a + b
  fibonacci_nums.append(b)
  n += 1 
  #After assigning a + b to b which is (a)n-1 + (a)n = (a)n+1
print(fibonacci_nums)