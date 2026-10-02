anggota = True
tidak_ada_denda = True
kartu_mahasiswa = True
kartu_pelajar = False

boleh_meminjam = anggota and tidak_ada_denda
identitas_valid = kartu_mahasiswa or kartu_pelajar
akses_khusus = kartu_mahasiswa != kartu_pelajar

print("Boleh meminjam:", boleh_meminjam)
print("Identitas valid:", identitas_valid)
print("Akses khusus:", akses_khusus)