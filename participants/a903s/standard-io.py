#!/usr/bin/env python
import sys;


def check (pilihan):
    try:
        return int(pilihan);
    except Exception, e:
        print "Input Salah: %s" % pilihan;
        sys.exit(1);


def calculator (operasi, bilangan1, bilangan2):
    if (operasi == 1):
        return [bilangan1 + bilangan2, "+"]
    if (operasi == 2):
        return [bilangan1 - bilangan2, "-"]
    if (operasi == 3):
        return [bilangan1 * bilangan2, "*"]
    if (operasi == 4):
        return [float(bilangan1) / float(bilangan2), "/"]
    else:
        print "Operasi salah: %s" % operasi
        sys.exit(1)

print "1. Tambah\n2. Kurang\n3. Kali\n4. Bagi"
operasi = check(raw_input("Masukkan Pilihan:"))
bilangan1 = check(raw_input("First number:"))
bilangan2 = check(raw_input("Second Number:"))
hasil = calculator(operasi, bilangan1, bilangan2)
print "Hasil: {0} {3} {1} = {2:.2f}" .format(bilangan1, bilangan2, hasil[0], hasil[1])
