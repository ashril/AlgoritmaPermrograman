data = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# ok = "y" 
# while (ok=="y"):
# 	data.append(input("Masukkan Bilangan: "))
# 	ok = raw_input("Lanjut? (y/n) : ")
print "Bilangan dalam array adalah: ",data
# testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]

#Sequential Search
b = input("Cari: ")
i = 1
n = len(data)
find = 0
for i in range(n):
	if(b==data[i]):
		k=i
		find=1

if (find==1):
	print "Ketemu! ",b,"berada pada indeks",i
else:
	print "Tidak Ketemu"