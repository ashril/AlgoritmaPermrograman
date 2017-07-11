def binarySearch(data, cari):
	i = 0
	h = len(data)-1
	found = False

	while i<=h and not found:
		m = (i + h)//2
		if data[m] == cari:
			found = True
		else:
			if cari < data[m]:
				h = m-1
			else:
				i = m+1
	return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print testlist
cari = input("Cari: ")
k = binarySearch(testlist,cari)
if (k==True):
	print "Ketemu"
else:
	print "Tidak Ketemu"