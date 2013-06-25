#!/usr/bin/env python
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

array = [];

def menu():
	print "1.SUM\n2.AVERAGE\n3.MUL\n"

def summation():
	angka = input("masukan beberapa angka : ")
	for x in xrange(0,int(angka)):
		array.append(input("--> Masukan angka ke - %d : "%(x+1)))
	print""
	jumlah = sum(array)
	print "Summation is : ",jumlah

def average():
	#array = [];
	angka = input("masukan beberapa angka : ")
	for x in xrange(0,int(angka)):
		array.append(input("--> Masukan angka ke - %d : "%(x+1)))
	print""
	jumlah = sum(array)
	average = float(jumlah) / len(array)
	print "Average is : ",average

def mul():
	mul = 1;
	angka = input("masukan beberapa angka : ")
	for x in xrange(0,int(angka)):
		array.append(input("--> Masukan angka ke - %d : "%(x+1)))
		mul *= array[x]
	print "Mul is : ",mul

menu()
pil = input("masukan pilihan : ")
if pil == 1:
	summation()
elif pil == 2:
	average()
elif pil == 3:
	mul()
else:
	print "invalid operation"