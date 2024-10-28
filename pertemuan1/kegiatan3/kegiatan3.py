import math

def hitung_diskriminan(a, b, c):
    return b ** 2 - 4 * a * c

def hitung_akar_kuadrat(a, b, c):
    D = hitung_diskriminan(a, b, c)
    
    if D >= 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-D) / (2 * a)
        x1 = f"{real_part} + {imag_part}i"
        x2 = f"{real_part} - {imag_part}i"
    
    return x1, x2

def soal_pertama():
    print("Menyelesaikan persamaan: ax + b * x^2 + c = 0")
    
    a = float(input("Masukkan nilai a (koefisien x): "))
    b = float(input("Masukkan nilai b (koefisien x^2): "))
    c = float(input("Masukkan nilai c (konstanta): "))
    
    x1, x2 = hitung_akar_kuadrat(b, a, c)  
    
    print(f"Akar-akar dari persamaan tersebut adalah: x1 = {x1}, x2 = {x2}\n")

def soal_kedua():
    print("Menyelesaikan persamaan: x^2 - 3x - 28 = 0")
    
    a, b, c = 1, -3, -28
    
    x1, x2 = hitung_akar_kuadrat(a, b, c)
    
    print(f"Akar-akar dari persamaan kedua adalah: x1 = {x1}, x2 = {x2}\n")

def soal_ketiga():
    print("Menyelesaikan persamaan: 3x^2 + 2x - 5 = 0")
    
    a, b, c = 3, 2, -5
    
    x1, x2 = hitung_akar_kuadrat(a, b, c)
    
    print(f"Akar-akar dari persamaan ketiga adalah: x1 = {x1}, x2 = {x2}\n")

soal_pertama()  # ax + b * x^2 + c = 0
soal_kedua()    # x^2 - 3x - 28 = 0
soal_ketiga()   # 3x^2 + 2x - 5 = 0