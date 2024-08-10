def fungsi_input_operasi(banyak_pilihan):
    while True:
        try:
            input_operasi = int(input('\nPilih Operasi: '))
            if 0 < input_operasi < banyak_pilihan:
                break
            else:
                print('Pilihan tidak tersedia.')
        except:
            print('Tolong masukkan angka.')
    return input_operasi