bilangan = input("Masukkan bilangan:")
if (bilangan<=1):
	print "Masukkan bilangan yang lebih besar dari 1."
else:
	j = 0
	p = 1
	while(p<bilangan):
		if (bilangan%p==0):
			j = j + p 
		p = p + 1

if (j==bilangan):
	print bilangan,"is Perfect Number."
else:
	print bilangan,"BUKAN Perfect Number."