#!/usr/bin/env python

def cetak(arg):
	print arg;
def tambah(arg1, arg2):
	print arg1 + arg2;
def kurang(arg1, arg2):
	print  arg1 - arg2;
def getAngkakuadrat(arg):
	return arg **2;
def angkaDikaliDua(arg):
	return arg *2;

tambah(3,6);
kurang(1,1);
angkaGue = getAngkakuadrat(angkaDikaliDua(2));
cetak(angkaGue);
