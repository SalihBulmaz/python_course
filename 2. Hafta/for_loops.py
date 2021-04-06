#For loops iterating a list
fruits = ['apple', 'banana', 'orange', 'strawberry']
for fruit in fruits:
  print(fruit)

#For loops iterating range function
for i in range(4):
  print(fruits[i])

#For loops helping to calculate squares of numbers.
squares = []
for num in range(15):
  squares.append(num ** 2) #Appending squares of the numbers
print(squares)

#For loops to create Fibonacci number series
fibonacci_nums = []
for n in range(1, 15):
  if n == 1 or n == 2:
    a = 1
    b = 1
  else:
    a, b = b, a + b
  fibonacci_nums.append(b) #After assigning a + b to b which is (a)n-1 + (a)n = (a)n+1
print(fibonacci_nums)