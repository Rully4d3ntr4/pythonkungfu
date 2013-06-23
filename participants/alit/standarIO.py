#!/usr/bin/env python

# Standar input python

import sys;

def check(pilihan):
	try:
		return int(pilihan);
		
	except Exception, e:
		print "Input salah: %s" % pilihan;
		sys.exit;

def calculator(operasi, operasi1, operasi2):
	if (operasi == 1):
		return [bilangan1 + bilangan2, "+"]
	if (operasi == 2):
		return [bilangan1 - bilangan2, "-"]
	if (operasi == 3):
		return [bilangan2 * bilangan2, "*"]
	if (operasi == 4):
		return [bilangan2 / bilangan2, "/"]
	else:
		print "operasi salah: %s" % operasi
		sys.exit(1)



print "1. Tambah\n2. Kurang\n3. kali\n4. Bagi";
operasi = check(raw_input("Masukkan operasi:"))

bilangan1 = check(raw_input("Masukkan bilangan pertama :"))
# check(bilangan1);
# bilangan1 = int(bilangan1);

bilangan2 = check(raw_input("Masukkan bilangan kedua :"))
# check(bilangan2);
# bilangan2 = int(bilangan2);

hasil = calculator(check(raw_input(operasi)))
print "Hasil: {0} {3} {1} = {2:.2f}".format(bilangan1, bilangan2, hasil[0], hasil[1])
# nama = raw_input("Masukkan nama :");
# print "Nama kamu => %s" %nama

