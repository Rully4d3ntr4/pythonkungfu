#!/usr/bin/env python

def cetak(arg):
	print arg;

def tambah(arg1 , arg2):
	print arg1 + arg2;

def kurang(arg1 , arg2):
	print arg1 - arg2;

def getAngkaKuadrat(arg):
	return arg **2;

def AngkadikaliDua(arg):
	return arg * 2;

tambah(3 , 7);
kurang(10 , 5);
angkaGue = getAngkaKuadrat(AngkadikaliDua(2));
cetak(angkaGue);