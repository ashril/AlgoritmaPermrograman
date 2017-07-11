#Input Bilangan
array = []
ok = "y" 
while (ok=="y"):
	array.append(input("Masukkan Bilangan: "))
	ok = raw_input("Lanjut? (y/n) : ")
print "Bilangan dalam array adalah: ",array

#Hitung Rata-rata
jumlah = 0.
for i in range(len(array)):
	jumlah = jumlah+array[i]
rata_rata = jumlah/len(array)

print "Rata-ratanya adalah:",rata_rata