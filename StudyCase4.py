umur_sesuai = True
sudah_mendaftar = True
pengalaman = False
sertifikat = True

boleh_mengikuti = umur_sesuai and sudah_mendaftar
kategori_tambahan = pengalaman or sertifikat
jalur_khusus = pengalaman != sertifikat

print("Boleh mengikuti:", boleh_mengikuti)
print("Kategori tambahan:", kategori_tambahan)
print("Jalur khusus:", jalur_khusus)
