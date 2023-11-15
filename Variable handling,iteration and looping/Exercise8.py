import math
while True:
    try:
      n = int(input("Enter a number: "))
      break
    except ValueError:
        print("Please enter a number:")

def get_divisors(n):
    result = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n//i)
    return list(result)

print(f"The divisors of {n} are:", get_divisors(n))


