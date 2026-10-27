size = int(input("Enter your size"))
anthony = 1
for x in range (size):
    for y in range (x):
        print(anthony, end= " ")
        anthony += 1
    print()