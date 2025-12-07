import time

start_time = time.time()
with open("input.txt", "r") as fd:
    s = [line.strip() for line in fd.readlines()]


def printlevels(s: list, l=-1):
    for idx, level in enumerate(s):
        if l != -1 and idx >= l:
            break
        for col in level:
            print(f"{col}", end="\t")
        print()


num_s = []
for level in s:
    cur_level = list(level)
    num_level = []
    for col in cur_level:
        if col == ".":
            num_level.append(0)
        elif col == "^":
            num_level.append(-1)
        elif col == "S":
            num_level.append(1)
    num_s.append(num_level)


current_beams = [num_s[0].index(1)]
new_beams = [b for b in current_beams]

for level in range(1, len(num_s)):
    for beam in current_beams:
        if num_s[level][beam] == -1:
            new_beams.remove(beam)
            num_s[level][beam - 1] += num_s[level - 1][beam]
            if beam - 1 not in new_beams:
                new_beams.append(beam - 1)
            num_s[level][beam + 1] += num_s[level - 1][beam]
            if beam + 1 not in new_beams:
                new_beams.append(beam + 1)
        else:
            num_s[level][beam] += num_s[level - 1][beam]
    current_beams = [b for b in new_beams]

    # if level == 17:
    #     break

printlevels(num_s)

print(
    f"Total number of timelines {sum(num_s[-1])}, with time: {time.time() - start_time}s"
)
