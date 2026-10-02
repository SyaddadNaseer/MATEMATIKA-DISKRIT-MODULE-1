kartu_akses = True
ruangan_terbuka = True
mahasiswa = True
pegawai = False

boleh_masuk = kartu_akses and ruangan_terbuka
identitas_valid = mahasiswa or pegawai
akses_alternatif = mahasiswa != pegawai

print("Boleh masuk:", boleh_masuk)
print("Identitas valid:", identitas_valid)
print("Akses alternatif:", akses_alternatif)