wordword = (input("Masukkan kalimat yang puitis : "))

print(f"total karakter : {len(wordword)}")
vookal = 0
for word in wordword :
    if word in ['o','e','u','i','a']:
        vookal += 1

print(f"Total huruf vokal adalah : {vookal}")