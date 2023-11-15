while True:
    try:
        num = float(input("Enter a real number: "))
        break
    except ValueError:
        print("please enter a valid real number: ")

precisions = []
while True:
    precision_input = input("Enter precision numbers seperated by comas: ")

    try:
        precisions = [int(p) for p in precision_input.split(',')]
        break
    except ValueError:
        print("Please enter valid integers for precisions.")

for precision in precisions:
    formatted_num = "{:.{}f}".format(num, precision)
    print(formatted_num)