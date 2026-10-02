nilai_tes = True
kehadiran = True
pengalaman = True
sertifikat = True

lulus = nilai_tes and kehadiran
prioritas = pengalaman or sertifikat
jalur_khusus = pengalaman != sertifikat

print("Lulus:", lulus)
print("Prioritas:", prioritas)
print("Jalur khusus:", jalur_khusus)