number = int(input("Masukkan angka : "))
pangkat = int (input("Masukkan pangkat : "))

total = 1

for n in range(pangkat):
    total *= number

print(f"Hasilnya : {total}")