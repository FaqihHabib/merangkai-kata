number = int(input("Masukkan angka : "))
pangkat = int (input("Masukkan pangkat : "))

total = 1
n = 0

while n < pangkat:
    total *= number
    n += 1

print(f"Hasilnya : {total}")