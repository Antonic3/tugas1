def isPalindrome(x):
    str_x = str(x)
    return str_x == str_x[::-1]

# Contoh penggunaan dengan input dari pengguna
input_number = int(input("Masukkan angka: "))
if isPalindrome(input_number):
    print(f"{input_number} is true")
else:
    print(f"{input_number} is false")
