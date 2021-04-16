print("****************************")
print("Perhitungan Pada Segitiga Siku-Siku")

import math
a = float(input("Masukkan sisi alas: "))
b = float(input("Masukkan sisi tinggi: "))
c = float(input("Masukkan sisi miring: "))

#mencari luas segitiga dan pembulatan keatas
luas = 1/2 * a * b
print("Luas segitiga siku-siku adalah", luas, "cm persegi")
print("Hasil pembulatan keatas luas segitiga siku-siku adalah", math.ceil(luas), "cm persegi")
print()

#mencari keliling segitiga dan pembulatan kebawah
keliling = a+b+c
print("Keliling segitiga siku-siku adalah", keliling, "cm")
print("Hasil pembulatan kebawah keliling segitiga siku-siku adalah", math.floor(keliling), "cm")
print()

#mencari panjang sisi terpanjang dan terpendek serta pembulatan keatas dan kebawah
terpanjang = max(a, b, c)
print("Panjang sisi terpanjang segitiga siku-siku adalah", max(a, b, c), "cm")
print("Hasil pembulatan keatas untuk sisi terpanjang segitiga adalah", math.ceil(terpanjang), "cm")
print("Hasil pembulatan kebawah untuk sisi terpanjang segitiga adalah", math.floor(terpanjang), "cm")
terpendek = min(a, b, c)
print("Panjang sisi terpendek segitiga siku-siku adalah", min(a, b, c), "cm")
print("Hasil pembulatan keatas untuk sisi terpendek segitiga siku-siku adalah", math.ceil(terpendek), "cm")
print("Hasil pembulatan kebawah untuk sisi terpendek segitiga siku-siku adalah", math.floor(terpendek), "cm")
(print)