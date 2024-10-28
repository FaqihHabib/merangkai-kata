text = (input("Masukkan kalimat : "))

vocal = 'a','i','u','e','o'
total_vocal = 0

for letter in text:
    if letter in vocal:
        total_vocal +=1

print(f"Total karakter : {len(text)}")
print(f"Huruf vokal : {total_vocal}")
