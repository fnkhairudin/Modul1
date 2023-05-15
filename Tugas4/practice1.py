if __name__ == '__main__':
    def find(list, target):
        # meng-copy list agar urutan index berawal dari index 1 pada list sebelumnya, 
        # agar nanti bisa dilakukan pertambahan antara list dengan listCopy
        # dimana listCopy urutannya dimulai dari list[1]
        listCopy = list.copy()
        del listCopy[0]

        # melakukan looping dengan cara menambahkan list dengan listCopy dan mengisi index-nya ke dalam list kosong
        temporaryList = []
        for i, valueI in enumerate(list):
            for j, valueJ in enumerate(listCopy):
                if valueI+valueJ == target:
                    #print(f'yang menghasilkan target {target} adalah bilangan {valueI} dan {valueJ}')
                    if valueI == valueJ: # setelah mencapai target, kita cek lagi apakah value index ke-0 dan ke -1 di original list (sebelum di-copy) nilainya sama ?
                        temporaryList.append(list.index(valueI)) # jika sama, supaya yang di-append adalah index ke-0 dan ke-1, oleh karena itu append yang kedua ditambah satu 
                        temporaryList.append(listCopy.index(valueJ)+1) # bisa gunakan contoh kasus [2,2,4,5], kemudian targetnya 4
                    else:
                        temporaryList.append(list.index(valueI)) # selain conditional yang diatas akan dilakukan append seperti biasa
                        temporaryList.append(list.index(valueJ))

        # melakukan slicing, sehingga outputnya menjadi HANYA 2 index yang pertama
        # untuk lebih jelasnya bisa menghapus tanda comment pada perintah print diatas 
        trueList = temporaryList[0:2]
        return trueList
