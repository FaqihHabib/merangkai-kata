number1 = int(input("Masukkan angka pertama = "))
number2 = int(input("Masukkan angka kedua = "))

def pertambahan():
    return number1 + number2

def pengurangan():
    return number1 - number2

def perkalian():
    return number1 * number2

def pembagian():
    return number1 // number2 

def pilihan():
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    
    operasi = {
        '1': pertambahan,
        '2': pengurangan,
        '3': perkalian,
        '4': pembagian
    }

    pilihan = input("pilih satu angka yaaa (1/2/3/4): ")

    hasil = operasi[pilihan]()
    
    print(f"Hasil: {hasil}")

pilihan()