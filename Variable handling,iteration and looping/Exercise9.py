total_numbers = 0
highest_number = float("-inf")
lowest_number = float("inf")
sum_of_numbers = 0

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break
    total_numbers += 1
    sum_of_numbers += number
    highest_number = max(highest_number, number)
    lowest_number = min(lowest_number, number)

if total_numbers > 0:
    average_number = sum_of_numbers / total_numbers
else:
    average_number = 0

print("Number of numbers read are: ", total_numbers)
print("Highest number is: ", highest_number)
print("Lowest number is: ", lowest_number)
print("Average of numbers is: ", average_number)