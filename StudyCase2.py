pengalaman = True
pendidikan_sesuai = True
sertifikat = False
rekomendasi = True

diterima = pengalaman and pendidikan_sesuai
nilai_tambahan = sertifikat or rekomendasi
jalur_khusus = pengalaman != sertifikat

print("Diterima:", diterima)
print("Mendapat nilai tambahan:", nilai_tambahan)
print("Jalur khusus:", jalur_khusus)