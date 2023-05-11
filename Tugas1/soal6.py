if __name__ == "__main__":
    """ Menghitung total harga berdasarkan
        jumlah item yang dibeli
    """
    jumlah_apel = int(input("masukkan jumlah apel: "))
    jumlah_jeruk = int(input("masukkan jumlah jeruk: "))
    jumlah_anggur = int(input("masukkan jumlah anggur: "))

    harga_apel = 10_000
    harga_jeruk = 15_000
    harga_anggur = 20_000

    list_total_harga = [jumlah_apel*harga_apel, jumlah_jeruk*harga_jeruk, jumlah_anggur*harga_anggur]

    print('\n---------Detail Belanja---------')
    print(f'Apel : {jumlah_apel} x {harga_apel} = {list_total_harga[0]}')
    print(f'Jeruk : {jumlah_jeruk} x {harga_jeruk} = {list_total_harga[1]}')
    print(f'Anggur : {jumlah_anggur} x {harga_anggur} = {list_total_harga[2]}')

    print(f'\nTotal belanja hari ini adalah {sum(list_total_harga)} Rupiah')
