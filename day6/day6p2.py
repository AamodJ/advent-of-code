import numpy as np

with open("input.txt", "r") as fd:
    s = np.array([list(line[:-1]) for line in fd.readlines()])


grand_total = 0
current_op_num_list = []
for idx in range(s.shape[1]):
    num = "".join(s[:, s.shape[1] - 1 - idx]).strip()
    if num == "":
        continue
    if num[-1] == "*":
        current_op_num_list.append(num[:-1])
        grand_total += np.array(current_op_num_list).astype(int).prod()
        current_op_num_list = []
    elif num[-1] == "+":
        current_op_num_list.append(num[:-1])
        grand_total += np.array(current_op_num_list).astype(int).sum()
        current_op_num_list = []
    else:
        current_op_num_list.append(num)

print(f"Grand total: {grand_total}")
