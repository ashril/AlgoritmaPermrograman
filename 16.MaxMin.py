#Input Bilangan
array = []
ok = "y" 
while (ok=="y"):
	array.append(input("Masukkan Bilangan: "))
	ok = raw_input("Lanjut? (y/n) : ")
print "Bilangan dalam array adalah: ",array

# Cari Max Min
max = array[0]
min = array[0]
for i in range(len(array)):
	if array[i]>max:
		max=array[i]
	if array[i]<min:
		min=array[i]

print "Terbesar:",max
print "Terkecil:",min