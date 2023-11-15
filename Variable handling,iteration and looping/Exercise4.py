def find_weights(target_weight):
    weights = [1000, 500, 200, 100, 50, 10, 5, 2, 1]
    result = {}

    for weight in weights:
        count = target_weight // weight
        if count > 0:
            result[weight] = count
            target_weight -= count * weight
    return result

def gramBalance():
 while True:
    try:
        target_weight = int(input("Enter the target weight in grams to balance the scale: "))
        if target_weight < 0:
            print("Please enter a non negative weight")
        else:
            result = find_weights(target_weight)
            print("Weights needed: ")
            for weight, count in result.items():
                print(f"{count} x {weight}g")
    except ValueError:
        print("Please enter a valid integer number: ")

gramBalance()









