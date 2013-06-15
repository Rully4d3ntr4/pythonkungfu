#!/usr/bin/env python

asbak = ["abu","rokok","puntung"];

print "===";

print len(asbak);

print "===";

for x in xrange(0,len(asbak)):
	print asbak[x];

beberapaAngka = [12,3,7,9];
print beberapaAngka;
beberapaAngka.append(10);

def sumArray(array):
	a = int(0);
	if type(array[0]) != int:
		return "the element is not an integer";
	else:
		a = array[0];
	for x in xrange(1,len(array)):
		if type(array[0]) != int:
			return "the element is not an integer";
		a = a + array[x];
	return a;

print sumArray(beberapaAngka);

