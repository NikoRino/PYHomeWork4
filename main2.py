num_bush = int(input("Введите количество кустов черники: "))
arr = list()
for i in range(num_bush):
    a = int(input("Введите количество ягод на кусте: "))
    arr.append(a)

arr_count = list()
for i in range(len(arr)):
    arr_count.append(arr[i - 2] + arr[i - 1] + arr[i])
print(max(arr_count))
