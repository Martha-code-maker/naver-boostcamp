while True:
    value = input("Input number")
    for digit in value:
        if digit not in "0123456789":
            raise ValueError("you should input number")
    
    print("change number into int value - ", int(value))
    