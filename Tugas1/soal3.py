if __name__ == "__main__":
    """mengkonversi jumlah hari tertentu ke dalam bentuk:
        'x' tahun 'y' bulan 'z' minggu 'n' hari
    """
    daysInWeek = 7 # hari
    daysInMonth = 30 # hari
    daysInYear = 360 # hari
    numberDays = 190 # hari

    years = numberDays//daysInYear
    month = (numberDays%daysInYear)//daysInMonth
    weeks = (numberDays%daysInMonth)//daysInWeek
    days = numberDays%daysInYear%daysInMonth%daysInWeek
    print(f'{numberDays} hari = {years} tahun {month} bulan {weeks} minggu {days} hari')
