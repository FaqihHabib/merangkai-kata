text = (input("Masukkan kalimat : "))

vocal = 'a','i','u','e','o'
total_vocal = 0
n = 0

while n in len(text):
    if text[n] in vocal:
        total_vocal +=1
    n += 1

print(f"Total karakter : {len(text)}")
print(f"Huruf vokal : {total_vocal}")
