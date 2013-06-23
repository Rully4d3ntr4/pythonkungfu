#!/usr/bin/env python
import sys

def check(pilihan):
	try:
		pilihan = int(pilihan);
		pass;
	except Exception,e:
		print "input salah: %s" % pilihan;
		sys.exit(1);

def calculator(opersi, bilangan1, bilangan2):
	if (opersi == "1"):
		return [bilangan1 + bilangan2, "+"]
	if (opersi== "2"):
		return [bilangan1 - bilangan2, "-"]
	if (opersi== "3"):
		return [bilangan1 * bilangan2, "*"]
	if (opersi== "4"):
		return [bilangan1 / bilangan2, "/"]
	else:
		print "opersi salah: %s" % opersi
		sys.exit(1)


print "1. Tambah\n2. kurang\n3. kali\n4.Bagi";
opersi= raw_input("masukan opersi");
check(opersi);

bilangan1 = raw_input("masukan nilai pertama:")
check(bilangan1)
bilangan1 =int(bilangan1)

bilangan2 = raw_input("masukan nilai kedua:")
check(bilangan2)
bilangan2 =int(bilangan2)


hasil = calculator(opersi, bilangan1, bilangan2);
print "hasil: {0} {3} {1} = {2}".format(bilangan1, bilangan2,hasil[0], hasil[1]);

						
	