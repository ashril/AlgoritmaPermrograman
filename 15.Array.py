#Input Bilangan
array = []
ok = "y" 
while (ok=="y"):
	array.append(input("Masukkan Bilangan: "))
	ok = raw_input("Lanjut? (y/n) : ")
print "Bilangan dalam array adalah: ",array

#Hitung Hasil Kali
hasil_kali = 1
for i in range(len(array)):
	hasil_kali = hasil_kali*array[i]
print "Jumlah hasil kalinya adalah:",hasil_kali
