import os
import Input

def fungsi_clear_terminal():
    sistem_operasi = os.name
    match sistem_operasi:
        case 'posix': os.system('clear')
        case 'nt': os.system('cls')

list_operasi = ['Keluar', 'Perkalian', 'Pembagian', 'Penjumlahan', 'Pengurangan']
banyakk_pilihan = len(list_operasi)
def fungsi_list_operasi():
    for nomor, operasi in enumerate(list_operasi, 1):
        print(f'{nomor}. {operasi}')

if __name__ == '__main__':
    while True:
        fungsi_clear_terminal()
        print(f'{'CALCULATOR':^25}')
        print('=' * 25)
        print('Silakan pilih operasi\n')
        
        fungsi_list_operasi()

        input_user = Input.fungsi_input_operasi(banyakk_pilihan)

        match input_user:
            case 1: break 
            case 2: print('Perkalian') 
            case 3: print('Pembagian') 
            case 4: print('Penjumlahan') 
            case 5: print('Pengurangan') 
    
        is_done = input('Apakah ingin keluar (Y/n)? ')
        if is_done.lower() == 'y' or is_done == '':
            break
        elif is_done.lower() == 'n':
            pass
        else:
            print('Input tidak valid, keluar dari program.')
            break
    print('Program selesai.')
    