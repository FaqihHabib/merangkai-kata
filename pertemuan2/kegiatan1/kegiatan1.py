def count_winrate(win, ttl_match):
    return (win / (ttl_match + (ttl_match == 0))) * 100

def main():
    jeneng = input("Masukkan nama klub atau atlet: ")
    win = int(input("Masukkan jumlah pertandingan yang dimenangkan: "))
    ttl_match = int(input("Masukkan jumlah total pertandingan: "))
    
    persentase = count_winrate(win, ttl_match)

    print(f"{jeneng} memenangkan {win} dari {ttl_match} pertandingan.")
    print(f"Persentase kemenangan: {persentase:.2f}%")

main()
