jam_kerja = input("Masukkan jumlah jam kerja:")
honor_perjam = input("Masukkan upah kerja per jam:")
honor = jam_kerja * honor_perjam
if (jam_kerja>40):
	honor = honor + (jam_kerja-40)*(2*honor_perjam)
print "Honor yang diterima adalah",honor