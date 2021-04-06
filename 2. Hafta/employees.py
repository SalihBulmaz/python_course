worker1 = {
  'name': 'Salih',
  'age': 22,
  'position': 'Sales Manager',
  'salary': 4500 
}
worker2 = {
  'name': 'Cem',
  'age': 24,
  'position': 'Manager',
  'salary': 7000 
}
worker3 = {
  'name': 'Merve',
  'age': 22,
  'position': 'HR',
  'salary': 4500 
}
Workers = [worker1, worker2, worker3]
for worker in Workers:
  print(f"Employee name is {worker['name']}, age is {worker['age']}, position is {worker['position']}, salary is {worker['salary']}")