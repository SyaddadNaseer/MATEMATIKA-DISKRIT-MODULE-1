aktif = True
nilai_memenuhi = True
berprestasi = True
sertifikat = False

lulus = aktif and nilai_memenuhi
prioritas = berprestasi or sertifikat
program_khusus = berprestasi != sertifikat

print("Lulus:", lulus)
print("Prioritas:", prioritas)
print("Program khusus:", program_khusus)