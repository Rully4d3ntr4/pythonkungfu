#!/usr/bin/env python


def arrayOperation(array, operation):
    a = int(0)
    for x in xrange(0, len(array)):
        # Handling error
        if type(array[x]) != int:
            return "The element is not a number"
        else:
            a += array[x]
    if (operation == "sum"):
        return a
    if(operation == "avg"):
        return float(a) / len(array)
    if(operation == "mul"):
        a = int(array[0])
        for x in xrange(1, len(array)):
            # Handling error
            if type(array[x]) != int:
                return "The element is not a number"
            else:
                a = a * array[x]
        return a
    else:
        return "Invalid operation!"

myArray = [1, 2, 3, 4]

# Tanyain dia mau ngapain?
# 1. sum
# 2. avg
# 3. mul
# --> 2
# Tanyain, ada berapa angka yang mau dia operasiin
# --> 4
# array.append(angka1)
# array.append(angka2)
# array.append(angka3)
# array.append(angka4)
# print arrayOperation(myArray, "avg")

print arrayOperation(myArray, "sum")
print arrayOperation(myArray, "avg")
print arrayOperation(myArray, "mul")
