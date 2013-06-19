#!/usr/bin/env python

def cetak(arg):
	print arg;

def kali(arg1,arg2,arg3):
	print arg1 * arg2 * arg3;

def bagi(arg1,arg2,arg3):
	print arg1 / arg2 / arg3

def angkakuadrat(arg):
	return arg **2;

def angkadikalidua(arg):
	return arg *2
	
kali(1,3,2);	#6
bagi(10,1,2);	#5
angkague = angkakuadrat(angkadikalidua(2));
#angkadikalidua(2) = 4; angkakuadrat(4) = 16; angkague = 16
cetak(angkague);
