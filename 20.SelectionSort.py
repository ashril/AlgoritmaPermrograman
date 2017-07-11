#Fungsi Selection Sort
def selectionSort(alist):
	for fillslot in range(len(alist)-1,0,-1):
		positionOfMax=0
		for location in range(1,fillslot+1):
			if alist[location]>alist[positionOfMax]:
				positionOfMax = location
		temp = alist[fillslot]
		alist[fillslot] = alist[positionOfMax]
		alist[positionOfMax] = temp
	print "Bilangan setelah diurutkan dengan Selection Sort adalah: ",alist

#Input Bilangan dalam List
alist = []
ok = "y" 
while (ok=="y"):
	alist.append(input("Masukkan Bilangan: "))
	ok = raw_input("Lanjut? (y/n) : ")
print "Bilangan dalam array adalah: ",alist

selectionSort(alist)