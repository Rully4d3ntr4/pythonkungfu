#!/usr/bin/env python

asbak = ["Abu", "Puntung", "Sampah"];

print asbak;

for i in xrange(0, len(asbak)):
    print asbak[i];

beberapaAngka = [11, 3, 7, 9];

# Tambahin 10 ke dalam array beberapaAngka
beberapaAngka.append(10);

def sumArray(array):
    a = int(0);
    # Handling error
    if type(array[0]) != int:
        return "The element is not a number";
    else:
        a = array[0];
    for x in xrange(1, len(array)):
        # Handling error
        if type(array[x]) != int:
            return "The element is not a number";
        else:
            a = a + array[x];
    return a;

print beberapaAngka;
print sumArray(beberapaAngka);

