b_prima = (input("Berikan saya beberapa bilangan (pisah dengan spasi) : "))

def cek_number(z):
    if z < 2:
        return False
    for i in range(2, int(z**0.5) + 1):
        if z % i == 0:
            return False
    return True

number_list = map(int, b_prima.split())

for number in number_list:
    if cek_number(number):
        print(f"{number} merupakan bilangan prima.")
