#!/usr/bin/env python

def cetak(arg):
	print arg;

def tambah(arg1, arg2):
	print arg1 + arg2;

def kurang(arg1, arg2):
	print arg1 - arg2;

def getAngkaKuadrat(arg):
	return arg **2;

def angkaDikaliDua(arg):
	return arg * 2;


tambah(3,7,);
kurang(10,5);
angkaGua = getAngkaKuadrat(angkaDikaliDua(2));
cetak(angkaGua);
# angkaDikaliDua(2) =4; getAngkaKuadrat(4) = 16; angkaGua = 14

