with open("input.txt", "r") as fd:
    s = fd.readline()[:-1]
    ranges = s.split(",")
    lower_limits = []
    upper_limits = []

    for r in ranges:
        lower_limits.append(int(r.split("-")[0]))
        upper_limits.append(int(r.split("-")[1]))


def num_is_invalid(num: int) -> bool:
    num_str = str(num)

    if len(num_str) % 2 == 1:
        return False

    idx = len(num_str) // 2
    if num_str[:idx] == num_str[idx:]:
        return True
    else:
        return False


running_sum = 0
for row_num in range(len(lower_limits)):
    # print(f"Checking ranges {lower_limits[row_num]} - {upper_limits[row_num]}")
    for num in range(lower_limits[row_num], upper_limits[row_num] + 1):
        if num_is_invalid(num):
            running_sum += num
            # print(f"{num}, ", end="")
    # print()

print(f"The total sum of all invalid Product IDs is {running_sum}")
