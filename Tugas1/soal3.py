if __name__ == "__main__":
    import math
    """mengkonversi jumlah hari tertentu ke dalam bentuk:
        'x' tahun 'y' bulan 'z' minggu 'n' hari
    """
    days_in_week = 7 # hari
    days_in_month = 30 # hari
    days_in_year = 360 # hari
    number_days = 385 # hari

    years = math.floor(number_days/days_in_year)
    months = math.floor((number_days - days_in_year)/days_in_month)
    weeks = math.floor((number_days - days_in_year - (days_in_month * months))/days_in_week)
    days = number_days - days_in_year - (days_in_month * months) - weeks
    print(f'{number_days} hari sama saja nilainya dengan {years} tahun {months} bulan {weeks} minggu {days} hari')
