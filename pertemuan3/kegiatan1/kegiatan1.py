
name = (input("Masukkan nama anda : "))
number = int (input("Masukkan tahun kelahiran anda : "))

if number >= 1944 and number <=1964:
    print(f"{name} berdasarkan tahun lahir anda tergolong generasi Baby Boomer")
elif number >= 1965 and number <=1979:
    print(f"{name} berdasarkan tahun lahir anda tergolong tergolong generasi X")
elif number >= 1980 and number <=1994:
    print(f"{name} berdasarkan tahun lahir anda tergolong tergolong generasi Y")
elif number >= 1995 and number <=2015:
    print(f"{name} berdasarkan tahun lahir anda tergolong tergolong generasi Z")

