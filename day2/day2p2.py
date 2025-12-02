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

    for num_parts in range(2, len(num_str) + 1):
        if len(num_str) % num_parts != 0:
            continue

        end_idx = len(num_str) // num_parts
        if num_str == num_str[:end_idx] * num_parts:
            return True

    return False


running_sum = 0
for row_num in range(len(lower_limits)):
    # print(f"Checking ranges {lower_limits[row_num]} - {upper_limits[row_num]}")
    for num in range(lower_limits[row_num], upper_limits[row_num] + 1):
        if num_is_invalid(num):
            running_sum += num
    #         print(f"{num}, ", end="")
    # print()

print(f"The total sum of all invalid Product IDs is {running_sum}")
