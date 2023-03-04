a = int(input())
operator = input()
b = int(input())

if operator == "+":
    result = a + b
elif operator == "*":
    result = a * b
else:
    print("Invalid Operator")
    result = None

if result is not None:
    print(result)
    
