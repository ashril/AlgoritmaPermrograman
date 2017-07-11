#Input Bilangan dalam List
data = []
ok = "y" 
while (ok=="y"):
	data.append(input("Masukkan Bilangan: "))
	ok = raw_input("Lanjut? (y/n) : ")
print "Bilangan dalam array adalah: ",data

#Bubble Sort
d = 0
n=(len(data)-1)
while(d<=(n)):
	c = n
	while(c!=d):
		if ((data[c-1])>(data[c])):
			titip=data[c-1]
			data[c-1]=data[c]
			data[c]=titip
		c = c-1
	d=d+1

print "Bilangan setelah diurutkan dengan Bubble Sort adalah: ",data