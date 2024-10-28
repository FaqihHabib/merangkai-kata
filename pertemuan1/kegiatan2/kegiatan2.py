def sambutan(nama):
    return f"selamat datang, {nama}!"

faqih=sambutan("selamat datang faqih")
print(faqih)


#PENJUMLAHAN ANGKA

def penjumlahan_angka():
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        
        hasil = angka1 + angka2
        
        print(f"\nHasil dari {angka1} + {angka2} = {hasil}")
        
        print("Keren bangetttt!!!")
    
    except ValueError:
        print("Inputnya salah nih, masukkin angka yang benar!!")

penjumlahan_angka()


#HITUNG LUASS

import math

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def luas_persegi(sisi):
    return sisi * sisi

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari * jari_jari

def input_segitiga():
    alas = float(input("alas segitiga: "))
    tinggi = float(input("tinggi segitiga: "))
    return luas_segitiga(alas, tinggi)

def input_persegi():
    sisi = float(input("panjang sisi persegi: "))
    return luas_persegi(sisi)

def input_lingkaran():
    jari_jari = float(input("jari-jari lingkaran: "))
    return luas_lingkaran(jari_jari)

def pilihan_tidak_valid():
    raise ValueError("PILIHAN TIDAK VALIIIIIDD")

pilihan_fungsi = {
    '1': input_segitiga,
    '2': input_persegi,
    '3': input_lingkaran
}

def main():
    print("1. Segitiga")
    print("2. Persegi")
    print("3. Lingkaran")
    
    pilihan = input("pilih satu angka yaaa (1/2/3): ")

    luas = pilihan_fungsi.get(pilihan, pilihan_tidak_valid)()
    print(f"Luas: {luas}")

main()

#HITUNG AKAR KUADRATT
import math 

def akar_kuadrat(angka):
    return math.sqrt(angka) if angka >= 0 else (_ for _ in ()).throw(ValueError("Input harus angka non-negatif."))

def main():
    try:
        angka = float(input("Masukkan angka untuk dihitung akar kuadrat: "))
        hasil = akar_kuadrat(angka)
        print(f"Akar kuadrat dari {angka} adalah {hasil}")
    except ValueError as e:
        print(e)


main()


