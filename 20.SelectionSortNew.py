#Input Bilangan dalam List
data = []
ok = "y" 
while (ok=="y"):
	data.append(input("Masukkan Bilangan: "))
	ok = raw_input("Lanjut? (y/n) : ")
print "Bilangan dalam array adalah: ",data

#Selection Sort
d = 0
n=len(data)
while(d<=(n-1)):
	p = d
	c = d+1
	while(c<n):
		if ((data[c])<(data[p])):
			p = c
		c = c+1
	titip=data[d]
	data[d]=data[p]
	data[p]=titip
	d=d+1

print "Bilangan setelah diurutkan dengan Selection Sort adalah: ",data