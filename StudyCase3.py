username_benar = True
password_benar = True
gunakan_username = True
gunakan_email = False
otp = True
biometrik = False

login = username_benar and password_benar
akses = gunakan_username or gunakan_email
verifikasi_tambahan = otp != biometrik

print("Login:", login)
print("Akses tersedia:", akses)
print("Verifikasi tambahan:", verifikasi_tambahan)
