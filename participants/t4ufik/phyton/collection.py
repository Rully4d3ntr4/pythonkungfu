#!/usr/bin/env python
kardus = ["baju","kaos",3,5,6];
print kardus;
for x in xrange(0, len(kardus)):
	print kardus[x];

beberapaAngka = [12, 3, 4, 7];
print beberapaAngka;

beberapaAngka.append(10);

def sumArray(array):
	a = int(0);
	if type(array[0]) != int:
		return "this element is not number";
	else:
		a = array[0];
	for x in xrange(1, len(array)):
		if type(array[x]) != int:
			return "this element is not number";
		else:
	 		a = a + array[x];
	return a;

print sumArray(beberapaAngka);


