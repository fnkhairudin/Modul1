if __name__ == "__main__":
    """Menentukan pada jam berapa ketika
        2 benda berpapasan yang berada pada jarak tertentu
        dan bergerak saling mendekati pada jam berangkat yang sama
    """
    import math
    # waktu berangkat kedua mobil adalah sama, yaitu pukul 09.00 WIB
    kec_A = 60 # km/jam dari timur
    kec_B = 40 # km/jam dari barat
    jarak_total = 120 # km

    # menghitung waktu yang dibutuhkan untuk saling bertabrakan
    waktu_jam = jarak_total/(kec_A + kec_B)
    jam = math.floor(waktu_jam)
    menit = round((waktu_jam - jam)*60,0)
    print(f'waktu yang dibutuhkan untuk saling bertabrakan adalah {jam} jam {menit} menit\nsehingga mobil A dan mobil B akan bertabrakan pada pukul 10.12 WIB')
