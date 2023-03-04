names = [input() for _ in range(5)]

pos = names.index("Ellie") + 1

if pos == 1:
    print("1st")
elif pos == 2:
    print("2nd")
elif pos == 3:
    print("3rd")
elif pos == 4:
    print("4th")
elif pos == 5:
    print("5th")
else:
    print("Error: Ellie's name not found in the input list")
