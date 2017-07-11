def faktorial(n):
	f = 1
	for i in range(1,n+1):
		f = f*i
	print "Nilai dari",n,"faktorial adalah",f

k = input("Angka: ")
faktorial(k)