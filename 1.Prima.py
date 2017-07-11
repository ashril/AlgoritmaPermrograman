bilangan = int(input('Masukkan bilangan = '))
cek = 1
for i in range (2,bilangan):
	if (bilangan%i==0):
		cek = 0

if (cek == 0 or bilangan<2):
	print bilangan,"BUKAN bilangan PRIMA"
else:
	print bilangan,"adalah bilangan PRIMA"
