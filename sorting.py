numbers = input("Enter numbers separated by spaces: ")
num_list = list(map(int, numbers.split()))
num_list.sort()
print("Sorted numbers:", num_list)
