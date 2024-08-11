from collections import Counter

def singleNumbers(nums):
    count = Counter(nums)
    result = [num for num, freq in count.items() if freq == 1]
    return result

# Menerima input dari pengguna
input_nums = input("Masukkan angka-angka yang dipisahkan dengan koma: ")
nums = list(map(int, input_nums.split(',')))

print("Angka yang hanya muncul sekali adalah:", singleNumbers(nums))
