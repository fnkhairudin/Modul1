if __name__ == '__main__':
    def find(nums, target):
        # meng-copy list agar urutan index berawal dari index 1 pada list sebelumnya, 
        # agar nanti bisa dilakukan pertambahan antara nums dengan nums.Copy
        # dimana nums.Copy urutannya dimulai dari nums[1]
        numsCopy = nums.copy()
        del numsCopy[0]

        # melakukan looping dengan cara menambahkan nums dengan numsCopy dan mengisi index-nya ke dalam list kosong
        list = []
        for i, valueI in enumerate(nums):
            for j, valueJ in enumerate(numsCopy):
                if valueI+valueJ == target:
                    #print(f'yang menghasilkan target {target} adalah bilangan {valueI} dan {valueJ}')
                    list.append(nums.index(valueI))
                    list.append(nums.index(valueJ))

        # melakukan slicing variable list diatas, sehingga outputnya menjadi HANYA 2 index yang pertama
        # untuk lebih jelasnya bisa menghapus tanda comment pada perintah print diatas 
        trueList = list[0:2]
        return trueList
