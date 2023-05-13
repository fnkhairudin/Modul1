if __name__ == "__main__":
    """mengkonversi jumlah hari tertentu ke dalam bentuk:
        'x' tahun 'y' bulan 'z' minggu 'n' hari
    """
    days_in_week = 7 # hari
    days_in_month = 30 # hari
    days_in_year = 360 # hari
    number_days = 485 # hari

    years = number_days//days_in_year
    month = (number_days%days_in_year)//days_in_month
    weeks = (number_days%days_in_month)//days_in_week
    days = abs(number_days - (years*days_in_year + month*days_in_month + weeks*days_in_week))
    print(f'{number_days} hari = {years} tahun {month} bulan {weeks} minggu {days} hari')
