film_tersedia = True
pembayaran_berhasil = True
member = True
voucher = False

tiket_berhasil = film_tersedia and pembayaran_berhasil
mendapat_diskon = member or voucher
promo_khusus = member != voucher

print("Tiket berhasil:", tiket_berhasil)
print("Mendapat diskon:", mendapat_diskon)
print("Promo khusus:", promo_khusus)