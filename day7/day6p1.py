import time

start_time = time.time()
with open("input.txt", "r") as fd:
    s = [line.strip() for line in fd.readlines()]

current_beams = [s[0].index("S")]
new_beams = [b for b in current_beams]

total_splits = 0

for level in range(len(s)):
    for beam in current_beams:
        if s[level][beam] == ".":
            s[level] = s[level][:beam] + "|" + s[level][beam + 1 :]
            continue
        elif s[level][beam] == "^":
            new_beams.remove(beam)
            total_splits += 1
            if s[level][beam - 1] == ".":
                s[level] = s[level][: beam - 1] + "|^" + s[level][beam + 1 :]
                if beam - 1 not in new_beams:
                    new_beams.append(beam - 1)
            if s[level][beam + 1] == ".":
                s[level] = s[level][:beam] + "^|" + s[level][beam + 2 :]
                if beam + 1 not in new_beams:
                    new_beams.append(beam + 1)
    current_beams = [b for b in new_beams]

    # if level == 10:
    #     break
for line in s:
    print(line)

print(f"Total number of splits {total_splits}, with time: {time.time() - start_time}s")
