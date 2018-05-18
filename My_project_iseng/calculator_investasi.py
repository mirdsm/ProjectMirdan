


modal = int(raw_input("Berapa Modal Investasi per Tahun (Juta Rupiah)?\n"))
ROI = int(raw_input("Rata-rata Return of Investmennya? (%)\n"))
jangka = int(raw_input("Jangka waktu berapa? (tahun)\n"))
ROI = ROI * 0.01
modal_tetap = modal
modal_1 = 0
for i in range(0,jangka):
    modal  = modal_tetap + modal_1
    untung = modal * ROI
    modal_1 = modal + untung

print "_" * 10, "Nilai Investasi" , "_" * 10
print " "
print "Rp.",modal_1, "Juta"
