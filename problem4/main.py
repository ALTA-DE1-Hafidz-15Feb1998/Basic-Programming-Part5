def muncul_sekali(angka):
    # Membuat dictionary untuk menghitung berapa kali setiap angka muncul
    count_dict = {}
    
    # Menghitung frekuensi munculnya setiap angka dalam string
    for digit in angka:
        if digit in count_dict:
            count_dict[digit] += 1
        else:
            count_dict[digit] = 1
    
    # Membuat list untuk menyimpan angka yang hanya muncul satu kali
    result = []
    for digit, count in count_dict.items():
        if count == 1:
            result.append(int(digit))
    
    return result

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]