while True:
    try:
      n = int(input("Enter a positive integer: "))
      if n < 0:
          print("Please enter a positive integer: ")
      break
    except ValueError:
        print("Please enter a valid positive integer")

for i in range(n, 0, -1):
    print("".join(str(j) for j in range(1, i + 1)))

