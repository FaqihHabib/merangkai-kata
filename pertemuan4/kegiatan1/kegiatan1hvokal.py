text = (input("Masukkan kalimat yang ingin diubah : "))
change_vocal = (input("Masukkan vokal pengganti : "))

for vocal in ['a','o','u','e','i']:
    text = text.replace (vocal, change_vocal)
    
print(f"Kalimat setelah huruf vokal dirubah menjadi : {text}")