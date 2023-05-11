if __name__ == "__main__":
    """Menentukan umur dua orang tertentu berdasarkan
    jumlah umur mereka dan perbandingan/rasio umur mereka
    """
    # perbandingan umur dan jumlah umur (tahun)
    a = 2 # perbandingan kedua umur adalah 0.4 atau 4 : 10 atau bisa juga ditulis 2 : 5
    b = 5
    total_ab = 49

    # rumus mencari umur masing2 setelah 2 tahun : Andi = ((perbandingan Andi/total penjumlahan perbandingan)*total kedua umur) + 2
    Andi_2thn = ((a/(a+b))*total_ab) + 2
    Budi_2thn = ((b/(a+b))*total_ab) + 2

    print(f'Usia Andi setelah 2 tahun lagi adalah {Andi_2thn} tahun\nUsia Budi setelah 2 tahun lagi adalah {Budi_2thn} tahun')
