first = input("1st number: ")
optr = input("enter optr ( +,-,*,/,%): ")
second = input("2nd number: ")

first = int(first)
second = int(second)
if optr == "+":
  print(first + second)
if optr == "-":
  print(first - second)
if optr == "*":
  print(first * second)
if optr == "/":
  print(first / second)
if optr == "%":
  print(first % second)  