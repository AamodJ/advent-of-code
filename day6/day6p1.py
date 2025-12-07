import numpy as np

with open("input.txt", "r") as fd:
    s = np.array([line.strip() for line in fd.readlines()])
    operations = np.array(s[-1].split())
    problems = np.array([line.split() for line in s[:-1]])


grand_total = 0
for idx, op in enumerate(operations):
    if op == "*":
        grand_total += problems[:, idx].astype(int).prod()
    elif op == "+":
        grand_total += problems[:, idx].astype(int).sum()


print(f"Grand total {grand_total}")
