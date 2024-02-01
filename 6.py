shift = int(input("Сдвинг: "))
original_list = [1, 2, 3, 4, 5]  # мы не прошли это, например: .pop
shifted_list = []
shift %= len(original_list)

for i in range(shift, 0, -1):
    shifted_list.append(original_list[-1 * i])

for j in range(len(original_list) - shift):
    shifted_list.append(original_list[j])

print(shifted_list)

