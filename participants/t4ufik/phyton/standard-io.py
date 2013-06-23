#!/usr/bin/env python
import sys;

def check(pilihan):
	try:
		pilihan = int(pilihan);
	except Exception, e:
		print "input salah : %s" % pilihan;
		sys.exit(1);


def calculator(operasi, bilangan1, bilangan2):
	if(operasi == "1"):
		return [bilangan1 + bilangan2, "+"];
	if(operasi == "2"):
		return [bilangan1 - bilangan2, "-"];
	if(operasi == "3"):
		return [bilangan1 * bilangan2, "*"];
	if(operasi == "4"):
		return float(bilangan1) / float(bilangan2), "/";
	else:
		print "Operasi salah: %s" %operasi;
		sys.exit(1)


print "1.Tambah\n2.kurang\n3.kali\n4.bagi";
operasi = raw_input("masukan operasi:");
check(operasi);

bilangan1 = raw_input("insert first bil=");
check(bilangan1);
bilangan1 = int(bilangan1);

bilangan2 = raw_input("insert second bil =");
check(bilangan2);
bilangan2 = int(bilangan2);

hasil = calculator(operasi, bilangan1, bilangan2)
print "hasil: {0} {3} {1} ={2:.2f}".format(bilangan1, bilangan2, hasil[0], hasil[1]);
