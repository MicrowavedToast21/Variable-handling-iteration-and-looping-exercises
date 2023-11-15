print("Gasoline 95: €1,070/l", "\n"
      "Gasoline 98: €1,182/l", "\n"
      "Diesel A: €1,071/l")
while True:
    gasoline = input("Choose a gasoline: ")

    if gasoline in ["Gasoline 95", "Gasoline 98", "Diesel A"]:
          break
    else:
          print("Enter one of the three gasoline names")
while True:
    try:
      gasoline_liters = float(input("Choose the amount of liters of gasoline you want to refill: "))
      break
    except ValueError:
          print("Please enter the number of liters of gasoline that you want to refill")
if gasoline == "Gasoline 95":
      print("The price of Gasoline 95 is: ", 1.070*gasoline_liters, "€")
elif gasoline == "Gasoline 98":
      print("The price of Gasoline 98 is: ", 1.182*gasoline_liters, "€")
elif gasoline == "Diesel A":
      print("The price of Diesel A is: ", 1.071*gasoline_liters, "€")
else:
      print("Enter one of the three gasolines")