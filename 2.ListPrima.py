n = input ("Masukkan batas bilangan: ")
for i in range (2,n):
	cek = 1
	for j in range (2,i):
		if (i%j==0):
			cek = 0
	if (cek==1):
		print i,
