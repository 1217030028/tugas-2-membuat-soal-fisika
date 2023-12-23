# Soal 2: Hukum Newton
def massa_dengan_gaya(gaya, percepatan):
    massa = gaya / percepatan
    return massa

gaya_benda = 10  # N
percepatan_benda = 5  # m/s^2

massa_benda = massa_dengan_gaya(gaya_benda, percepatan_benda)
print("Massa benda:", massa_benda, "kg")
